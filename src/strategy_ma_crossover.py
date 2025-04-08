import numpy as np

def moving_average_crossover(df):
    df = df.copy()
    short_window = 20
    long_window = 50
    df['short_ma'] = df['price'].rolling(window=short_window, min_periods=1).mean()
    df['long_ma'] = df['price'].rolling(window=long_window, min_periods=1).mean()
    df['signal'] = 0

    # Calcola i segnali dove entrambe le medie mobili sono disponibili
    valid_idx = df.index[short_window:]  # Indici validi dove entrambe le medie sono calcolate
    signals = np.where(df.loc[valid_idx, 'short_ma'] > df.loc[valid_idx, 'long_ma'], 1, 0)
    df.loc[valid_idx, 'signal'] = signals

    df['positions'] = df['signal'].diff()
    df['returns'] = df['price'].pct_change()
    df['strategy_returns'] = df['returns'] * df['signal']
    df['cumulative_returns'] = (1 + df['strategy_returns']).cumprod()
    return df['cumulative_returns']
