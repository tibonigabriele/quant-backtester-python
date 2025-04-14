import matplotlib.pyplot as plt
import os

def plot_equity_curve(returns_dict):
    """
    Plots cumulative returns for multiple strategies.

    Parameters:
    - returns_dict (dict): Dictionary where keys are strategy names and values are pandas Series of cumulative returns.
    """
    plt.figure(figsize=(10, 5))
    
    for strategy_name, returns in returns_dict.items():
        plt.plot(returns, label=strategy_name)

    plt.title('Equity Curve')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    os.makedirs("plots", exist_ok=True)
    plt.savefig("plots/equity_curve.png")
    plt.show()
