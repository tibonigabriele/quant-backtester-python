from src.data_loader import load_data
from src.strategy_buy_hold import buy_and_hold
from src.strategy_ma_crossover import moving_average_crossover
from src.performance_metrics import compute_metrics
from src.plotter import plot_equity_curve

def main():
    # Load data
    df = load_data('SPY')

    # Implement strategies
    buy_hold_returns = buy_and_hold(df)
    ma_crossover_returns = moving_average_crossover(df)

    # Compute metrics
    bh_metrics = compute_metrics(buy_hold_returns)
    ma_metrics = compute_metrics(ma_crossover_returns)

    # Plot equity curve
    plot_equity_curve(buy_hold_returns, ma_crossover_returns)

    # Print results
    print("Buy & Hold Metrics:", bh_metrics)
    print("MA Crossover Metrics:", ma_metrics)

if __name__ == "__main__":
    main()
