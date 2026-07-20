def get_outdoor_recommendation(weather, air_quality):

    score = 0
    positive = []
    negative = []

    temperature = weather["temperature"]
    feels_like = weather["feels_like"]
    wind = weather["wind"]
    aqi = air_quality["aqi"]


    # Temperature
    if 55 <= feels_like <= 75:
        score += 2
        positive.append("Comfortable temperature")

    elif 75 < feels_like <= 85:
        score += 1
        positive.append("Warm but manageable")

    elif feels_like > 85:
        score -= 2
        negative.append("High heat")

    elif feels_like < 40:
        score -= 2
        negative.append("Cold conditions")


    # Wind
    if wind <= 10:
        score += 1
        positive.append("Low wind")

    elif wind > 20:
        score -= 1
        negative.append("High wind")


    # Air quality
    if aqi <= 50:
        score += 2
        positive.append("Good air quality")

    elif aqi <= 100:
        score += 1
        positive.append("Acceptable air quality")

    elif aqi > 100:
        score -= 2
        negative.append("Poor air quality")


    # Final recommendation
    if score >= 4:
        recommendation = "Excellent conditions"

    elif score >= 2:
        recommendation = "Good conditions"

    elif score >= 0:
        recommendation = "Okay conditions"

    else:
        recommendation = "Poor conditions"


    return {
        "recommendation": recommendation,
        "score": score,
        "positive": positive,
        "negative": negative
    }