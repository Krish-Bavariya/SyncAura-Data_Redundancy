from database import save_session
from anomaly_detection import detect_anomaly


session1 = {
    "user_id": "U101",
    "meeting_id": "M001",
    "device_id": "Laptop123",
    "location": "India",
    "timestamp": "2026-03-16T10:30:00"
}

session2 = {
    "user_id": "U101",
    "meeting_id": "M001",
    "device_id": "Mobile456",
    "location": "India",
    "timestamp": "2026-03-16T10:31:00"
}


print("User joining meeting...")

if not detect_anomaly(session1):
    save_session(session1)

print("\nSecond login attempt...")

if detect_anomaly(session2):
    print("Access denied due to anomaly")
else:
    save_session(session2)