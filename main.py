from irrigation_system import start_irrigation, stop_irrigation, adjust_settings, check_system_status
from answer_validation import validate_user_input
from user_registration import initialize_database, sign_up, login

def main():
    print("WELCOME TO THE UNIQUE SMART IRRIGATION SYSTEM")

    initialize_database()  # Initialize the user database

    while True:
        print("\nSMART IRRIGATION SYSTEM MENU")
        print("1. Start Irrigation")
        print("2. Stop Irrigation")
        print("3. Adjust Settings")
        print("4. Check System Status")
        print("5. User Registration")
        print("6. Login")
        print("7. Exit")

        user_input = input("\nEnter your choice (1-7): ")

        if validate_user_input(user_input):
            choice = int(user_input)
            if 1 <= choice <= 7:
                if choice == 1:
                    start_irrigation()
                elif choice == 2:
                    stop_irrigation()
                elif choice == 3:
                    adjust_settings()
                elif choice == 4:
                    check_system_status()
                elif choice == 5:
                    sign_up()
                elif choice == 6:
                    login()
                elif choice == 7:
                    print("Exiting the program. Thank you for using the Unique Smart Irrigation System!")
                    break
            else:
                print("Please provide a valid input (1-7)")
        else:
            print("Invalid input. Please enter a number (1-7).")

if __name__ == "__main__":
    main()

