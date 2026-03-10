# SyncAura Session & Region Tracker

A lightweight prototype module for **SyncAura**, an internal meeting platform.
This module focuses on two main features:

1. Detecting the **region (city/country)** from which a user joins a meeting.
2. Preventing a **single user from joining the same meeting from multiple devices**.

The project is designed as a **minimal and efficient prototype** suitable for internship demonstrations and experimentation.

---

# Features

* 🌍 **Region Detection**

  * Detects the user's **country and city** using their IP address.

* 🔐 **Single Device Join Enforcement**

  * Prevents a user from joining the same meeting from multiple devices.

* 💾 **Session Logging**

  * Stores session data locally for monitoring and analysis.

* 🤖 **Optional ML Anomaly Detection**

  * Detects suspicious behavior such as rapid device switching or location changes.

---

# Project Structure

```
syncaura-tracker/

src/
 ├── location.py
 ├── device.py
 ├── session.py
 ├── database.py
 └── anomaly_detection.py

data/
 └── sessions.json

main.py
requirements.txt
README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/syncaura-tracker.git
cd syncaura-tracker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Requirements

```
requests
scikit-learn
```

---

# Running the Prototype

Run the main script:

```bash
python main.py
```

Example output:

```
User: U101
Meeting: M21
Location: Pune, India
Device: Laptop

Status: Join Successful
```

If the same user tries to join from another device:

```
User already active in meeting
Access Denied
```

---

# Code Implementation

## main.py

```python
from src.location import get_location
from src.device import generate_device_id
from src.session import join_meeting

user_id = "U101"
meeting_id = "M202"

ip = "8.8.8.8"
browser = "Chrome"
os = "Windows"
screen = "1920x1080"

location = get_location(ip)

device_id = generate_device_id(browser, os, screen, ip)

status = join_meeting(user_id, meeting_id, device_id, location)

print(status)
```

---

# src/location.py

```python
import requests

def get_location(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()

    return {
        "country": data.get("country"),
        "city": data.get("city")
    }
```

---

# src/device.py

```python
import hashlib

def generate_device_id(browser, os, screen, ip):

    raw = browser + os + screen + ip

    device_hash = hashlib.sha256(raw.encode()).hexdigest()

    return device_hash
```

---

# src/database.py

```python
import json
import os

DB_FILE = "data/sessions.json"


def load_sessions():

    if not os.path.exists(DB_FILE):
        return []

    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_sessions(sessions):

    with open(DB_FILE, "w") as f:
        json.dump(sessions, f, indent=4)
```

---

# src/session.py

```python
from src.database import load_sessions, save_sessions


def join_meeting(user_id, meeting_id, device_id, location):

    sessions = load_sessions()

    for session in sessions:

        if session["user_id"] == user_id and session["meeting_id"] == meeting_id:
            return "User already active in meeting. Access Denied."

    new_session = {
        "user_id": user_id,
        "meeting_id": meeting_id,
        "device_id": device_id,
        "location": location
    }

    sessions.append(new_session)

    save_sessions(sessions)

    return "Join Successful"
```

---

# src/anomaly_detection.py (Optional ML Feature)

```python
from sklearn.ensemble import IsolationForest
import numpy as np


def detect_anomaly(data):

    model = IsolationForest(contamination=0.1)

    model.fit(data)

    prediction = model.predict(data)

    return prediction
```

Example feature data:

```
device_change_count
location_change_distance
ip_change_frequency
```

---

# Example Stored Session Data

`data/sessions.json`

```json
[
    {
        "user_id": "U101",
        "meeting_id": "M202",
        "device_id": "abc123",
        "location": {
            "country": "India",
            "city": "Pune"
        }
    }
]
```

---

# Task Division (3 Members)

### Member 1 – Location Detection

Responsibilities:

* Capture user IP
* Convert IP to region
* Implement `location.py`

---

### Member 2 – Device Validation

Responsibilities:

* Generate device fingerprint
* Prevent multiple device joins
* Implement:

```
device.py
session.py
```

---

### Member 3 – Data & ML

Responsibilities:

* Session storage
* Participation logging
* ML anomaly detection

Files:

```
database.py
anomaly_detection.py
```

---

# Future Improvements

* Real-time meeting integration
* Browser fingerprinting
* Dashboard for meeting host
* Advanced ML fraud detection
* Scalable database (PostgreSQL)

---

# License

This project is intended for **research and educational purposes** as part of the SyncAura internship project.
