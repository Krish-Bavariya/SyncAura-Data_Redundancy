from device_validation import DeviceFingerprint, SessionManager
from anomaly_detection import detect_anomaly
from database import save_session

manager = SessionManager()


# ✅ DEFINE FUNCTION FIRST
def handle_user_join(user_id, meeting_id, browser, location):

    device = DeviceFingerprint(browser=browser)
    device_id = device.generate_device_id()

    result = manager.join_meeting(user_id, device)
    print(result)

    if result["status"] == "rejected":
        print("Blocked at device validation level")
        return

    session = {
        "user_id": user_id,
        "meeting_id": meeting_id,
        "device_id": device_id,
        "location": location,
        "timestamp": "2026-03-26T10:00:00"
    }

    if detect_anomaly(session):
        print("Blocked due to anomaly detection")
        return

    save_session(session)
    print("User successfully joined\n")


# ✅ CALL FUNCTION AT BOTTOM
if __name__ == "__main__":
    print("---- FIRST LOGIN ----")
    handle_user_join("U101", "M001", "Chrome", "India")

    print("---- SAME DEVICE LOGIN ----")
    handle_user_join("U101", "M001", "Chrome", "India")

    print("---- DIFFERENT DEVICE LOGIN ----")
    handle_user_join("U101", "M001", "Firefox", "India")