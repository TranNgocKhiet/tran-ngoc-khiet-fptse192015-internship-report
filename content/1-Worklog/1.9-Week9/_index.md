---
title: "Week 9 Worklog"
weight: 9
chapter: false
pre: " <b> 1.7. </b> "
---

### Week 9 Objectives:
* Implement MQTT Messaging for the Project.
* Define Topic Hierarchy.
* Simulate Data Publication.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2   | - **Project:** Define Topic Structure <br> - **Practice:** <br>&emsp; + Finalize topics (e.g., `office/room1/temp`) | 11/03/2025 | 11/03/2025 | <https://docs.aws.amazon.com/iot/latest/developerguide/topics.html> |
| 3   | - **Project:** Python MQTT Script <br> - **Practice:** <br>&emsp; + Write Python script using `AWSIoTPythonSDK` <br>&emsp; + Configure script with Certs from Week 6 | 11/04/2025 | 11/04/2025 | <https://github.com/aws/aws-iot-device-sdk-python> |
| 4   | - **Project:** Data Simulation <br> - **Practice:** <br>&emsp; + Update script to publish random JSON data | 11/05/2025 | 11/05/2025 | <https://www.youtube.com/watch?v=kYJj7K0fT4Y> |
| 5   | - **Project:** Verify Data <br> - **Practice:** <br>&emsp; + Use AWS Console MQTT Client to subscribe to `office/*` and watch data flow | 11/06/2025 | 11/06/2025 | <https://docs.aws.amazon.com/iot/latest/developerguide/view-mqtt-messages.html> |
| 6   | - **Project:** Threading <br> - **Practice:** <br>&emsp; + Add Threading logic to Python script for multiple devices simulation | 11/07/2025 | 11/07/2025 | <https://www.geeksforgeeks.org/python/multithreading-python-set-1/> |

### Week 9 Achievements:
* Defined a logical MQTT topic hierarchy for the Smart Office.
* Created a Python script to simulate hardware sensors.
* Successfully published telemetry data to AWS IoT Core.