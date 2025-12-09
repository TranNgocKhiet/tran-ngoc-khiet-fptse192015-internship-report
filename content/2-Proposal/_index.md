---
title: "Proposal"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# Smart Office Management System for Lab Research
## A Unified AWS Serverless Solution for Real-Time Monitoring & Administration

### 1. Executive Summary
The Smart Office Management System is proposed by Team **Skyscraper** from **FPTU HCM Campus**, inspired by the operational excellence observed during a field trip to the AWS office in Ho Chi Minh City. Traditional office management lacks real-time visibility into room conditions (temperature, humidity, light) and relies heavily on manual oversight. To address this, we propose a centralized **Management Console** built on a fully **AWS Serverless architecture**. By leveraging services like AWS IoT Core, Lambda, and DynamoDB, the system collects sensor data every 2-5 minutes to support real-time monitoring and allows administrators to manage device configurations remotely. This project also serves as a strategic "First Cloud AI Journey", enabling the team to bridge the gap between theoretical knowledge and practical application of Cloud Computing.

### 2. Problem Statement
#### What’s the Problem?
Nowadays, managing office environments in research labs requires manual intervention to check device statuses (lights, air conditioners) and environmental conditions. Managers often lack the data needed to make informed decisions about energy usage or room comfort. Operating devices on fixed schedules (e.g., 8 a.m. to 5 p.m.) without regarding actual room usage or environmental factors leads to energy waste. Furthermore, without a centralized dashboard, administrators cannot quickly detect anomalies or configure settings for multiple rooms efficiently.

#### The Solution
The platform uses **AWS IoT Core** to ingest MQTT data from room sensors, **AWS Lambda** and **API Gateway** for backend logic and processing, **Amazon DynamoDB** for storing sensor logs and room configurations, and **Amazon S3** combined with **CloudFront** to host the web management dashboard. Access is strictly secured via **Amazon Cognito**. **Amazon EventBridge** is utilized to handle scheduled automation tasks, while **Amazon SNS** ensures timely notifications for system alerts. This solution replaces manual tracking with a digital, real-time management console capable of monitoring multiple rooms simultaneously.

#### Benefits and Return on Investment
The Smart Office Management System enhances operational efficiency by providing a single pane of glass for monitoring and configuration. It empowers lab managers to control devices remotely and make data-driven decisions. Beyond operational improvements, the project provides a reusable serverless foundation for future IoT research at the university.

Monthly operating costs are estimated at **$1.81 USD**, utilizing the AWS Free Tier for services like Lambda, API Gateway, and DynamoDB. Major costs include CloudFront ($1.27) and CloudWatch ($0.25), totaling approximately **$21.72 USD per year**. Since the system leverages existing ESP32 hardware and sensors, there are no additional capital expenditures. The system offers immediate value through time savings and reduced management effort.

### 3. Solution Architecture
The Smart Office system adopts a fully serverless AWS architecture optimized for cost efficiency and scalability. Data from multiple sensor hubs is transmitted to AWS IoT Core, processed by Lambda functions, and stored in DynamoDB for real-time monitoring and configuration management. EventBridge automates scheduled device actions, while SNS handles system notifications. The web dashboard is hosted on S3 and delivered securely via CloudFront, with user authentication managed through Amazon Cognito. This architecture minimizes operational overhead and ensures high reliability for smart environment control.

![Smart Office Architecture](/images/2-Proposal/Smart-Office-Architect-Diagram.drawio.png)

#### AWS Services Used
- **AWS IoT Core**: Ingests and manages MQTT data from smart room hubs, enabling secure communication between edge devices and the cloud.
- **AWS Lambda**: Executes backend logic for processing sensor telemetry, handling API requests, and executing management commands (Serverless Compute).
- **Amazon API Gateway**: Exposes secure RESTful endpoints for the web dashboard to interact with the backend services.
- **Amazon DynamoDB**: Provides fast, NoSQL storage for room configurations, device states, and historical sensor logs.
- **Amazon EventBridge**: Orchestrates event-driven workflows, such as scheduled configuration updates or heartbeat checks.
- **Amazon SNS**: Sends email notifications to administrators regarding system alerts or critical updates.
- **Amazon S3**: Hosts the frontend static assets (HTML, CSS, JS) for the Management Dashboard.
- **Amazon CloudFront**: Delivers the web application globally with low latency and SSL security.
- **Amazon Cognito**: Manages user identity, authentication, and access control for the Management Console.
- **Amazon CloudWatch**: Collects logs and metrics to monitor system health and debug Lambda executions.

