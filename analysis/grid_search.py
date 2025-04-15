def run_grid_search(ticker, strategy_class, param_combinations, file_prefix):
    import os
    import pandas as pd
    from itertools import product
    from sklearn.preprocessing import MinMaxScaler

    from src.data_loader import load_data
    from src.performance_metrics import compute_metrics
    from src.print_metrics import print_metrics

    print(f"📥 Downloading data for {ticker}...")
    df = load_data(ticker)
    if df.empty:
        print("❌ No data available. Aborting analysis.")
        return
    print("✅ Data successfully loaded.\n")

    results = []

    for params in param_combinations:
        strategy = strategy_class(*params)
        cumulative_returns = strategy.backtest(df)
        metrics = compute_metrics(cumulative_returns)

        if metrics is None:
            continue

        label = f"{strategy_class.__name__} {params}"
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
    results_df.to_csv(f"results/{file_prefix}_results_{ticker}.csv", index=False)

    print(f"\n✅ Analysis completed. Results saved to 'results/{file_prefix}_results_{ticker}.csv'")
