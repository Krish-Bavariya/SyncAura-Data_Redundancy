from database import load_sessions


def detect_anomaly(new_session):

    sessions = load_sessions()

    for s in sessions:

        if s["user_id"] == new_session["user_id"]:

            # Device change detection
            if s["device_id"] != new_session["device_id"]:
                print("Anomaly detected: Device changed")
                return True

            # Location change detection
            if s["location"] != new_session["location"]:
                print("Anomaly detected: Location changed")
                return True

    return False