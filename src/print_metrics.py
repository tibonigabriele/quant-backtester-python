def print_metrics(name, metrics):
    print(f"\n{name} Performance Metrics:")
    for key, value in metrics.items():
        print(f"- {key}: {value:.4f}")