#### Component Design
- **Sensor Hubs**: IoT-enabled devices (ESP32) in each room collect telemetry (temperature, humidity, light) and transmit it to **AWS IoT Core** every few minutes.
- **Data Ingestion**: **AWS IoT Core** rules trigger the **HandleTelemetry Lambda**, which validates data and persists it to **Amazon DynamoDB**.
- **Configuration Management**: Administrators use the dashboard to update room settings. The **RoomConfigHandler Lambda** updates DynamoDB and pushes changes to devices via IoT Core Shadows or MQTT.
- **User Interaction**: The **Next.js Web Dashboard** (on **S3/CloudFront**) visualizes real-time data and provides a control interface.
- **User Authentication**: **Amazon Cognito** ensures only authorized lab members can log in and access sensitive room data.
- **Monitoring & Reliability**: **Amazon CloudWatch** tracks system performance, ensuring high availability and rapid troubleshooting.

### 4. Technical Implementation
**Implementation Phases**
- **Research & Foundation (Weeks 1-7)**: Study core AWS services (IoT Core, Lambda, DynamoDB, S3, API Gateway, Cognito) and understand Serverless design patterns.
- **Architecture Design & Estimation (Week 8)**: Finalize the solution diagram for an 8-room setup and use the AWS Pricing Calculator to forecast the budget.
- **Development (Weeks 9-11)**:
    - Implement firmware/scripts for IoT data simulation.
    - Develop Backend: Lambda functions, DynamoDB tables, and API Gateway resources using CloudFormation/CDK.
    - Develop Frontend: Build the Management Dashboard and integrate with APIs.
- **Testing & Deployment (Week 12)**: Perform end-to-end testing, validate data flow from sensors to the dashboard, and deploy the system to the production environment.

**Technical Requirements**
- **Hardware Layer**: ESP32-based Sensor Hubs monitoring environmental metrics.
- **Cloud Layer**: A fully serverless stack on AWS (IoT Core, Lambda, DynamoDB, API Gateway, S3, CloudFront, Cognito, EventBridge, SNS).
- **DevOps**: Infrastructure as Code (IaC) using AWS CloudFormation for reproducible deployments.
- **Interface**: A responsive web dashboard allowing real-time monitoring and configuration updates.

### 5. Timeline & Milestones
**Project Timeline**
- **Weeks 1–7**: Deep dive into AWS services and complete "First Cloud AI Journey" fundamental training.
- **Week 8**: Design the system architecture and finalize cost estimation.
- **Weeks 9–11**: Core development phase (Backend logic, Database schema, Frontend UI integration).
- **Week 12**: System integration testing, debugging, and final Go-Live presentation.

### 6. Budget Estimation
You can find the budget estimation on the [AWS Pricing Calculator](https://calculator.aws/#/estimate?id=0db12150c448b012356e475becefd549c37094d8).  
Or you can download the [Budget Estimation File](/file/proposal/smart_office_pricing_caculator.pdf).

### Infrastructure Costs
**AWS Services:**
- **Amazon DynamoDB**: Free (Always Free Tier: 25GB Storage).
- **AWS Lambda**: Free (Always Free Tier: 1M requests/month).
- **AWS IoT Core**: $0.18/month (8 devices, sending data every 2 mins).
- **Amazon API Gateway**: Free (Free Tier: 1M calls/month for 12 months).
- **Amazon S3**: Free (Standard storage < 5GB).
- **Amazon CloudFront**: $1.27/month (Based on est. data transfer and requests).
- **Amazon EventBridge**: Free (Free Tier events).
- **Amazon SNS**: $0.02/month (Email notifications).
- **Amazon CloudWatch**: $0.25/month (Log ingestion and storage).
- **Amazon Cognito**: Free (Free Tier: 50,000 MAUs).

**Hardware:** Mock script
**Total:** ≈ **$1.81/month**, or **$21.72/year** (optimized within AWS Free Tier).

### 7. Risk Assessment
#### Risk Matrix
- **IoT Connectivity Issues**: Medium impact, medium probability.
- **Sensor Data Inaccuracy**: Medium impact, low probability.
- **Unexpected AWS Charges**: Low impact, low probability (due to strict budget alerts).
- **Security Misconfiguration**: High impact, low probability.

#### Mitigation Strategies
- **Connectivity**: Implement retry logic on edge devices and local buffering.
- **Cost**: Configure AWS Budgets to alert when spending exceeds $1.00.
- **Security**: Enforce strict IAM policies (Least Privilege) and require authentication for all API access via Cognito.
- **Reliability**: Use CloudWatch Logs to trace errors in Lambda execution immediately.

#### Contingency Plans
- Enable manual override controls if the cloud system becomes unavailable.
- Maintain a backup of the CloudFormation templates for rapid redeployment.

### 8. Expected Outcomes
#### Technical Improvements:
- Replaces manual checks with **real-time digital monitoring**.
- Provides a **centralized platform** for managing configurations across multiple rooms.
- Establishes a **scalable architecture** capable of supporting more devices in the future.

#### Long-term Value:
- Serves as a practical **learning hub** for students to master AWS Serverless technologies.
- Provides data insights that can lead to better energy usage policies in the lab.
- Demonstrates a cost-effective, production-ready cloud solution.

## Proposal Link

[Smart_Office_Proposal](/file/proposal/Smart_Office_Proposal.docx)