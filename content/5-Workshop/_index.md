---
title: "Workshop"
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Smart Office Management System Workshop

#### Overview

**Smart Office Management System** provides a real-time environmental monitoring and management solution for offices, built entirely on **AWS Serverless** architecture to optimize costs and scalability.

In this lab, you will learn how to deploy, configure, and test a full-stack IoT system, allowing sensor devices to transmit data to the cloud and enabling administrators to control devices via a Web Dashboard.

You will work with two main architectural models to operate the Smart Office system:
+ **Serverless Architecture** - Uses **AWS Lambda**, **API Gateway**, and **DynamoDB** to handle logic and data storage. This model allows code to run in response to requests without managing servers.
+ **Event-Driven Architecture** - Uses **AWS IoT Core**, **EventBridge**, and **SNS**. The system operates based on events, where data from sensors or user actions trigger automation workflows and send alert notifications.

#### Content

1. [Workshop overview](5.1-Workshop-overview/)
2. [Prerequisite](5.2-Prerequiste/)
3. [Run CloudFormation Stack](5.3-Run-cloudformation-stack/)
4. [Set up website](5.4-Set-up-website/)
5. [Event Bridge](5.5-Event-Bridge/)
6. [SNS](5.6-SNS/)
7. [Test website IoT connection](5.7-Test-website-iot-connection/)