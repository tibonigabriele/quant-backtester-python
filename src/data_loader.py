import pandas as pd
import yfinance as yf

def load_data(ticker, start_date, end_date):
    # Download historical data for the specified ticker and selected period
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Select the 'Close' column and rename it to 'price'
    if 'Close' in data.columns:
        data = data['Close']  # Use the 'Close' column
    else:
        raise ValueError(f"The ‘Close’ column for {ticker} is not present in the downloaded data")
    
    # Convert the data into a DataFrame and rename the column
    data = pd.DataFrame(data)
    data.columns = ['price']
    
    return data
