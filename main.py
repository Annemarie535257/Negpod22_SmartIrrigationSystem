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
 user_input = input("\nEnter your choice (1-8): ")

        if user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= 8:
                if choice == 1:
                    sign_up()
                elif choice == 2:
                    login()
                elif choice == 3:
                    display_soil_moisture(sensor, irrigation_system)
                    time.sleep(4)
                elif choice == 4:
                    start_irrigation()
                elif choice == 5:
                    stop_irrigation()
                elif choice == 6:
                    adjust_settings()
                elif choice == 7:
                    check_system_status()
                elif choice == 8:
                    print("Exiting the program. Thank you for using the Unique Smart Irrigation System!")
                    break
            else:
                print("Please provide a valid input (1-8)")
        else:
            print("Invalid input. Please enter a number (1-7).")
if __name__ == "__main__":
    main()
