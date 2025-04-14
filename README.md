# 📈 Quant Backtester

A modular backtesting engine to simulate and compare trading strategies on historical stock data.

---

## 🚀 Features

- Fetches historical data using **Yahoo Finance**
- Strategy-based architecture with plug-and-play logic
- Computes financial performance metrics:
  - **CAGR**
  - **Sharpe Ratio**
  - **Max Drawdown**
- Plot equity curves with Matplotlib
- Easily test rule-based strategies with custom logic

---

## 📸 Demo

![Equity Curve](plots/equity_curve.png)

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

- **Buy & Hold** – Baseline benchmark
- **Moving Average Crossover** – Entry when short MA > long MA
- **RSI Strategy** – Entry/exit based on RSI thresholds

---

## 📊 Performance Metrics

| Metric           | Description                                                 |
| ---------------- | ----------------------------------------------------------- |
| **CAGR**         | Compound Annual Growth Rate                                 |
| **Sharpe Ratio** | Risk-adjusted return (annualized)                          |
| **Max Drawdown** | Largest drop from peak equity to trough during backtest    |

---

## 📂 Project Structure

```
quant-backtester-python/
├── main.py                     # Main script to run the backtest
├── requirements.txt            # Dependencies
├── LICENSE                     # License file
├── README.md                   # Project info
├── plots/
│   └── equity_curve.png        # Sample equity curve output
├── analysis/
│   └── test_ma_grid_search.py # Strategy parameter testing
└── src/
    ├── data_loader.py          # Loads financial data
    ├── performance_metrics.py  # Calculates metrics
    ├── plotter.py              # Plots returns
    ├── print_metrics.py        # Pretty-prints metrics
    ├── rules/                  # Modular strategy rules
    │   ├── base_rule.py
    │   ├── ma_crossover_rule.py
    │   └── rsi_rule.py
    └── strategies/            # Complete strategy implementations
        ├── buy_hold_strategy.py
        ├── ma_crossover_strategy.py
        ├── rsi_strategy.py
        ├── rule_based_strategy.py
        └── strategy_base.py
```

---

## 🧐 Why this project?

To:
- Explore quantitative trading with Python
- Build a reusable backtesting framework
- Learn by doing: Pandas, NumPy, Matplotlib, strategy logic

---

## 📬 Contact

Created by [Gabriele Tiboni](https://github.com/tibonigabriele)

Feel free to leave feedback, star the repo, or reach out for collaboration.

