import time
import random

def menu():
    print("\nSMART IRRIGATION SYSTEM MENU")
    print("1. Start Irrigation")
    print("2. Stop Irrigation")
    print("3. Adjust Settings")
    print("4. Check System Status")
    print("5. Exit")

def start_irrigation():
    print("\nStarting irrigation. Please wait...")
    time.sleep(2)
    print("Irrigation in progress.")

def stop_irrigation():
    print("\nStopping irrigation.")
    time.sleep(1)
    print("Irrigation halted. Soil moisture levels stabilized.")

def adjust_settings():
    print("\nAdjusting irrigation settings. Finding the optimal balance.")
    time.sleep(2)
    print("Settings adjusted. The system is now optimized for efficiency.")

def check_system_status():
    print("\nChecking system status. Verifying sensors and components.")
    time.sleep(1)
    status = random.choice(["Normal", "Sensors Offline", "Low Water Supply"])
    print(f"System status: {status}")

def main():
    print("WELCOME TO THE UNIQUE SMART IRRIGATION SYSTEM")

    while True:
        menu()
        user_input = input("\nEnter your choice (1-5): ")

        if user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= 5:
                if choice == 1:
                    start_irrigation()
                elif choice == 2:
                    stop_irrigation()
                elif choice == 3:
                    adjust_settings()
                elif choice == 4:
                    check_system_status()
                elif choice == 5:
                    print("Exiting the program. Thank you for using the Unique Smart Irrigation System!")
                    break
            else:
                print("Please provide a valid input (1-5)")
        else:
            print("Invalid input. Please enter a number (1-5).")

if __name__ == "__main__":
    main()

