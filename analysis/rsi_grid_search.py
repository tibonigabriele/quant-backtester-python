def run_rsi_grid_search():
    import os
    import pandas as pd
    from itertools import product
    from sklearn.preprocessing import MinMaxScaler

    from src.data_loader import load_data
    from src.strategies.rsi_strategy import RSIStrategy
    from src.performance_metrics import compute_metrics
    from src.print_metrics import print_metrics

    print("\U0001F4C5 Downloading data...")
    df = load_data("SPY")
    print("\u2705 Data successfully loaded.\n")

    rsi_windows = [10, 14, 21]
    lower_thresholds = [30, 35]
    upper_thresholds = [65, 70]

    results = []

    for window, lower, upper in product(rsi_windows, lower_thresholds, upper_thresholds):
        if lower >= upper:
            continue

        label = f"RSI {window} | {lower}-{upper}"
        strategy = RSIStrategy(rsi_window=window, lower_threshold=lower, upper_threshold=upper)
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
        print("\n\u26A0\uFE0F No results available.")
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
    results_df.to_csv("results/rsi_results.csv", index=False)

    print("\n\u2705 RSI analysis completed. Results saved to 'results/rsi_results.csv'")
