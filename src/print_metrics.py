def print_metrics(strategy_name, metrics):
    print(f"\n{strategy_name} Performance Metrics:")
    for key, value in metrics.items():
        # Converti il valore a float prima di formattarlo
        try:
            value = float(value)
            print(f"- {key}: {value:.4f}")
        except ValueError:
            print(f"- {key}: {value}")  # Se il valore non può essere convertito in float, stampalo come stringa
