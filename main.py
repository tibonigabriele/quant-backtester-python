from src.data_loader import load_data
from src.strategies.buy_hold_strategy import BuyHoldStrategy
from src.strategies.ma_crossover_strategy import MACrossoverStrategy
from src.strategies.rsi_strategy import RSIStrategy
from src.performance_metrics import compute_metrics
from src.plotter import plot_equity_curve
from src.print_metrics import print_metrics

def main():
    while True:
        print("\nCosa vuoi fare?")
        print("1. Eseguire le strategie base (Buy & Hold, MA, RSI)")
        print("2. Lanciare la grid search su MA Crossover")
        print("3. Esci")
        choice = input("\nScegli un'opzione (1/2/3): ")

        if choice == "1":
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

        elif choice == "2":
            from analysis.ma_grid_search import run_ma_grid_search
            run_ma_grid_search()

        elif choice == "3":
            print("👋 Uscita dal programma.")
            break
        else:
            print("\n❌ Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()
