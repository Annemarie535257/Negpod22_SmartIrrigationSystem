from datetime import datetime
import time 
import random
from getpass import getpass
from display_problem import SoilMoistureSensor, IrrigationSystem
from display_problem import display_soil_moisture 
from user_registration import initialize_database, sign_up, login
from irrigation_system import menu, start_irrigation, stop_irrigation, adjust_settings, check_system_status
def main():
    print("WELCOME TO THE UNIQUE SMART IRRIGATION SYSTEM")

    # Initialize the user database
    initialize_database()
        # Create instances of SoilMoistureSensor and IrrigationSystem
    sensor = SoilMoistureSensor(location="Fields")
    irrigation_system = IrrigationSystem(threshold=5)
while True:
        print("\nSMART IRRIGATION SYSTEM MENU")
        print("1. Signup")
        print("2. Login")
        print("3. check moisture level")
        print("4. Start Irrigation")
        print("5. Stop Irrigation")
        print("6. Adjust Settings")
        print("7. Check System Status")
        print("8. Exit")
