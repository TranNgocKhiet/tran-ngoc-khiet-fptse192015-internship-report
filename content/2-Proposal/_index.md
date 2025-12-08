---
title: "Proposal"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# Smart Office Management Console
## A Unified AWS Serverless Solution for Real-Time Weather Monitoring

### 1. Executive Summary
The Smart Office Management Console is designed base on the idea of weekly trip to AWS office at Ho Chi Minh city. It supports office with smart device like auto light, auto scensor window, auto air conditioner by collect, transmit and process data from IoT Sensor. By utilizing AWS Serverless services, data can transmit via MQTT and process every 5 minutes to support real-time monitoring, acting base on predictive weather and saving cost from unused devicesm with restricted to athenticated members via Amazon Cognito

### 2. Problem Statement
#### What’s the Problem?
Nowadays, offices require manual control for light, window, air conditioner, .etc. Most office turn on light and air conditioner thoughout there work hour (usually 8 a.m to 5 p.m), but this 
may not be necessary. For example, sunlight at 8 a.m may not be bright enough for worker to see clearly, but if the office is not very big, sunlight from 10 a.m to 3.pm can support light up very much. Additionally, in rainy season, some places have high humidity which can provide a cool environment similar to air conditioner environment. If we can control devices base on these condition, it will save energy for the world as well as money for organization.

#### The Solution
The platform uses AWS IoT Core to ingest MQTT data, AWS Lambda and API Gateway for processing, DynamoDB for data storage, Amazon S3 for static website hosting and Amazon Cognito ensures secure access, AWS SNS to send notifications when system monitoring device or when supisious weather condition detect. Similar to Thingsboard and CoreIoT, users can register new devices and manage connections, though this platform operates on a smaller scale and is designed for private use. Key features include real-time monitoring, weather prediction, auto controlling and low operational costs.

#### Benefits and Return on Investment
The Smart Office system enhances automation, monitoring, and energy efficiency across office environments, providing a reliable platform for research, expansion, and real-world IoT application development. It serves as a foundational resource for lab members and developers to build advanced smart environment solutions, while offering a centralized system that reduces manual configuration, improves data reliability, and simplifies maintenance.

Monthly operating costs are estimated at $1.81 USD, including DynamoDB ($0.09), IoT Core ($0.18), CloudFront ($1.27), CloudWatch ($0.25) and SNS ($0.02), totaling $21.72 USD per year. As IoT hardware is already deployed, there are no additional equipment expenses. The system achieves a break-even period of 6–12 months through significant time savings and reduced manual operation, offering long-term scalability and cost efficiency.

### 3. Solution Architecture

The Smart Office system adopts a fully serverless AWS architecture optimized for cost efficiency and scalability. Data from multiple sensor hubs is transmitted to AWS IoT Core, processed by Lambda functions, and stored in DynamoDB for real-time monitoring and configuration management. EventBridge automates scheduled device actions and anomaly detection, while SNS handles system notifications. The web dashboard is hosted on S3 and delivered securely via CloudFront, with user authentication managed through Amazon Cognito. This architecture minimizes operational overhead and ensures high reliability for smart environment control.

![Smart Office Architecture](/images/2-Proposal/Smart-Office-Architect-Diagram.drawio.png)

#### AWS Services Used
- **AWS IoT Core**: Ingests and manages MQTT data from eight smart room hubs, enabling near real-time monitoring and automation. 
- **AWS Lambda**: Handles sensor data processing, configuration updates, and automation triggers (four primary functions). 
- **Amazon API Gateway**: Connects the web client to backend services through secure RESTful APIs. 
- **Amazon DynamoDB**: Stores user profiles, office and room configurations, and recent sensor logs for fast access. 
- **Amazon EventBridge**: Triggers scheduled automation events and anomaly detection workflows. 
- **Amazon SNS**: Delivers alerts and notifications when anomalies or threshold events occur. 
- **Amazon S3**: Hosts the web dashboard and static assets for the Smart Office application. 
- **Amazon CloudFront**: Distributes the web dashboard globally with secure HTTPS access and low latency. 
- **Amazon Cognito**: Manages authentication and authorization for users interacting with the system. 
- **Amazon CloudWatch**: Monitors metrics and stores operational logs for debugging and performance optimization.

#### Component Design
- **Sensor Hubs**: Each IoT-enabled room device collects environmental data (temperature, humidity, light, etc.) and sends it to **AWS IoT Core** every two minutes. 
- **Data Ingestion**: **AWS IoT Core** routes incoming MQTT messages to the **SensorProcessor Lambda**, which validates and logs the data into **Amazon DynamoDB**. 
- **Configuration Management**: The **RoomConfigHandler Lambda** updates room settings (auto/manual modes, thresholds, timers) in DynamoDB when users make changes through the dashboard. 
- **Automation Control**: **AutomationSetup Lambda** listens to **DynamoDB Streams** for configuration updates and registers automation events in **Amazon EventBridge**. 
- **Event Handling**: **EventBridge** triggers **AutomationHandler Lambda** at scheduled times or when anomalies are detected, sending alerts via **Amazon SNS** if needed. 
- **User Interaction**: The **web dashboard** (hosted on **Amazon S3** and delivered via **CloudFront**) allows users to view sensor data and manage configurations. 
- **User Authentication**: **Amazon Cognito** secures user access with sign-up, sign-in, and token-based authorization integrated through **API Gateway**. 
- **Monitoring & Reliability**: **Amazon CloudWatch** collects logs and metrics from all Lambda functions, with **SQS** queues as DLQs to capture failed executions for debugging.

