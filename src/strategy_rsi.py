import pandas as pd
import numpy as np

def compute_rsi(series, window=14):
    delta = series.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def rsi_strategy(df, rsi_window=14, lower_threshold=30, upper_threshold=70):
    df = df.copy()
    df['rsi'] = compute_rsi(df['price'], window=rsi_window)

    df['signal'] = 0
    df.loc[df['rsi'] < lower_threshold, 'signal'] = 1
    df.loc[df['rsi'] > upper_threshold, 'signal'] = 0
    df['signal'] = df['signal'].ffill().fillna(0)

    df['returns'] = df['price'].pct_change()
    df['strategy_returns'] = df['returns'] * df['signal']
    df['cumulative_returns'] = (1 + df['strategy_returns']).cumprod()

    return df['cumulative_returns']
