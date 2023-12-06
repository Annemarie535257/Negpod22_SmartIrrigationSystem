import sqlite3
from getpass import getpass

def initialize_database():
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def sign_up():
    print("Sign Up:")
    username = input("Enter a username: ")
    password = getpass("Enter a password: ")
    email = input("Enter your email: ")

    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, email))

    conn.commit()
    conn.close()

    print("Registration successful!")

def login():
    print("Login:")
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        print("Login successful!")
    else:
        print("Invalid username or password.")

def main():
    initialize_database()

    print("Choose an option:")
    print("1. Sign Up")
    print("2. Login")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        sign_up()
    elif choice == "2":
        login()
    else:
        print("Invalid choice. Please enter either '1' for Sign Up or '2' for Login.")

if __name__ == "__main__":
    main()
