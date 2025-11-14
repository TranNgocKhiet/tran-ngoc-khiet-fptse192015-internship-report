---
title : "Introduction"
weight : 1 
chapter : false
pre : " <b> 5.1. </b> "
---

#### Serverless & Event-Driven Architecture
+ **Serverless Architecture**: This project uses cloud services like **AWS Lambda**, **API Gateway**, and **DynamoDB**. This model allows code to run in response to events without managing or provisioning servers, as AWS handles all scaling and infrastructure.
+ **Event-Driven Architecture**: The core of the system is event-driven. Instead of services polling each other, events (like a sensor reading or a user request) trigger downstream processes. This is managed by services like **Amazon EventBridge**, **SQS**, and **AWS IoT Core**, creating a flexible and scalable system.

#### Workshop overview
In this workshop, you will deploy a serverless data platform on AWS to process real-time environmental data from 8 rooms. The system uses IoT Core, Lambda, DynamoDB, S3, EventBridge, and SNS. Sensor data is forwarded from edge devices or simulated scripts, ingested into AWS, stored in DynamoDB tables, processed by Lambda, and routed through EventBridge for alerting or downstream automation. This architecture provides high availability, low cost, and seamless scalability as more rooms or sensors are added.

![overview](/images/5-Workshop/5.1-Workshop-overview/Smart-Office-Architect-Diagram.drawio.png)
