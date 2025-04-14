import matplotlib.pyplot as plt
import os

def plot_equity_curve(bh_returns, ma_returns, rsi_returns):
    plt.figure(figsize=(10, 5))
    plt.plot(bh_returns, label='Buy & Hold')
    plt.plot(ma_returns, label='MA Crossover')
    plt.plot(rsi_returns, label='RSI Strategy')
    plt.title('Equity Curve')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    os.makedirs("plots", exist_ok=True)
    plt.savefig("plots/equity_curve.png")
    plt.show()
