import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_loader import load_data
from src.rules.ma_crossover_rule import MACrossoverRule
from src.strategies.rule_based_strategy import RuleBasedStrategy
from src.performance_metrics import compute_metrics
from src.plotter import plot_equity_curve
from src.print_metrics import print_metrics

# ... resto del codice

# Carica i dati una sola volta
df = load_data("SPY")

# Definisci le combinazioni di finestre da testare
param_combinations = [(10, 50), (20, 50), (20, 100), (50, 200)]

# Per salvare tutti i risultati
all_metrics = {}
all_returns = {}

for short_w, long_w in param_combinations:
    rule = MACrossoverRule(short_w, long_w)
    strategy = RuleBasedStrategy([rule])
    cum_returns = strategy.backtest(df)
    metrics = compute_metrics(cum_returns)

    label = f"MA {short_w}-{long_w}"
    all_metrics[label] = metrics
    all_returns[label] = cum_returns

# Ordina le strategie per Sharpe Ratio (decrescente)
sorted_strategies = sorted(
    all_metrics.items(),
    key=lambda x: x[1]["Sharpe Ratio"],
    reverse=True
)

# Stampa risultati ordinati
for label, metrics in sorted_strategies:
    print_metrics(label, metrics)

# Evidenzia la strategia migliore
best_label, best_metrics = sorted_strategies[0]
print("\n🏆 MIGLIOR STRATEGIA (Sharpe Ratio più alto):")
print_metrics(best_label, best_metrics)

# Plot comparativo delle equity curve
plot_equity_curve(all_returns)
