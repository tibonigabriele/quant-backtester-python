# analysis/ma_grid_search.py

def run_ma_grid_search():
    import os
    import pandas as pd
    from itertools import product
    from sklearn.preprocessing import MinMaxScaler

    from src.data_loader import load_data
    from src.strategies.ma_crossover_strategy import MACrossoverStrategy
    from src.performance_metrics import compute_metrics
    from src.print_metrics import print_metrics

    print("📥 Downloading data...")
    df = load_data("SPY")
    print("✅ Data successfully loaded.\n")

    short_windows = [10, 20, 50]
    long_windows = [50, 100, 200]

    results = []

    for short_w, long_w in product(short_windows, long_windows):
        if short_w >= long_w:
            continue  # Short MA must be shorter than long MA

        label = f"MA {short_w}-{long_w}"
        strategy = MACrossoverStrategy(short_window=short_w, long_window=long_w)
        cumulative_returns = strategy.backtest(df)
        metrics = compute_metrics(cumulative_returns)

        if metrics is None:
            continue

        print_metrics(label, metrics)
        print("----------------------------------------")

        results.append({
            "Strategy": label,
            "CAGR": metrics["Annualized Return"],
            "Sharpe Ratio": metrics["Sharpe Ratio"],
            "Max Drawdown": metrics["Max Drawdown"]
        })

    if not results:
        print("\n⚠️ No results available.")
        return

    os.makedirs("results", exist_ok=True)
    results_df = pd.DataFrame(results)

    scaler = MinMaxScaler()
    norm_values = scaler.fit_transform(results_df[["CAGR", "Sharpe Ratio", "Max Drawdown"]])
    norm_df = pd.DataFrame(norm_values, columns=["CAGR_norm", "Sharpe_norm", "Drawdown_norm"])
    results_df = pd.concat([results_df, norm_df], axis=1)

    results_df["Score"] = (
        0.4 * results_df["CAGR_norm"] +
        0.5 * results_df["Sharpe_norm"] -
        0.3 * results_df["Drawdown_norm"]
    )

    results_df.sort_values(by="Score", ascending=False, inplace=True)
    results_df.to_csv("results/ma_crossover_results.csv", index=False)

    print("\n✅ Analysis completed. Results saved to 'results/ma_crossover_results.csv'")
