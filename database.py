import json
import os

# Path to session storage file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "Data", "sessions.json")


# Load all stored sessions
def load_sessions() -> list:
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as file:
        data = json.load(file)
        return data if isinstance(data, list) else []


# Validate required session fields
def validate_session(session):

    required_fields = [
        "user_id",
        "meeting_id",
        "device_id",
        "location",
        "timestamp"
    ]

    for field in required_fields:
        if field not in session:
            print("Missing field:", field)
            return False

    return True


# Save new session and prevent duplicate device login
def save_session(session):

    if not validate_session(session):
        print("Session validation failed")
        return

    sessions = load_sessions()

    for s in sessions:
        if s["user_id"] == session["user_id"] and s["meeting_id"] == session["meeting_id"]:

            if s["device_id"] != session["device_id"]:
                print("Access denied: second device login detected")
                return

    sessions.append(session)

    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    with open(FILE_PATH, "w") as file:
        json.dump(sessions, file, indent=4)

    print("Session stored successfully")