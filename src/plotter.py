import matplotlib.pyplot as plt

def plot_equity_curve(bh_returns, ma_returns):
    plt.figure(figsize=(10, 5))
    plt.plot(bh_returns, label='Buy & Hold')
    plt.plot(ma_returns, label='MA Crossover')
    plt.title('Equity Curve')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("equity_curve.png")
    plt.show()

