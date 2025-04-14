from abc import ABC, abstractmethod
import pandas as pd

class Strategy(ABC):
    @abstractmethod
    def backtest(self, df: pd.DataFrame) -> pd.Series:
        """
        Executes the backtest of the strategy on a DataFrame of historical data.

        Parameters:
        - df (pd.DataFrame): DataFrame containing at least a 'price' column

        Returns:
        - pd.Series: Series of the strategy's cumulative returns
        """
        pass
