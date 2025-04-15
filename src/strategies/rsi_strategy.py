import pandas as pd
import numpy as np
from src.strategies.strategy_base import Strategy

class RSIStrategy(Strategy):
    def __init__(self, window=14, lower=30, upper=70):
        self.window = window
        self.lower = lower
        self.upper = upper

    def compute_rsi(self, series: pd.Series) -> pd.Series:
        delta = series.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(window=self.window, min_periods=1).mean()
        avg_loss = loss.rolling(window=self.window, min_periods=1).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def backtest(self, df: pd.DataFrame) -> pd.Series:
        df = df.copy()
        df['rsi'] = self.compute_rsi(df['price'])

        df['signal'] = 0
        df.loc[df['rsi'] < self.lower, 'signal'] = 1
        df.loc[df['rsi'] > self.upper, 'signal'] = 0
        df['signal'] = df['signal'].ffill().fillna(0)

        df['returns'] = df['price'].pct_change()
        df['strategy_returns'] = df['returns'] * df['signal']
        df['cumulative_returns'] = (1 + df['strategy_returns']).cumprod()

        return df['cumulative_returns']
