from datetime import datetime
from src.data_loader import load_data
from src.strategies.buy_hold_strategy import BuyHoldStrategy
from src.strategies.ma_crossover_strategy import MACrossoverStrategy
from src.strategies.rsi_strategy import RSIStrategy
from src.performance_metrics import compute_metrics
from src.plotter import plot_equity_curve
from src.print_metrics import print_metrics
from analysis.grid_search import run_grid_search  # La funzione generica di grid search

def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Run base strategies (Buy & Hold, MA, RSI)")
        print("2. Run grid search on MA Crossover")
        print("3. Run grid search on RSI Strategy")
        print("4. Exit")
        choice = input("\nSelect an option (1/2/3/4): ")

        if choice == "1":
            ticker = input("Enter a stock ticker (e.g., AAPL, TSLA): ").strip()

            if not ticker:
                print("❌ Empty ticker. Please enter a valid ticker.")
                continue
            
            start_date = input("Enter start date (YYYY-MM-DD): ").strip()
            end_date = input("Enter end date (YYYY-MM-DD): ").strip()

            # Verifica se le date sono valide
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
                end_date = datetime.strptime(end_date, "%Y-%m-%d")
                if start_date >= end_date:
                    print("❌ Start date must be earlier than end date.")
                    continue
            except ValueError:
                print("❌ Invalid date format. Please enter the dates in 'YYYY-MM-DD' format.")
                continue

            # Carica i dati con le date selezionate
            df = load_data(ticker, start_date=start_date, end_date=end_date)

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

        elif choice == "2" or choice == "3":
            ticker = input("Enter a stock ticker (e.g., AAPL, TSLA): ").strip()

            if not ticker:
                print("❌ Empty ticker. Please enter a valid ticker.")
                continue
            
            start_date = input("Enter start date (YYYY-MM-DD): ").strip()
            end_date = input("Enter end date (YYYY-MM-DD): ").strip()

            # Verifica se le date sono valide
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
                end_date = datetime.strptime(end_date, "%Y-%m-%d")
                if start_date >= end_date:
                    print("❌ Start date must be earlier than end date.")
                    continue
            except ValueError:
                print("❌ Invalid date format. Please enter the dates in 'YYYY-MM-DD' format.")
                continue

            # Carica i dati con le date selezionate
            df = load_data(ticker, start_date=start_date, end_date=end_date)

            if choice == "2":
                param_combinations = [(10, 50), (20, 100), (50, 200)]  # Example for MA strategy
                run_grid_search(ticker, MACrossoverStrategy, param_combinations, "ma_crossover")

            elif choice == "3":
                param_combinations = [
                    (10, 20, 30), (14, 50, 60)  # Example for RSI strategy
                ]
                run_grid_search(ticker, RSIStrategy, param_combinations, "rsi_strategy")

        elif choice == "4":
            print("👋 Exiting the program.")
            break
        else:
            print("\n❌ Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
