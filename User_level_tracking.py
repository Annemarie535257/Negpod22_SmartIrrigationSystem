from datetime import datetime
import sqlite3

# Connect to SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Create a table to store user activities if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_activities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        username TEXT,
        activity_name TEXT,
        timestamp DATETIME
    )
''')

conn.commit()


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.activities = []


class UserTracker:
    def __init__(self):
        self.users = {}
        self.load_users_from_db()

    def load_users_from_db(self):
        cursor.execute('SELECT DISTINCT user_id, username FROM user_activities')
        rows = cursor.fetchall()
        for row in rows:
            user_id, username = row
            new_user = User(user_id, username)
            self.users[user_id] = new_user

    def create_user(self, user_id, username):
        if user_id not in self.users:
            new_user = User(user_id, username)
            self.users[user_id] = new_user
            print(f"User {user_id} ({username}) created.")
        else:
            print(f"User {user_id} already exists.")

    def track_activity(self, user_id, activity_name):
        if user_id in self.users:
            user = self.users[user_id]
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            activity = {'activity_name': activity_name, 'timestamp': timestamp}
            user.activities.append(activity)

            # Store data in the database
            cursor.execute('''
                INSERT INTO user_activities (user_id, username, activity_name, timestamp)
                VALUES (?, ?, ?, ?)
            ''', (user_id, user.username, activity_name, timestamp))

            print(f"Activity tracked for user {user_id} ({user.username}): {activity_name} at {timestamp}")
            conn.commit()
        else:
            print(f"User {user_id} does not exist.")

    def get_user_activities(self, user_id):
        if user_id in self.users:
            user = self.users[user_id]
            return user.activities
        else:
            print(f"User {user_id} does not exist.")
            return []

# Example Usage:
tracker = UserTracker()

# Track activities for users
tracker.track_activity(user_id=1, activity_name='Login')
tracker.track_activity(user_id=1, activity_name='Page View')
tracker.track_activity(user_id=1, activity_name='Logout')

tracker.track_activity(user_id=2, activity_name='Login')
tracker.track_activity(user_id=2, activity_name='Search')
tracker.track_activity(user_id=2, activity_name='Logout')

tracker.track_activity(user_id=3, activity_name='Login')
tracker.track_activity(user_id=3, activity_name='Form submission')
tracker.track_activity(user_id=3, activity_name='Logout')

# Get activities for users
user1_activities = tracker.get_user_activities(user_id=1)
user2_activities = tracker.get_user_activities(user_id=2)
user3_activities = tracker.get_user_activities(user_id=3)

print(f"\nUser 1 Activities: {user1_activities}")
print(f"User 2 Activities: {user2_activities}")
print(f"User 3 Activities: {user3_activities}")

# Close the database connection
conn.close()



