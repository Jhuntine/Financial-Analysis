"""Retrieve a dated closing price from LSEG or WRDS, with an offline receipt.

Credentials stay in memory. The receipt contains only the market observation,
its request parameters, source field, retrieval time and a data-file hash.
"""
from datetime import date, datetime, timezone
import contextlib
import hashlib
import io
import json
import math
import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
WRDS_QUERY = """SELECT c.gvkey, c.conm, c.tic, d.iid, d.datadate, d.prccd, d.curcdd
FROM comp.secd AS d
JOIN comp.company AS c ON c.gvkey = d.gvkey
WHERE c.tic = %s AND d.iid = c.priusa AND d.datadate = %s
ORDER BY d.gvkey, d.iid
LIMIT 2"""


def _redacted_error(error):
    message = str(error)
    for name in ["LSEG_APP_KEY", "WRDS_USERNAME", "WRDS_PASSWORD", "API_KEY", "OPENAI_API_KEY"]:
        value = os.getenv(name)
        if value:
            message = message.replace(value, "[REDACTED]")
    return message[:600]


def _lseg_close(ticker, trade_date, ric):
    import lseg.data as ld
    if not os.getenv("LSEG_APP_KEY"):
        raise RuntimeError("LSEG_APP_KEY is missing from .env.")
    if not ric:
        raise ValueError("LSEG requires an explicit --ric for the listed share class.")
    # Suppress SDK diagnostics that can contain authentication/session details.
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        session = None
        try:
            session = ld.open_session(name="desktop.workspace", app_key=os.environ["LSEG_APP_KEY"])
            frame = ld.get_history(universe=ric, fields=["TRDPRC_1"], interval="1D",
                                   start=trade_date, end=trade_date, adjustments="unadjusted")
        except Exception as error:
            raise RuntimeError("LSEG retrieval failed: " + _redacted_error(error)) from None
        finally:
            if session is not None:
                ld.close_session()
    if frame is None or frame.empty or len(frame.columns) != 1:
        raise ValueError("LSEG did not return one unambiguous closing-price field.")
    rows = frame.loc[pd.to_datetime(frame.index).date == date.fromisoformat(trade_date)]
    if len(rows) != 1:
        raise ValueError("LSEG did not return exactly the requested trade date.")
    value = float(rows.iloc[0, 0])
    data = pd.DataFrame([{"ticker": ticker, "ric": ric, "trade_date": trade_date,
                          "field": "TRDPRC_1", "close_usd": value}])
    return data, {"provider": "LSEG", "dataset": "Historical Pricing, daily",
                  "instrument": ric, "field": "TRDPRC_1", "adjustments": "unadjusted",
                  "request": {"universe": ric, "fields": ["TRDPRC_1"], "interval": "1D",
                              "start": trade_date, "end": trade_date, "adjustments": "unadjusted"},
                  "source": f"LSEG Historical Pricing; {ric}; TRDPRC_1; daily close; {trade_date}; unadjusted",
                  "documentation": "https://developers.lseg.com/en/api-catalog/lseg-data-platform/lseg-data-library-for-python/tutorials/access-tutorials/tutorial-4-get_history"}


