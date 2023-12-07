import random
from datetime import datetime

class SoilMoistureSensor:
    def __init__(self, location):
        self.location = location
        self.moisture_level = 0  # Initialize moisture level

    def measure_moisture(self):
        # Simulate measuring soil moisture (replace with actual sensor readings)
        self.moisture_level = random.uniform(0, 100)

    def get_moisture_level(self):
        return self.moisture_level

class IrrigationSystem:
    def __init__(self, threshold=30):
        self.threshold = threshold  # Moisture level below which irrigation is needed

    def needs_irrigation(self, moisture_level):
        return moisture_level < self.threshold

def display_soil_moisture(sensor, irrigation_system):
    sensor.measure_moisture()
    moisture_level = sensor.get_moisture_level()
    need_irrigation = irrigation_system.needs_irrigation(moisture_level)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Location: {sensor.location}")
    print(f"Timestamp: {timestamp}")
    print(f"Soil Moisture Level: {moisture_level:.2f}%")

    if need_irrigation:
        print("Irrigation is needed!\n")
    else:
        print("No irrigation needed.\n")

# Example of usage
if __name__ == "__main__":
    # Create a soil moisture sensor for a specific location
    sensor1 = SoilMoistureSensor(location="Garden")

    # Create an irrigation system with a moisture threshold
    irrigation_system1 = IrrigationSystem(threshold=30)

    # Display soil moisture information
    display_soil_moisture(sensor1, irrigation_system1)

