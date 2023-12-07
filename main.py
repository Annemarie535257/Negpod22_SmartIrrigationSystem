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
