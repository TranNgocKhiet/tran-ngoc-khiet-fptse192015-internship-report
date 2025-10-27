---
title : "Set up Amazon DynamoDB"
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

#### Overview

- In this section, you will configure Amazon DynamoDB tables to store and manage Smart Office data. Each table supports specific functions such as room configuration, user automation schedules, and real-time logs. You will also enable Time to Live (TTL) for automatic cleanup, Point-in-Time Recovery (PITR) for data protection, and DynamoDB Streams to trigger AWS Lambda functions upon data changes.
  
- Why using DynamoDB with TTL, PITR, and Streams:
<br> &emsp;- TTL (Time to Live) automatically removes expired items (e.g., old logs), optimizing storage and cost.
<br> &emsp;- PITR (Point-in-Time Recovery) ensures data resilience, allowing full table recovery within 35 days.
<br> &emsp;- Streams capture real-time updates (both old and new images) and trigger Lambda to sync room modes or automation changes with IoT Core instantly.





