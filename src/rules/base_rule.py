# src/rules/base_rule.py

from abc import ABC, abstractmethod
import pandas as pd

class Rule(ABC):
    @abstractmethod
    def evaluate(self, df: pd.DataFrame) -> pd.Series:
        """
        Must return a binary Series (1 = enter long, 0 = stay out)        
        """
        pass
