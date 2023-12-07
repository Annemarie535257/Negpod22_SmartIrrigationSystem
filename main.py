from irrigation_system import start_irrigation, stop_irrigation, adjust_settings, check_system_status
from answer_validation import validate_user_input
from user_registration import initialize_database, sign_up, login

def main():
    print("WELCOME TO THE UNIQUE SMART IRRIGATION SYSTEM")

    initialize_database()  # Initialize the user database

    while True:
        print("\nSMART IRRIGATION SYSTEM MENU")
        print("1. User Registration")
        print("2. Login")
        print("3. Start Irrigation")
        print("4. Stop Irrigation")
        print("5. Adjust Settings")
        print("6. Check System Status")
        print("7. Exit")

        user_input = input("\nEnter your choice (1-7): ")

        if validate_user_input(user_input):
            choice = int(user_input)
            if 1 <= choice <= 7:
                if choice == 1:
                    sign_up()
                elif choice == 2:
                    login()
                elif choice == 3:
                    start_irrigation()
                elif choice == 4:
                    stop_irrigation()
                elif choice == 5:
                    adjust_settings()
                elif choice == 6:
                    check_system_status()
                elif choice == 7:
                    print("Exiting the program. Thank you for using the Unique Smart Irrigation System!!")
                    break
            else:
                print("Please provide a valid input (1-7)")
        else:
            print("Invalid input. Please enter a number (1-7).")

if __name__ == "__main__":
    main()


