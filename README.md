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

* [x] Create project folder structure
* [x] Create `src/location.py`

## IP Capture

* [x] Implement function to capture user IP
* [x] Validate IP format
* [x] Handle missing or invalid IP cases

## Region Detection

* [x] Integrate GeoIP API
* [x] Implement function `get_location(ip)`
* [x] Extract:

  * [x] Country
  * [x] City
  * [x] Region

## Data Formatting

* [x] Structure location data as JSON
* [x] Ensure compatibility with session storage

## Testing

* [x] Test with multiple IP addresses
* [x] Handle API errors gracefully

---

# Member 2 – Device Validation Module

## Device Fingerprinting

* [x] Create `src/device.py`
* [x] Capture device attributes:

  * [x] Browser
  * [x] Operating system
  * [x] Screen resolution
  * [x] IP address

## Device ID Generation

* [x] Implement `generate_device_id()`
* [x] Generate hash for device fingerprint
* [x] Ensure uniqueness of device ID

## Session Control

* [x] Create `src/session.py`
* [x] Implement join validation logic
* [x] Check if user already active in meeting
* [x] Block additional device attempts
* [x] Return join status message

## Testing

* [x] Test same device join
* [x] Test multiple device attempts
* [x] Confirm rejection logic works

---

# Member 3 – Data Storage & ML Module

## Database Setup

* [x] Create `src/database.py`
* [x] Implement session load function
* [x] Implement session save function

## Session Logging

* [x] Create `data/sessions.json`
* [x] Store fields:

  * [x] user_id
  * [x] meeting_id
  * [x] device_id
  * [x] location
  * [x] timestamp

## Data Validation

* [x] Ensure sessions append correctly
* [x] Prevent duplicate entries
* [x] Handle missing fields

## ML Prototype (Optional but recommended)

* [x] Create `src/anomaly_detection.py`
* [x] Define feature inputs

  * [x] device change count
  * [x] location change distance
  * [x] IP change frequency
* [x] Implement anomaly detection model
* [x] Test with sample dataset

---

# Final Validation

* [x] Clean code and remove debug prints
* [x] Verify folder structure
* [x] Add comments to important functions
* [x] Create final demo scenario
* [x] Prepare presentation or demo script

---

# Demo Scenario Checklist

* [x] User joins meeting normally
* [x] System displays detected region
* [x] Session stored in logs
* [x] Same user attempts second device join
* [x] System blocks second login
* [x] Display access denied message

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
