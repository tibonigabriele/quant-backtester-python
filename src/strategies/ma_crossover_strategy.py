import pandas as pd
import numpy as np
from src.strategies.strategy_base import Strategy

class MACrossoverStrategy(Strategy):
    def __init__(self, short_window=20, long_window=50):
        self.short_window = short_window
        self.long_window = long_window

    def backtest(self, df: pd.DataFrame) -> pd.Series:
        df = df.copy()
        df['short_ma'] = df['price'].rolling(window=self.short_window, min_periods=1).mean()
        df['long_ma'] = df['price'].rolling(window=self.long_window, min_periods=1).mean()
        
        df['signal'] = 0
        df.loc[df.index[self.short_window:], 'signal'] = (
            df['short_ma'][self.short_window:] > df['long_ma'][self.short_window:]
        ).astype(int)

        df['returns'] = df['price'].pct_change()
        df['strategy_returns'] = df['returns'] * df['signal']
        df['cumulative_returns'] = (1 + df['strategy_returns']).cumprod()

        return df['cumulative_returns']
