def compute_metrics(returns):
    if returns.empty:
        print("No data to compute metrics.")
        return None
    total_return = returns.iloc[-1] - 1
    num_years = len(returns) / 252  # assuming daily data
    annualized_return = (returns.iloc[-1]) ** (1 / num_years) - 1
    max_drawdown = ((returns.cummax() - returns) / returns.cummax()).max()
    daily_returns = returns.pct_change().dropna()
    sharpe_ratio = (daily_returns.mean() / daily_returns.std()) * (252 ** 0.5)
    
    return {
        'Total Return': round(total_return, 4),
        'Annualized Return': round(annualized_return, 4),
        'Max Drawdown': round(max_drawdown, 4),
        'Sharpe Ratio': round(sharpe_ratio, 2)
    }
