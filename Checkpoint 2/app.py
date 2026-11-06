"""Local checkpoint 2 interface; all new runs include live semantic verification."""
from datetime import date
from pathlib import Path
import pandas as pd
import streamlit as st
from team import BASE, previous_config, read_json, run_team

st.set_page_config(page_title="Equity research agent team",layout="wide")
st.title("Equity research agent team")
st.caption("Filing tools ? Research ? Finance ? Advisor ? Manager ? Verifier")
pointer=BASE/"costco_data_pointer.json"
if pointer.exists():
    source=BASE/read_json(pointer)["run_dir"]
    saved=read_json(source/"configuration.json")
else:
    saved=previous_config();source=Path(saved["source_run"])
with st.form("run_team"):
    ticker=st.text_input("Company ticker",value=saved["ticker"])
    peers=st.text_input("Optional peers, separated by commas",value=",".join(saved["peers"]))
    evidence=st.selectbox("Filing evidence",["New SEC retrieval","Saved baseline snapshot"])
    cutoff=st.date_input("Information cutoff",value=date.fromisoformat(saved["as_of"]))
    pricing=st.selectbox("Closing price",["WRDS historical close","User-supplied close","Omit price"])
    price_date=st.date_input("Close date",value=date.fromisoformat(saved["price_date"]))
    price=st.number_input("User-supplied close (USD)",min_value=0.01,value=float(saved["price"]),step=0.01)
    price_source=st.text_input("Source for a user-supplied close",value="User-supplied closing price; independently check the observation")
    provider=st.selectbox("Model provider",["Purdue GenAI Studio","OpenAI"])
    submitted=st.form_submit_button("Run research team",type="primary")
if submitted:
    config={"ticker":ticker.strip().upper(),"peers":[p.strip().upper() for p in peers.split(",") if p.strip()],
            "as_of":cutoff.isoformat(),"offline":evidence.startswith("Saved"),"source_run":str(source) if evidence.startswith("Saved") else None,
            "market_provider":"wrds" if pricing.startswith("WRDS") else None,"ric":None,
            "price_date":None if pricing=="Omit price" else price_date.isoformat(),
            "model_provider":"purdue" if provider.startswith("Purdue") else "openai"}
    if pricing.startswith("User"):
        config.update(price=price,price_source=price_source)
    try:
        with st.status("Running research team",expanded=True) as status:
            result=run_team(config,on_node=lambda name:status.write(name))
            if result["manager_approved"]:
                status.update(label="Report compiled and verified",state="complete")
            else:
                status.update(label="Manager review needs revision",state="error")
        st.session_state["last_run"]=result["run_dir"]
    except Exception as exc:
        st.error(f"Run incomplete ({type(exc).__name__}). Check local credentials, input dates and saved-snapshot settings. No successful report is claimed.")
if "last_run" in st.session_state:
    folder=Path(st.session_state["last_run"])
    summary=read_json(folder/"summary.json")
    verification=read_json(folder/"verification.json")
    st.write("Saved run:",folder.name)
    st.write("Semantic verification:",verification["semantic_status"])
    if not summary["manager_approved"] or verification.get("unresolved_errors",0):
        st.warning("This run contains unresolved review findings. Read the saved findings before using the report.")
    st.dataframe(pd.DataFrame(verification["marks"])[["id","mark","reported","corrected","reason"]],hide_index=True)
    report=(folder/"verified_report_readable.md").read_text(encoding="utf-8")
    st.markdown(report)
    st.download_button("Download verified report",report,file_name="verified_report.md",mime="text/markdown")
