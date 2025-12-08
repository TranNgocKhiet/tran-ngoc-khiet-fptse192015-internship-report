---
title: "Workshop"
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Serverless Smart Office IoT Platform

#### Overview

This workshop demonstrates how to build a **comprehensive serverless data platform** on AWS for real-time environmental monitoring. The system implements a modern **event-driven and serverless architecture** utilizing cloud-native AWS services.

**Key Architecture Principles:**
+ **Serverless Architecture** - Uses **AWS Lambda**, **Amazon API Gateway**, and **Amazon DynamoDB** to run code without provisioning servers. AWS automatically handles scaling and infrastructure management.
+ **Event-Driven Architecture** - Instead of continuous polling, specific events (IoT sensor readings, user API calls) trigger workflows. **AWS IoT Core** and **Amazon EventBridge** orchestrate these events for flexibility and scalability.

**System Components:**
The platform manages an **smart office setup** that integrates **AWS IoT Core** for sensor data ingestion, **Lambda** functions for processing, **DynamoDB** for storage, **S3** and **CloudFront** for website hosting, and **Amazon Cognito** for authentication. Sensor data flows from edge devices into AWS, gets stored and processed, updates the management dashboard, and routes critical events through EventBridge for alerting.

#### Content

1. [Workshop overview](5.1-Workshop-overview/)
2. [Prerequisites](5.2-Prerequiste/)
3. [Run CloudFormation stack](5.3-Run-cloudformation-stack/)
4. [Set up website](5.4-Set-up-website/)
5. [EventBridge and Lambda Setup](5.5-Event-Bridge/)
6. [SNS Setup](5.6-SNS/)
7. [Test website and IoT connection](5.7-Test-website-iot-connection/)