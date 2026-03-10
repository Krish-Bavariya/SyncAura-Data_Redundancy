# SyncAura – Feature Development Task Checklist

This checklist helps the team track the progress of the **SyncAura Region Detection & Single-Device Join module**.
Mark tasks as completed (`[x]`) when finished.

---

# Project Goal

Build a lightweight module that:

* Detects the **region (city/country) of meeting participants**
* Prevents **users from joining the same meeting from multiple devices**
* Logs session information for monitoring and analysis

---

# Member 1 – Region Detection Module

## Setup

* [ ] Create project folder structure
* [ ] Create `src/location.py`

## IP Capture

* [ ] Implement function to capture user IP
* [ ] Validate IP format
* [ ] Handle missing or invalid IP cases

## Region Detection

* [ ] Integrate GeoIP API
* [ ] Implement function `get_location(ip)`
* [ ] Extract:

  * [ ] Country
  * [ ] City
  * [ ] Region

## Data Formatting

* [ ] Structure location data as JSON
* [ ] Ensure compatibility with session storage

## Testing

* [ ] Test with multiple IP addresses
* [ ] Handle API errors gracefully

---

# Member 2 – Device Validation Module

## Device Fingerprinting

* [ ] Create `src/device.py`
* [ ] Capture device attributes:

  * [ ] Browser
  * [ ] Operating system
  * [ ] Screen resolution
  * [ ] IP address

## Device ID Generation

* [ ] Implement `generate_device_id()`
* [ ] Generate hash for device fingerprint
* [ ] Ensure uniqueness of device ID

## Session Control

* [ ] Create `src/session.py`
* [ ] Implement join validation logic
* [ ] Check if user already active in meeting
* [ ] Block additional device attempts
* [ ] Return join status message

## Testing

* [ ] Test same device join
* [ ] Test multiple device attempts
* [ ] Confirm rejection logic works

---

# Member 3 – Data Storage & ML Module

## Database Setup

* [ ] Create `src/database.py`
* [ ] Implement session load function
* [ ] Implement session save function

## Session Logging

* [ ] Create `data/sessions.json`
* [ ] Store fields:

  * [ ] user_id
  * [ ] meeting_id
  * [ ] device_id
  * [ ] location
  * [ ] timestamp

## Data Validation

* [ ] Ensure sessions append correctly
* [ ] Prevent duplicate entries
* [ ] Handle missing fields

## ML Prototype (Optional but recommended)

* [ ] Create `src/anomaly_detection.py`
* [ ] Define feature inputs

  * [ ] device change count
  * [ ] location change distance
  * [ ] IP change frequency
* [ ] Implement anomaly detection model
* [ ] Test with sample dataset

---

# Final Validation

* [ ] Clean code and remove debug prints
* [ ] Verify folder structure
* [ ] Add comments to important functions
* [ ] Create final demo scenario
* [ ] Prepare presentation or demo script

---

# Demo Scenario Checklist

* [ ] User joins meeting normally
* [ ] System displays detected region
* [ ] Session stored in logs
* [ ] Same user attempts second device join
* [ ] System blocks second login
* [ ] Display access denied message

---

# Project Completion Status

| Task Area         | Status |
| ----------------- | ------ |
| Region Detection  | ⬜      |
| Device Validation | ⬜      |
| Session Storage   | ⬜      |
| ML Prototype      | ⬜      |
| Final Testing     | ⬜      |

---

# Notes

Use this checklist during development meetings to track:

* completed tasks
* pending tasks
* blockers or issues
