import requests
import re


def validate_ip(ip):
    """
    Validate IPv4 address format
    """
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"

    if re.match(pattern, ip):
        return True
    return False


def get_location(ip):
    """
    Get location data from IP address
    """

    if not validate_ip(ip):
        return {"error": "Invalid IP address"}

    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url, timeout=5)
        data = response.json()

        if data["status"] != "success":
            return {"error": "Location lookup failed"}

        location_data = {
            "country": data.get("country"),
            "city": data.get("city"),
            "region": data.get("regionName"),
        }

        return location_data

    except Exception as e:
        return {"error": str(e)}


# Run test if executed directly
if __name__ == "__main__":

    test_ips = [
        "8.8.8.8",       # Google DNS (USA)
        "1.1.1.1",       # Cloudflare DNS
        "49.36.10.5",    # Example India IP
        "999.999.999.999" # Invalid IP
    ]

    for ip in test_ips:
        print(f"\nTesting IP: {ip}")
        print(get_location(ip))
