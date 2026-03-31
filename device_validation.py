import hashlib
import platform
import socket


# ------------------ DEVICE FINGERPRINT ------------------

class DeviceFingerprint:
    def __init__(self, browser=None, screen_resolution=None, ip_address=None):
        self.browser = browser or "Unknown"
        self.operating_system = platform.system()
        self.screen_resolution = screen_resolution or "Unknown"
        self.ip_address = ip_address or self._get_ip_address()

    def _get_ip_address(self):
        try:
            hostname = socket.gethostname()
            return socket.gethostbyname(hostname)
        except:
            return "Unknown"

    def generate_device_id(self):
        device_string = f"{self.browser}|{self.operating_system}|{self.screen_resolution}|{self.ip_address}"
        return hashlib.sha256(device_string.encode()).hexdigest()


# ------------------ SESSION CONTROL ------------------

class SessionManager:
    def __init__(self):
        self.active_sessions = {}  # user_id -> device_id

    def join_meeting(self, user_id, device):
        device_id = device.generate_device_id()

        if user_id in self.active_sessions:
            if self.active_sessions[user_id] == device_id:
                return {"status": "accepted", "message": "Same device rejoined"}
            else:
                return {"status": "rejected", "message": "User already active on another device"}

        self.active_sessions[user_id] = device_id
        return {"status": "accepted", "message": "Joined successfully"}

    def leave_meeting(self, user_id):
        if user_id in self.active_sessions:
            del self.active_sessions[user_id]
            return {"status": "left", "message": "Left meeting"}
        return {"status": "error", "message": "User not found"}


# ------------------ MAIN DEMO ------------------

if __name__ == "__main__":

    manager = SessionManager()

    print("Test Run")

    device1 = DeviceFingerprint(browser="Chrome")
    print(manager.join_meeting("user1", device1))

    print("\nSame Device Join")
    print(manager.join_meeting("user1", device1))

    print("\nDifferent Device Attempt")
    device2 = DeviceFingerprint(browser="Firefox")
    print(manager.join_meeting("user1", device2))

    print("\nLeave Meeting")
    print(manager.leave_meeting("user1"))