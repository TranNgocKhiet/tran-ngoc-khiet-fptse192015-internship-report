---
title : "Introduction"
weight : 1 
chapter : false
pre : " <b> 5.1. </b> "
---

#### Serverless & Event-Driven Architecture
+ **Serverless Architecture**: This workshop utilizes a cloud-native model with services like **AWS Lambda**, **Amazon API Gateway**, and **Amazon DynamoDB**. This approach allows code to run in response to requests without provisioning or managing servers, as AWS handles all automatic scaling and infrastructure management.
+ **Event-Driven Architecture**: The core of the system functions on an event-driven basis. Instead of services continuously polling for data, specific events—such as IoT sensor readings or user API calls—trigger downstream workflows. This is orchestrated by **AWS IoT Core** and **Amazon EventBridge**, creating a highly flexible and scalable system.

#### Workshop overview
In this workshop, you will deploy a comprehensive serverless data platform on AWS to manage real-time environmental monitoring for an **8-room smart office setup**. The system integrates **AWS IoT Core**, **Lambda**, **DynamoDB**, **S3**, **CloudFront**, and **Amazon Cognito**. Sensor data is forwarded from edge devices (or simulated scripts), ingested into AWS, stored in DynamoDB tables, and processed by Lambda functions to update the management dashboard. Critical events are routed through EventBridge for alerting, demonstrating a high-availability, low-cost, and seamless scalability architecture.

![overview](/images/5-Workshop/5.1-Workshop-overview/Smart-Office-Architect-Diagram.drawio.png)
