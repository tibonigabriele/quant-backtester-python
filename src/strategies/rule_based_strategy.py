# src/strategies/rule_based_strategy.py

import pandas as pd

class RuleBasedStrategy:
    def __init__(self, rules):
        self.rules = rules  # list of Rule objects

    def generate_signals(self, df: pd.DataFrame) -> pd.Series:
        if not self.rules:
            raise ValueError("No rules provided")

        signals = pd.Series(1, index=df.index)  # let's start with all 'buy'
        for rule in self.rules:
            rule_signal = rule.evaluate(df)
            signals = signals & rule_signal  # logical and between rules

        return signals.astype(int)

    def backtest(self, df: pd.DataFrame) -> pd.Series:
        signals = self.generate_signals(df)
        df = df.copy()
        df['returns'] = df['price'].pct_change()
        df['strategy_returns'] = df['returns'] * signals
        df['cumulative_returns'] = (1 + df['strategy_returns']).cumprod()
        return df['cumulative_returns']
