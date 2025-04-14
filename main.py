from src.data_loader import load_data
from src.strategy_buy_hold import buy_and_hold
from src.strategy_ma_crossover import moving_average_crossover
from src.strategy_rsi import rsi_strategy
from src.performance_metrics import compute_metrics
from src.plotter import plot_equity_curve
from src.print_metrics import print_metrics

def main():
    # Load data
    df = load_data('SPY')

    # Implement strategies
    strategies = {
        "Buy & Hold": buy_and_hold(df),
        "MA Crossover": moving_average_crossover(df),
        "RSI Strategy": rsi_strategy(df)
    }

    # Compute metrics and print
    for name, returns in strategies.items():
        metrics = compute_metrics(returns)
        print_metrics(name, metrics)

    # Plot all strategies
    plot_equity_curve(strategies)

if __name__ == "__main__":
    main()

