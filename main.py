from src.data_loader import load_data
from src.strategies.buy_hold_strategy import BuyHoldStrategy
from src.strategies.ma_crossover_strategy import MACrossoverStrategy
from src.strategies.rsi_strategy import RSIStrategy
from src.performance_metrics import compute_metrics
from src.plotter import plot_equity_curve
from src.print_metrics import print_metrics

def main():
    # Load data
    df = load_data('SPY')

    # Initialize strategies
    strategies = {
        "Buy & Hold": BuyHoldStrategy(),
        "MA Crossover": MACrossoverStrategy(short_window=20, long_window=50),
        "RSI Strategy": RSIStrategy(rsi_window=14, lower_threshold=30, upper_threshold=70)
    }

    # Run backtests
    strategies_returns = {
        name: strategy.backtest(df)
        for name, strategy in strategies.items()
    }

    # Compute and print metrics
    for name, returns in strategies_returns.items():
        metrics = compute_metrics(returns)
        print_metrics(name, metrics)

    # Plot results
    plot_equity_curve(strategies_returns)

if __name__ == "__main__":
    main()
