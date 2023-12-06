class UserTracker:
    def __init__(self, user_id):
        self.user_id = user_id
        self.user_events = []

    def track_event(self, event_name, timestamp):
        event = {
            'event_name': event_name,
            'timestamp': timestamp
        }
        self.user_events.append(event)
        print(f"Event tracked for user {self.user_id}: {event_name} at {timestamp}")

    def get_user_events(self):
        return self.user_events


# Example Usage:
user1_tracker = UserTracker(user_id=1)

user1_tracker.track_event('Login', '2023-11-16 12:30:00')
user1_tracker.track_event('Page View', '2023-11-16 12:35:00')

user1_events = user1_tracker.get_user_events()
print(f"\nUser 1 Events: {user1_events}")

