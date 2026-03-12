import requests
import json

GEO_API = "http://ip-api.com/json/"


def get_location(ip):
    """
    Fetch location information from GeoIP API
    Returns JSON-compatible location data
    """

    try:
        response = requests.get(GEO_API + ip, timeout=5)
        data = response.json()

        if data["status"] != "success":
            return {"error": "GeoIP lookup failed"}

        # Structured location data
        location_data = {
            "country": data.get("country"),
            "city": data.get("city"),
            "region": data.get("regionName")
        }

        return location_data

    except Exception as e:
        return {"error": str(e)}


# Manual testing block
if __name__ == "__main__":

    ip = input("Enter IP address: ")

    location = get_location(ip)

    print("\nLocation (Dictionary):")
    print(location)

    print("\nLocation (JSON format):")
    print(json.dumps(location, indent=4))
