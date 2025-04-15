import numpy as np

def compute_metrics(returns):
    if returns.empty:
        print("No data to compute metrics.")
        return None
    total_return = returns.iloc[-1] - 1
    num_years = len(returns) / 252  # assuming daily data
    annualized_return = (returns.iloc[-1]) ** (1 / num_years) - 1
    max_drawdown = ((returns.cummax() - returns) / returns.cummax()).max()
    daily_returns = returns.pct_change().dropna()
    
    # Add a check to prevent division by zero for Sharpe Ratio
    daily_returns_std = daily_returns.std()
    if daily_returns_std == 0:
        sharpe_ratio = np.nan  # Set Sharpe Ratio to NaN if std is zero
    else:
        sharpe_ratio = (daily_returns.mean() / daily_returns_std) * (252 ** 0.5)
    
    return {
        'Total Return': round(total_return, 4),
        'Annualized Return': round(annualized_return, 4),
        'Max Drawdown': round(max_drawdown, 4),
        'Sharpe Ratio': round(sharpe_ratio, 2) if not np.isnan(sharpe_ratio) else "N/A"
    }
