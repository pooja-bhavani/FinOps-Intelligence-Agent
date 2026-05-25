def get_ec2_instances():
    return [
        {
            "instance_id": "i-84738",
            "instance_type": "t3.medium",
            "cpu_usage": 4,
            "monthly_cost": 120,
            "state": "running"
        },
        {
            "instance_id": "i-29384",
            "instance_type": "m5.large",
            "cpu_usage": 75,
            "monthly_cost": 300,
            "state": "running"
        },
        {
            "instance_id": "i-92837",
            "instance_type": "t3.small",
            "cpu_usage": 2,
            "monthly_cost": 80,
            "state": "idle"
        }
    ]