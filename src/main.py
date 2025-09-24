import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "xauusd.csv"
REPORT = ROOT / "report"
REPORT.mkdir(parents=True, exist_ok=True)

def find_col(cols, candidates):
    low = {c.lower(): c for c in cols}
    for cand in candidates:
        if cand in low:
            return low[cand]
    return None

def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        print(f"[!] Missing data: {path}")
        print("    Please place a CSV at data/xauusd.csv with columns like Date, Close.")
        sys.exit(1)
    df = pd.read_csv(path)
    # Identify date and close columns (case-insensitive)
    date_col = find_col(df.columns, ["date","datetime","time","timestamp"])
    close_col = find_col(df.columns, ["close","adj close","adj_close","closing price"])
    if date_col is None:
        raise ValueError("Could not find a date-like column (date/datetime/time/timestamp).")
    if close_col is None:
        raise ValueError("Could not find a close-like column (close/adj close).")
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df = df.dropna(subset=[date_col, close_col])
    df = df.sort_values(by=date_col).reset_index(drop=True)
    df = df.rename(columns={date_col: "Date", close_col: "Close"})
    return df[["Date","Close"]]

def plot_price(df: pd.DataFrame, outpath: Path):
    plt.figure()  # each chart in its own figure
    plt.plot(df["Date"], df["Close"])
    plt.title("XAUUSD Close Price")
    plt.xlabel("Date")
    plt.ylabel("Close")
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()
    print(f"[✓] Saved figure -> {outpath}")

if __name__ == "__main__":
    df = load_data(DATA)
    plot_price(df, REPORT / "price.png")
    print("[✓] Done. Next: implement a simple MA cross in src/signals.py.")
