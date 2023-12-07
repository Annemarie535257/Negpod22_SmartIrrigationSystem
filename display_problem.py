import random
from datetime import datetime

import sqlite3

# Connect to SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Create a table to store soil moisture data if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS moisture_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location TEXT,
        timestamp DATETIME,
        moisture_level REAL,
        need_irrigation INTEGER
    )
''')

conn.commit()

def display_soil_moisture(sensor, irrigation_system):
    sensor.measure_moisture()
    moisture_level = sensor.get_moisture_level()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Display soil moisture level
    print(f"Location: {sensor.location}")
    print(f"Timestamp: {timestamp}")
    print(f"Soil Moisture Level: {moisture_level:.2f}%")
    
    # Store data in the database
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO moisture_data (location, timestamp, moisture_level)
        VALUES (?, ?, ?)
    ''', (sensor.location, timestamp, moisture_level))

    conn.commit()
    conn.close()


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

if __name__ == "__main__":
    sensor1 = SoilMoistureSensor(location="Fields")
    irrigation_system1 = IrrigationSystem(threshold=5)
    display_soil_moisture(sensor1, irrigation_system1)

