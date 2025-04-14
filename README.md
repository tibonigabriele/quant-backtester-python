# 📈 Quant Backtester

A lightweight, modular backtesting engine to simulate trading strategies on historical stock data and evaluate their performance.

---

## 🚀 Features

- Fetches historical stock data via Yahoo Finance
- Modular strategy architecture (easy to plug in new ones)
- Computes key performance metrics:
  - **CAGR**
  - **Sharpe Ratio**
  - **Maximum Drawdown**
- Visualizes equity curves with Matplotlib

---

## 📸 Demo

![Equity Curve](screenshots/equity_curve.png)

---

## ⚙️ How to Use

```bash
git clone https://github.com/tibonigabriele/quant-backtester-python.git
cd quant-backtester-python
pip install -r requirements.txt
python main.py
```

> Make sure you're connected to the internet: the script fetches data using `yfinance`.

---

## 💡 Included Strategies

- **Buy & Hold** – benchmark strategy
- **Moving Average Crossover** – buys when short-term MA crosses above long-term MA

You can add your own strategies by creating new modules in the `src/` folder and modifying `main.py`.

---

## 📊 Performance Metrics

| Metric           | Description                                                 |
| ---------------- | ----------------------------------------------------------- |
| **CAGR**         | Compound Annual Growth Rate                                 |
| **Sharpe Ratio** | Risk-adjusted return (using daily returns, annualized)      |
| **Max Drawdown** | Largest equity drop from peak to trough during the backtest |

---

## 📂 Project Structure

```
quant-backtester-python/
├── main.py                     # Main script to run a backtest
├── requirements.txt            # Python dependencies
├── LICENSE                     # MIT License
├── README.md                   # This file
├── equity_curve.png            # Plot output
├── screenshots/
│   └── equity_curve.png        # Same plot saved separately for README display
└── src/
    ├── data_loader.py          # Fetches data from Yahoo Finance
    ├── performance_metrics.py  # Calculates financial metrics
    ├── plotter.py              # Plots equity curves
    ├── print_metrics.py        # Prints metrics in terminal
    ├── strategy_buy_hold.py    # Buy and hold logic
    └── strategy_ma_crossover.py # MA crossover strategy logic
```

---

## 😨 Why this project?

This project was created as a personal exercise to:

- Explore quantitative finance and algorithmic strategy evaluation
- Build a flexible backtesting framework from scratch
- Learn and apply Python, Pandas, NumPy, and Matplotlib in a real-world use case

---

## 📬 Contact

Project by [Gabriele Tiboni](https://github.com/tibonigabriele)  
Feel free to reach out for feedback or collaboration!
