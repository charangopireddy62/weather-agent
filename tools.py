def get_weather(latitude: float, longitude: float) -> dict:
    """
    Mock weather tool.
    Validates coordinates and returns fixed weather data.
    """

    # Validate latitude
    if not isinstance(latitude, (int, float)):
        raise ValueError("Latitude must be a number.")
    if latitude < -90 or latitude > 90:
        raise ValueError("Latitude must be between -90 and 90.")

    # Validate longitude
    if not isinstance(longitude, (int, float)):
        raise ValueError("Longitude must be a number.")
    if longitude < -180 or longitude > 180:
        raise ValueError("Longitude must be between -180 and 180.")

    # Mock response (API comes later)
    return {
        "latitude": round(latitude, 4),
        "longitude": round(longitude, 4),
        "temperature_c": 31,
        "condition": "Partly cloudy",
        "humidity": 62
    }
