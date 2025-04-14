import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Per importazioni da src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Carica i risultati
results_path = "results/ma_crossover_results.csv"
results = pd.read_csv(results_path)

# Estrai short e long window dai nomi delle strategie
results[['Short_MA', 'Long_MA']] = results['Strategy'].str.extract(r'MA (\d+)-(\d+)').astype(int)

# Pivot per heatmap dello score
pivot_score = results.pivot(index='Long_MA', columns='Short_MA', values='Score')

plt.figure(figsize=(8, 6))
sns.heatmap(pivot_score, annot=True, cmap='YlGnBu', fmt=".2f")
plt.title("MA Crossover Grid Search - Normalized Score")
plt.xlabel("Short MA Window")
plt.ylabel("Long MA Window")
os.makedirs("plots", exist_ok=True)
plt.savefig("plots/ma_grid_heatmap.png")
plt.show()

# Barplot per Sharpe Ratio
sorted_results = results.sort_values(by="Sharpe Ratio", ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(data=sorted_results, x="Sharpe Ratio", y="Strategy", palette="viridis")
plt.title("MA Crossover Strategies - Sharpe Ratio")
plt.xlabel("Sharpe Ratio")
plt.ylabel("Strategy")
plt.tight_layout()
plt.savefig("plots/ma_grid_sharpe_barplot.png")
plt.show()