### 4. Technical Implementation
**Implementation Phases**
- Build Theory and Research AWS Services: Study core AWS components (IoT Core, Lambda, S3, API Gateway, EventBridge, CloudFront, Cognito) and learn their integration for IoT data handling and automation (7 weeks).
- Design Architecture and Estimate Costs: Create the serverless architecture diagram for an 8-room smart office and use the AWS Pricing Calculator to forecast monthly expenses (1 week).
- Develop and Optimize Solution: Implement scripts that simulate IoT sensor data to send to AWS IoT Core, build Lambda functions for automation and anomaly detection, and connect the web dashboard with API Gateway and DynamoDB (3 weeks).
- Testing and Deployment: Deploy all AWS services, test system reliability and rule triggers, validate message flows from IoT Core through EventBridge and Lambda, and monitor real-time results on the hosted dashboard (1 week).

**Technical Requirements**
- Sensor Hub Network: Each room includes a Sensor Hub with temperature, humidity, and light sensors, controlled by an ESP32 or similar microcontroller. Hubs send sensor data every 2 minutes via MQTT to AWS IoT Core when in auto mode.
- Smart Office Platform: Implements a serverless AWS architecture using AWS IoT Core (data ingestion and rule engine), AWS Lambda (data processing and automation logic), Amazon DynamoDB (device configuration and user data), Amazon S3 (web hosting), Amazon API Gateway (REST API), Amazon EventBridge (scheduled automation and anomaly detection), Amazon SNS (notifications), Amazon CloudFront (content delivery), and Amazon Cognito (user authentication).
- Deployment and Tools: All services are provisioned via AWS CDK/SDK. The web dashboard, built with Next.js and hosted on S3 + CloudFront, allows configuration, real-time monitoring, and automation scheduling while minimizing backend Lambda execution time.

### 5. Timeline & Milestones
**Project Timeline**
- Weeks 1–7: Study and research AWS services including IoT Core, Lambda, DynamoDB, S3, API Gateway, and Cognito.
- Week 8: Design the full architecture and estimate costs using the AWS Pricing Calculator.
- Weeks 9–11: Develop and integrate all system components — data simulation scripts, Lambda functions, database setup, and web dashboard.
- Week 12: Test, debug, and deploy the system to production.

### 6. Budget Estimation
You can find the budget estimation on the [AWS Pricing Calculator](https://calculator.aws/#/estimate?id=0db12150c448b012356e475becefd549c37094d8).  
Or you can download the [Budget Estimation File](/file/proposal/smart_office_pricing_caculator.pdf).

### Infrastructure Costs
AWS Services:
- Amazon DynamoDB: Free (0.00208 GB/month)
- AWS Lambda: Free (119,000 requests/month, 13,386.25 GB/s)
- AWS IoT Core: $0.18/month (8 devices, 13,000 messages/month)
- AWS API Gateway: Free (720 requests/month)
- Amazon Simple Storage Service (S3): Free (0.01 GB)
- Amazon CloudFront: $1.27/month (10,000 requests/month)
- Amazon EventBridge: Free (2600 events/month)
- Amazon Simple Queue Service (SQS): Free (2600 requests/month)
- Amazon CloudWatch: $0.25/month (0,3612736 GB/month) (set retention 3 days)
- Amazon Amazon Simple Notification Service (SNS): $0.02/month (2100 requests/month, 2100 emails/month)
- Amazon Cognito: Free (3 MAU/month)
Hardware: Existing smart office sensors and hubs — no additional cost.
Total: ≈ $1.81/month, or $21.72/year (within AWS Free Tier limits).

### 7. Risk Assessment
#### Risk Matrix
- IoT Connectivity Issues: Medium impact, medium probability.
- Sensor Hub Malfunction: High impact, low probability.
- Unexpected AWS Charges: Medium impact, low probability.
- Data Inconsistency or Delay: Medium impact, medium probability.

#### Mitigation Strategies
- Connectivity: Implement message buffering at Sensor Hub; retry on reconnect.
- Hardware: Keep spare hubs and perform periodic health checks.
- Cost: Use AWS Budgets and Cost Explorer to monitor spending within Free Tier.
- Data Reliability: Validate incoming IoT data via Lambda before storing in DynamoDB.

#### Contingency Plans
- Switch to manual operation if IoT service disruption occurs.
- Enable CloudWatch alerts for early issue detection.
- Use AWS CloudFormation or CDK rollback for quick recovery and cost control.

### 8. Expected Outcomes
#### Technical Improvements:
- Real-time monitoring and automation replace manual room control.
- Centralized platform enhances data accuracy and consistency.
- Scalable architecture supports future expansion to more rooms or other IoT devices.
  
#### Long-term Value:
- Provides a reusable foundation for smart building and IoT automation research.
- Enables data-driven insights for energy efficiency and environmental optimization.
- Demonstrates a fully serverless, low-cost AWS architecture (under $2/month).

## Proposal Link

[Smart_Office_Proposal](/file/proposal/Smart_Office_Proposal.docx)