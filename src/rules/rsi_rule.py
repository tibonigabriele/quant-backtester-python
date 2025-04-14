import pandas as pd
import numpy as np

class RSIRule:
    def __init__(self, lower_threshold=30, upper_threshold=70, window=14):
        self.lower_threshold = lower_threshold
        self.upper_threshold = upper_threshold
        self.window = window

    def compute_rsi(self, series):
        delta = series.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(window=self.window, min_periods=1).mean()
        avg_loss = loss.rolling(window=self.window, min_periods=1).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def evaluate(self, df):
        df = df.copy()
        df['rsi'] = self.compute_rsi(df['price'])

        signal = pd.Series(0, index=df.index)
        signal[df['rsi'] < self.lower_threshold] = 1
        signal[df['rsi'] > self.upper_threshold] = 0
        signal = signal.ffill().fillna(0)

        return signal
