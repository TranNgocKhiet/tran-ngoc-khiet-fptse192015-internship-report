---
title: "Week 10 Worklog"
weight: 10
chapter: false
pre: " <b> 1.8. </b> "
---

### Week 10 Objectives:
* Configure AWS IoT Rules Engine.
* Integrate IoT Core with EventBridge.
* Filter incoming data.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2   | - **Project:** IoT Rules <br> - **Practice:** <br>&emsp; + Write SQL statement to select data: <br> e.g `SELECT * FROM 'office/+/temp'` | 11/10/2025 | 11/10/2025 | <https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-reference.html> |
| 3   | - **Project:** Create Rule <br> - **Practice:** <br>&emsp; + Create an IoT Rule in Console <br>&emsp; + Set Action: "Send a message to EventBridge" | 11/11/2025 |11/11/2025  | <https://docs.aws.amazon.com/iot/latest/developerguide/eventbridge-rule.html> |
| 4   | - **Project:** EventBridge Setup <br> - **Practice:** <br>&emsp; + Go to EventBridge, check for incoming events | 11/12/2025 | 11/12/2025 | <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-iot-event.html> |
| 5   | - **Project:** Event Pattern <br> - **Practice:** <br>&emsp; + Create an EventBridge Rule with a pattern to match High Temp (> 40C) | 11/13/2025 | 11/13/2025 | <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html> |
| 6   | - **Project:** Testing Integration <br> - **Practice:** <br>&emsp; + Publish high temp data via Python script <br>&emsp; + Verify Rule metric count increases | 11/14/2025 | 11/14/2025 | <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-monitoring.html> |

### Week 10 Achievements:
* Configured IoT SQL Rules to filter message traffic.
* Established a direct integration between IoT Core and EventBridge.
* Defined EventBridge patterns to detect "High Temperature" anomalies.