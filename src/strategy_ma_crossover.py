import numpy as np

def moving_average_crossover(df):
    df = df.copy()
    short_window = 20
    long_window = 50
    df['short_ma'] = df['price'].rolling(window=short_window, min_periods=1).mean()
    df['long_ma'] = df['price'].rolling(window=long_window, min_periods=1).mean()
    df['signal'] = 0
    df.loc[short_window:, 'signal'] = np.where(df['short_ma'][short_window:] > df['long_ma'][short_window:], 1, 0)
    df['positions'] = df['signal'].diff()
    df['returns'] = df['price'].pct_change()
    df['strategy_returns'] = df['returns'] * df['signal']
    df['cumulative_returns'] = (1 + df['strategy_returns']).cumprod()
    return df['cumulative_returns']

