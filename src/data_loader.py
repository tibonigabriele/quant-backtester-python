import pandas as pd
import yfinance as yf

def load_data(ticker):
    data = yf.download(ticker, start="2010-01-01")
    # Selezioniamo 'Close' e rinominiamola 'price'
    if ('Close', ticker) in data.columns:
        data = data[('Close', ticker)]
    else:
        raise ValueError(f"La colonna 'Close' per {ticker} non è presente nei dati scaricati")
    
    data = pd.DataFrame(data)
    data.columns = ['price']
    return data
