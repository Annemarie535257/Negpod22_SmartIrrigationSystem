from datetime import datetime

class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.activities = []

class UserTracker:
    def __init__(self):
        self.users = {}

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
            print(f"Activity tracked for user {user_id} ({user.username}): {activity_name} at {timestamp}")
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

# Create users
tracker.create_user(user_id=1, username='Alice')
tracker.create_user(user_id=2, username='Bob')

# Track activities for user 1
tracker.track_activity(user_id=1, activity_name='Login', '2023-11-29 12:30:00')
tracker.track_activity(user_id=1, activity_name='Page View', '2023-11-29 12:35:10')

# Track activities for user 2
tracker.track_activity(user_id=2, activity_name='Login', '2023-11-30 11:45:12')
tracker.track_activity(user_id=2, activity_name='Search', '2023-11-30 1:47:35')

# Track activities for user 3
tracker.track_activity(user_id=3, activity_name='Login', '2023-12-2 1:15:00')
tracker.track_activity(user_id=3, activity_name='Form submission', '2023-12-4 3:30:05')

# Get activities for user 1 and user 2
user1_activities = tracker.get_user_activities(user_id=1)
user2_activities = tracker.get_user_activities(user_id=2)

print(f"\nUser 1 Activities: {user1_activities}")
print(f"User 2 Activities: {user2_activities}")


