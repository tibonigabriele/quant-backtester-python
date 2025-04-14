import pandas as pd
from src.strategies.strategy_base import Strategy

class BuyHoldStrategy(Strategy):
    def backtest(self, df: pd.DataFrame) -> pd.Series:
        df = df.copy()
        df['returns'] = df['price'].pct_change()
        df['cumulative_returns'] = (1 + df['returns']).cumprod()
        return df['cumulative_returns']
