import pandas as pd
import yfinance as yf

def load_data(ticker):
    data = yf.download(ticker, start="2010-01-01")
    # Select ‘Close’ and rename it ‘price’.
    if ('Close', ticker) in data.columns:
        data = data[('Close', ticker)]
    else:
        raise ValueError(f"The ‘Close’ column for {ticker} is not present in the downloaded data")
    
    data = pd.DataFrame(data)
    data.columns = ['price']
    return data
