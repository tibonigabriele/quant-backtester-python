def buy_and_hold(df):
    df['returns'] = df['price'].pct_change()
    df['cumulative_returns'] = (1 + df['returns']).cumprod()
    return df['cumulative_returns']
