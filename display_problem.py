import random
from datetime import datetime

class SoilMoistureSensor:
    def __init__(self, location):
        self.location = location
        self.moisture_level = 0  # Initialize moisture level

    def measure_moisture(self):
        self.moisture_level = random.uniform(0, 10)

    def get_moisture_level(self):
        return self.moisture_level

class IrrigationSystem:
    def __init__(self, threshold=5):
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

