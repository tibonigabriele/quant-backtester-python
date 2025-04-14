from src.data_loader import load_data
from src.strategies.buy_hold_strategy import BuyHoldStrategy
from src.strategies.ma_crossover_strategy import MACrossoverStrategy
from src.strategies.rsi_strategy import RSIStrategy
from src.performance_metrics import compute_metrics
from src.plotter import plot_equity_curve
from src.print_metrics import print_metrics

def main():
    df = load_data("SPY")

    strategies = {
        "Buy & Hold": BuyHoldStrategy(),
        "MA Crossover": MACrossoverStrategy(short_window=20, long_window=50),
        "RSI Strategy": RSIStrategy()
    }

    all_returns = {}
    all_metrics = {}

    for name, strategy in strategies.items():
        cumulative_returns = strategy.backtest(df)
        metrics = compute_metrics(cumulative_returns)

        all_returns[name] = cumulative_returns
        all_metrics[name] = metrics

        print_metrics(name, metrics)

    plot_equity_curve(all_returns)

if __name__ == "__main__":
    main()
