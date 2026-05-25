def generate_recommendation(instances):

    recommendations = []

    for i in instances:

        if i["cpu_usage"] < 10:

            recommendations.append({
                "instance_id": i["instance_id"],
                "message": "Underutilized instance. Consider downsizing."
            })

    return recommendations