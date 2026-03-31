from database import save_session
from anomaly_detection import detect_anomaly


def detect_region(location):
    print("Detected region:", location)


print("----- SyncAura Security System -----\n")

# First user login
session1 = {
    "user_id": "U101",
    "meeting_id": "M001",
    "device_id": "Laptop123",
    "location": "India",
    "timestamp": "2026-03-16T10:30:00"
}

print("User joining meeting...\n")

detect_region(session1["location"])

if not detect_anomaly(session1):
    save_session(session1)


print("\nSecond login attempt from another device...\n")

session2 = {
    "user_id": "U101",
    "meeting_id": "M001",
    "device_id": "Mobile456",
    "location": "India",
    "timestamp": "2026-03-16T10:31:00"
}

detect_region(session2["location"])

if detect_anomaly(session2):
    print("Access denied: Multiple device login detected")
else:
    save_session(session2)