def _wrds_close(ticker, trade_date):
    import psycopg2
    if not os.getenv("WRDS_USERNAME") or not os.getenv("WRDS_PASSWORD"):
        raise RuntimeError("WRDS_USERNAME and WRDS_PASSWORD are required in .env.")
    try:
        connection = psycopg2.connect(host="wrds-pgdata.wharton.upenn.edu", port=9737,
            dbname="wrds", user=os.environ["WRDS_USERNAME"], password=os.environ["WRDS_PASSWORD"],
            sslmode="require", connect_timeout=15, options="-c statement_timeout=45000")
        try:
            connection.set_session(readonly=True)
            with connection.cursor() as cursor:
                cursor.execute(WRDS_QUERY, (ticker, trade_date))
                result = cursor.fetchall()
                columns = [item.name for item in cursor.description]
        finally:
            connection.close()
    except Exception as error:
        raise RuntimeError("WRDS retrieval failed: " + _redacted_error(error)) from None
    if len(result) != 1:
        raise ValueError("WRDS did not return one primary U.S. share-class observation on the requested date.")
    row = dict(zip(columns, result[0]))
    if row["curcdd"] != "USD":
        raise ValueError("The WRDS observation is not quoted in USD.")
    value = float(row["prccd"])
    data = pd.DataFrame([{"ticker": ticker, "gvkey": row["gvkey"], "iid": row["iid"],
                          "trade_date": str(row["datadate"]), "field": "prccd", "close_usd": value}])
    return data, {"provider": "WRDS", "dataset": "Compustat North America, comp.secd",
                  "instrument": {"gvkey": row["gvkey"], "iid": row["iid"]}, "field": "prccd",
                  "source": f"WRDS Compustat North America; comp.secd.prccd; primary U.S. issue; {trade_date}",
                  "request": {"sql": WRDS_QUERY, "parameters": [ticker, trade_date]},
                  "documentation": "https://github.com/wharton/wrds"}


def verify_receipt(run_dir, ticker, trade_date, provider=None):
    run_dir = Path(run_dir)
    record = json.loads((run_dir / "market_input.json").read_text(encoding="utf-8"))
    if record.get("status") != "retrieved" or record.get("provider") not in {"LSEG", "WRDS"}:
        raise ValueError("No verified LSEG/WRDS price receipt. Fetch a price with --market-provider first.")
    if (record["ticker"], record["trade_date"]) != (ticker, trade_date):
        raise ValueError("Recorded price belongs to a different ticker or trade date.")
    if provider and record["provider"].lower() != provider.lower():
        raise ValueError("Recorded price provider differs from the requested provider.")
    source_path = (run_dir / record["data_file"]).resolve()
    if not source_path.is_relative_to(run_dir.resolve()):
        raise ValueError("Market-data receipt points outside this run.")
    data = source_path.read_bytes()
    if hashlib.sha256(data).hexdigest() != record["sha256"]:
        raise ValueError("Market observation failed its SHA-256 check.")
    frame = pd.read_csv(io.BytesIO(data))
    if len(frame) != 1 or str(frame.iloc[0]["trade_date"]) != trade_date or str(frame.iloc[0]["ticker"]) != ticker:
        raise ValueError("Market observation does not match the recorded ticker/date.")
    if not math.isclose(float(frame.iloc[0]["close_usd"]), record["close_usd"], rel_tol=0, abs_tol=1e-9):
        raise ValueError("Market observation's value differs from its receipt.")
    return record


def get_market_close(ticker, trade_date, run_dir, provider="lseg", ric=None, offline=False):
    load_dotenv(ROOT / ".env", override=False)
    date.fromisoformat(trade_date)
    if offline:
        record = verify_receipt(run_dir, ticker, trade_date, provider)
        if provider == "lseg" and ric and record["instrument"] != ric:
            raise ValueError("Recorded LSEG instrument differs from the requested RIC.")
        return record
    if provider == "lseg":
        frame, record = _lseg_close(ticker, trade_date, ric)
    elif provider == "wrds":
        frame, record = _wrds_close(ticker, trade_date)
    else:
        raise ValueError("Choose lseg or wrds; no public-price fallback is used.")
    value = float(frame.iloc[0]["close_usd"])
    if not math.isfinite(value) or value <= 0:
        raise ValueError("Provider price must be finite and positive.")
    run_dir = Path(run_dir)
    folder = run_dir / "market_data"
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / (provider + "_close.csv")
    frame.to_csv(path, index=False, lineterminator="\n")
    record.update({"status": "retrieved", "ticker": ticker, "trade_date": trade_date,
                   "close_usd": value, "currency": "USD", "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
                   "data_file": path.relative_to(run_dir).as_posix(),
                   "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    (run_dir / "market_input.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
    return verify_receipt(run_dir, ticker, trade_date, provider)
