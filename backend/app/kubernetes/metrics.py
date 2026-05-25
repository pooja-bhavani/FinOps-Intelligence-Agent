def get_kubernetes_metrics():
    return [
        {
            "pod_name": "payment-service",
            "namespace": "production",
            "cpu_usage": 3,
            "memory_usage": 120,
            "status": "Running"
        },
        {
            "pod_name": "cart-service",
            "namespace": "production",
            "cpu_usage": 65,
            "memory_usage": 450,
            "status": "Running"
        }
    ]