import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

# Path per importare moduli da src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Carica i risultati
results_path = os.path.join("results", "ma_crossover_results.csv")
df = pd.read_csv(results_path)

# Crea scatter plot con colore in base al CAGR
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    df["Max Drawdown"],
    df["Sharpe Ratio"],
    c=df["CAGR"],
    cmap="viridis",
    s=100,
    edgecolors='k'
)

# Aggiunge etichette
for _, row in df.iterrows():
    plt.text(row["Max Drawdown"], row["Sharpe Ratio"], row["Strategy"], fontsize=8, ha='right')

# Aggiunge colorbar per CAGR
cbar = plt.colorbar(scatter)
cbar.set_label("CAGR", rotation=270, labelpad=15)

# Titoli e assi
plt.title("MA Crossover Strategies")
plt.xlabel("Max Drawdown")
plt.ylabel("Sharpe Ratio")
plt.grid(True)
plt.tight_layout()

# Salva
os.makedirs("plots", exist_ok=True)
plt.savefig("plots/ma_grid_search_advanced.png")
plt.show()
