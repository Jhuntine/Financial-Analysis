"""Checkpoint 1's seven tools, extended for fiscal-week quarterly releases."""
from datetime import datetime
from pathlib import Path
import re
import sys

PREVIOUS = Path(__file__).resolve().parents[1] / "Checkpoint 1"
sys.path.insert(0, str(PREVIOUS))
from desk import Desk, write_json


def numeric_cells(line):
    return [float(s.strip().replace(",", "").replace("$", "")) for s in line.split("|")
            if re.fullmatch(r"\s*\$?\s*[\d,]+(?:\.\d+)?\s*", s)]


class CourseDesk(Desk):
    def calculate(self,ticker,include_price=False):
        if include_price and self.market_provider=="wrds":
            from market_adapter import get_wrds_close
            receipt=get_wrds_close(ticker,self.price_date,self.run_dir,self.sec.offline)
            self.price,self.price_source=receipt["close_usd"],receipt["source"]
            self.market_provider=None
            try:return super().calculate(ticker,include_price)
            finally:self.market_provider="wrds"
        return super().calculate(ticker,include_price)

    def _quarter_observations(self, doc, quarter_end=None):
        lines = doc["lines"]
        statement = next((i for i,t in enumerate(lines) if re.search(
            r"consolidated statements? of (income|operations|earnings)", t, re.I)), None)
        if statement is None:
            raise ValueError("Release has no identifiable consolidated GAAP income statement.")
        revenue_label = self.facts[self.ticker]["revenue"]["source_text"].split("|")[0].strip()
        candidates = [i for i in range(statement+1, min(statement+100,len(lines)))
                      if re.match(r"^(total revenue|net revenue|revenue|net sales)s?\s*\|",lines[i],re.I)
                      and len(numeric_cells(lines[i]))>=2]
        same = [i for i in candidates if lines[i].split("|")[0].strip().casefold()==revenue_label.casefold()]
        if len(same)!=1:
            raise ValueError("Quarterly revenue must use the annual filing's same explicit revenue definition.")
        ri=same[0]
        headers=lines[statement:ri]
        combined=" ".join(headers)
        scale_match=re.search(r"in (millions|thousands|billions)",combined,re.I)
        if not scale_match:
            raise ValueError("Quarterly monetary units are absent.")
        scale_name=scale_match[1].lower()
        scale={"millions":1_000_000,"thousands":1_000,"billions":1_000_000_000}[scale_name]
        duration=re.search(r"(Three|\d+)\s+(Months|Weeks)\s+Ended",combined,re.I)
        if not duration or (duration[2].lower()=="months" and duration[1].lower() not in {"three","3"}) or (
                duration[2].lower()=="weeks" and not 10<=int(duration[1])<=17):
            raise ValueError("First statement columns are not an identifiable fiscal quarter.")
        full_dates=re.findall(r"[A-Z][a-z]+\s+\d{1,2},\s+\d{4}",combined)
        if full_dates:
            quarter_end=datetime.strptime(full_dates[0],"%B %d, %Y").date().isoformat()
            prior_end=datetime.strptime(full_dates[1],"%B %d, %Y").date().isoformat() if len(full_dates)>1 else None
        else:
            month_day=re.search(r"Ended\s+([A-Z][a-z]+\s+\d{1,2}),?",combined)
            years=re.findall(r"\b20\d{2}\b",combined)
            if not month_day or len(years)<2:
                raise ValueError("Quarter columns do not identify their dates.")
            quarter_end=datetime.strptime(month_day[1]+", "+years[0],"%B %d, %Y").date().isoformat()
            prior_end=datetime.strptime(month_day[1]+", "+years[1],"%B %d, %Y").date().isoformat()
        if not prior_end or prior_end>=quarter_end:
            raise ValueError("Quarter comparison dates are missing or reversed.")
        # A direct diluted-EPS row or a labelled share-class row after its heading.
        ei=None
        for i in range(ri+1,min(ri+100,len(lines))):
            if re.search(r"shares used|weighted.average shares|shares outstanding",lines[i],re.I):
                continue
            if re.match(r"^Diluted(?:\s+(?:Earnings|Net Income).*?(?:Per Share)?)?\s*\|",lines[i],re.I) and len(numeric_cells(lines[i]))>=2:
                ei=i;break
            if re.match(r"^Diluted (Earnings|Net Income).*Per Share",lines[i],re.I):
                ei=next((j for j in range(i+1,min(i+8,len(lines)))
                         if re.match(r"^Class A common stock\s*\|",lines[j],re.I) and len(numeric_cells(lines[j]))>=2),None)
                if ei is not None:break
        if ei is None:
            raise ValueError("Release has no unambiguous GAAP diluted-EPS row.")
        rv,ev=numeric_cells(lines[ri]),numeric_cells(lines[ei])
        if rv[1]<=0:
            raise ValueError("Quarter comparison denominator must be positive.")
        current,prior=rv[0]*scale,rv[1]*scale
        dimensions=self.facts[self.ticker]["diluted_eps"].get("dimensions",{})
        share_class=next(iter(dimensions.values()),"listed common stock; no separate class dimension")
        duration_text=duration[0].removesuffix(" Ended").lower()
        observations={
            "quarter_net_revenue":{"value":current,"unit":"USD","line":ri+1,"column":f"First quarter column; {duration_text} ended {quarter_end}; {revenue_label}; source in {scale_name}","column_index":0,"scale":scale,"period_end":quarter_end},
            "prior_quarter_net_revenue":{"value":prior,"unit":"USD","line":ri+1,"column":f"Second quarter column; corresponding quarter ended {prior_end}; {revenue_label}; source in {scale_name}","column_index":1,"scale":scale,"period_end":prior_end},
            "quarter_gaap_diluted_eps":{"value":ev[0],"unit":"USD/shares","line":ei+1,"column":f"First quarter column; GAAP diluted EPS; {duration_text} ended {quarter_end}; {share_class}","column_index":0,"scale":1,"period_end":quarter_end},
        }
        if re.search(r"(?:Twelve|12) Months Ended|(?:52|53) Weeks Ended",combined,re.I) and len(ev)>=4:
            observations["annual_release_gaap_diluted_eps"]={"value":ev[2],"unit":"USD/shares","line":ei+1,
                "column":f"Third numeric column; full fiscal year ended {quarter_end}; GAAP diluted EPS; {share_class}","column_index":2,"scale":1,"period_end":quarter_end}
        return {"period_end":quarter_end,"prior_period_end":prior_end,"quarter_duration":duration_text,
                "release_date":doc["filing"]["report_date"],"accession":doc["filing"]["accession"],"file":doc["file"],"url":doc["url"],
                "column_headers_lines":[i+1 for i in range(statement,ri) if re.search(r"(Weeks|Months) Ended|in (millions|thousands|billions)|20\d{2}",lines[i],re.I)],
                "observations":observations,"calculated_quarter_revenue_growth":{"value":(current/prior-1)*100,"unit":"%",
                    "arithmetic":f"({current:,.0f} / {prior:,.0f} - 1) * 100","line":ri+1,
                    "note":"Same consolidated revenue definition and corresponding fiscal-quarter columns; not headline net-sales growth."},
                "extraction_note":"Explicit fiscal-quarter headers, unit scale, total/net revenue label and diluted EPS row determine the observations."}

    def release_quarter(self):
        doc=self.documents[self.ticker]["earnings"]
        observations=self._quarter_observations(doc)
        def item(metric):
            n=observations["observations"][metric]["line"]
            return {"line":n,"text":doc["lines"][n-1]}
        result={"period_end":observations["period_end"],"release_date":observations["release_date"],
                "accession":observations["accession"],"file":doc["file"],"url":doc["url"],
                "revenue_candidates":[item("quarter_net_revenue")],"eps_candidates":[item("quarter_gaap_diluted_eps")],
                "header_lines":[{"line":n,"text":doc["lines"][n-1]} for n in observations["column_headers_lines"]],
                "observations":observations["observations"],"revenue_growth":observations["calculated_quarter_revenue_growth"]}
        write_json(self.run_dir/"quarter_observations.json",observations)
        write_json(self.run_dir/self.ticker/"quarter_source_lines.json",result)
        self.quarter=result
        return result

    def save(self):
        result=super().save()
        for name in ("human_audit.md","human_signoff.md"):
            path=self.run_dir/name
            text=path.read_text(encoding="utf-8").replace("Checkpoint 1 human audit","Checkpoint 2 human audit")
            if not self.facts[self.ticker]["diluted_eps"].get("dimensions"):
                text=text.replace("listed Class A","listed common stock").replace("Class A GAAP","listed-common-stock GAAP")
            path.write_text(text,encoding="utf-8")
        return result
