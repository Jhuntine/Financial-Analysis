"""Read-only WRDS daily close using the dated security ticker, not company.tic."""
from datetime import datetime,timezone
import hashlib
import math
import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

QUERY="""SELECT d.gvkey, c.conm, d.tic, d.iid, d.datadate, d.prccd, d.curcdd
FROM comp.secd AS d
JOIN comp.company AS c ON c.gvkey=d.gvkey
WHERE d.tic=%s AND d.iid=c.priusa AND d.datadate=%s
ORDER BY d.gvkey,d.iid
LIMIT 2"""


def get_wrds_close(ticker,trade_date,run_dir,offline=False):
    from market_data import verify_receipt
    from verifier import write_json
    if offline:return verify_receipt(run_dir,ticker,trade_date,"wrds")
    import psycopg2
    load_dotenv(Path(__file__).resolve().parents[1]/".env",override=False)
    if not os.getenv("WRDS_USERNAME") or not os.getenv("WRDS_PASSWORD"):
        raise RuntimeError("WRDS credentials are not configured.")
    try:
        connection=psycopg2.connect(host="wrds-pgdata.wharton.upenn.edu",port=9737,dbname="wrds",
            user=os.environ["WRDS_USERNAME"],password=os.environ["WRDS_PASSWORD"],sslmode="require",
            connect_timeout=15,options="-c statement_timeout=45000")
        try:
            connection.set_session(readonly=True)
            with connection.cursor() as cursor:
                cursor.execute(QUERY,(ticker,trade_date))
                rows=cursor.fetchall()
                names=[c.name for c in cursor.description]
        finally:connection.close()
    except Exception:
        raise RuntimeError("WRDS close retrieval failed; no replacement price was supplied.") from None
    if len(rows)!=1:raise ValueError("WRDS did not return exactly one primary U.S. security/date observation.")
    row=dict(zip(names,rows[0]))
    value=float(row["prccd"])
    if row["curcdd"]!="USD" or not math.isfinite(value) or value<=0:
        raise ValueError("WRDS closing observation must be finite, positive and denominated in USD.")
    run_dir=Path(run_dir);folder=run_dir/"market_data";folder.mkdir(parents=True,exist_ok=True)
    target=folder/"wrds_close.csv"
    pd.DataFrame([{"ticker":ticker,"gvkey":row["gvkey"],"iid":row["iid"],"trade_date":str(row["datadate"]),
                   "field":"prccd","close_usd":value}]).to_csv(target,index=False,lineterminator="\n")
    record={"status":"retrieved","provider":"WRDS","ticker":ticker,"trade_date":trade_date,
            "close_usd":value,"currency":"USD","dataset":"Compustat North America comp.secd",
            "instrument":{"gvkey":row["gvkey"],"iid":row["iid"]},"field":"prccd",
            "source":f"WRDS Compustat comp.secd.prccd; primary U.S. security; dated security ticker {ticker}; {trade_date}",
            "request":{"sql":QUERY,"parameters":[ticker,trade_date]},
            "retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"data_file":"market_data/wrds_close.csv",
            "sha256":hashlib.sha256(target.read_bytes()).hexdigest()}
    write_json(run_dir/"market_input.json",record)
    return verify_receipt(run_dir,ticker,trade_date,"wrds")
