def display_agriculture_problems(temperature, humidity, soil_moisture, crop_type):
    """
    Display potential agriculture problems based on environmental factors.

    Parameters:
    - temperature: Temperature in Celsius
    - humidity: Humidity percentage
    - soil_moisture: Soil moisture percentage
    - crop_type: Type of crop being cultivated

    Returns:
    None (Prints recommendations)
    """
    print("Analyzing agriculture conditions...")
    
    # Check temperature range
    if temperature < 10 or temperature > 35:
        print("Warning: Temperature is outside the optimal range for most crops.")

    # Check humidity levels
    if humidity < 40 or humidity > 80:
        print("Warning: Humidity levels may not be suitable for the chosen crop.")

    # Check soil moisture
    if soil_moisture < 20 or soil_moisture > 80:
        print("Warning: Soil moisture levels are not within the recommended range.")

    # Specific recommendations based on crop type
    if crop_type == "wheat":
        print("Consider adjusting planting schedule for optimal wheat growth.")

    elif crop_type == "rice":
        print("Ensure proper water management for rice cultivation.")

    elif crop_type == "tomatoes":
        print("Check for signs of pests and diseases in tomato plants.")

    else:
        print("No specific recommendations for the given crop type.")

# Example usage
display_agriculture_problems(25, 60, 50, "wheat")

