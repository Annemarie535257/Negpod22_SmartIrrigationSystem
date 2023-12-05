import sqlite3
from getpass import getpass  # For securely entering passwords

# Function to create a database connection and initialize the table
def initialize_database():
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    # Create a table if it doesn't exist
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

# Function to get user information and store it in the database
def get_user_info():
    print("Enter your personal information:")
    username = input("Username: ")
    password = getpass("Password: ")  # Using getpass to securely enter passwords
    email = input("Email: ")

    # Insert user information into the database
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, email))

    conn.commit()
    conn.close()

    print(i"Registration successful!")

# Main function to initialize the database and get user information
def main():
    initialize_database()
    get_user_info()

if __name__ == "__main__":
    main()
