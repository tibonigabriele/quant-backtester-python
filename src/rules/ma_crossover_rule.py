# src/rules/ma_crossover_rule.py

import pandas as pd
import numpy as np
from .base_rule import Rule

class MACrossoverRule(Rule):
    def __init__(self, short_window=20, long_window=50):
        self.short_window = short_window
        self.long_window = long_window

    def evaluate(self, df: pd.DataFrame) -> pd.Series:
        short_ma = df['price'].rolling(window=self.short_window, min_periods=1).mean()
        long_ma = df['price'].rolling(window=self.long_window, min_periods=1).mean()
        signal = np.where(short_ma > long_ma, 1, 0)
        return pd.Series(signal, index=df.index)
