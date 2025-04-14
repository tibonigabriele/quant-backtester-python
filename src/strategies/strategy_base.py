from abc import ABC, abstractmethod
import pandas as pd

class Strategy(ABC):
    @abstractmethod
    def backtest(self, df: pd.DataFrame) -> pd.Series:
        """
        Esegue il backtest della strategia su un DataFrame di dati storici.

        Parametri:
        - df (pd.DataFrame): DataFrame con almeno una colonna 'price'

        Ritorna:
        - pd.Series: Serie dei ritorni cumulati della strategia
        """
        pass
