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
-- INSERT --                                                                                                     1,1           Top
