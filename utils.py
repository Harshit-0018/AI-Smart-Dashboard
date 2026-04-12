def generate_insights(data):
    trend = "increasing" if data.iloc[-1] > data.iloc[0] else "decreasing"

    insights = f"""
    - Overall trend is {trend}
    - Latest value: {data.iloc[-1]}
    - Average value: {data.mean():.2f}
    """

    return insights