import pandas as pd
import yfinance as yf

def load_data(ticker):
    data = yf.download(ticker, start="2010-01-01", end="today")
    data = data[['Adj Close']]
    data.columns = ['price']
    return data
