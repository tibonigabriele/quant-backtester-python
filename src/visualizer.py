import pandas as pd
import os

def show_ma_grid_results(filepath="results/ma_crossover_results.csv", top_n=5):
    if not os.path.exists(filepath):
        print(f"\n❌ Il file {filepath} non esiste.")
        return

    df = pd.read_csv(filepath)
    if df.empty:
        print("\n⚠️ Il file è vuoto.")
        return

    print(f"\n📊 Top {top_n} strategie MA Crossover (ordinate per Score):\n")
    top_df = df.sort_values(by="Score", ascending=False).head(top_n)
    print(top_df[["Strategy", "CAGR", "Sharpe Ratio", "Max Drawdown", "Score"]].to_string(index=False))
