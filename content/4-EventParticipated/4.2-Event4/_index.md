---
title: "Event 4"
weight: 4
chapter: false
pre: " <b> 4.4. </b> "
---

# Summary Report: "AWS Cloud Mastery Series #3: ​Theo AWS Well-Architected Security Pillar"

### Event Objectives

- Security Foundation
- Identity & Access Management
- Detection
- Infrastructure Protection
- Data Protection
- Incident Response

### Speakers

- Le Vu Xuan An
- Tran Duc Anh
- Tran Doan Cong Ly
- Danh Hoang Hieu Nghi
- Thinh Lam
- Viet Nguyen
- Mendel Branski (Long)

### Key Highlights

#### Introduce to Cloud Club

- Introduce some Cloud Club at university like UTE, SGU
- Activities at Cloud Club

#### Security Foundation

- Service Control Policies
- Permission Bondaries
- Multi-Factor Authentication (MFA)

#### Detection and monitoring

- Multi-Layer Security Visibility
- Alerting & Automation with EventBridge
- Detection-as-code

#### Network and data protection

- VPC Security Group Sharing 
- API-Based Services
- Secret Management

#### Incident response

- Prevention - Nobody has time for incidents
- Guide to sleeping better
- Incident response process

### Key Takeaways

#### Service Control Policies

- Organizational policy
- Control maximum available permissions for all account in the organization
- Never grant permissions, it can only filtered

#### Permission Boundaries

- Advanced IAM feature designed to solve the sole central security problem
- Sets the maximum permissions that identity-based policy can grant to an User/Role

#### Multi-Factor Authentication (MFA)

- TOTP: Shared secret, requires manually 6-digits code (Google Authenticator), free, flexible backups and recovey
- FIDO2: Public-key cryptography, requires a simple touch biometric scan, variable, strict backups and recovey

#### Alerting & Automation with EventBridge

- Real-time Events: CloudTrail events flow to EventBrige for immediate processing
- Automated Alerting: Detect suspicious activities across all organization accounts
- Cross-account Event Routing: Centralized event processing and automated response
- Itegration & Workflows: SNS, Stack, SQS integration for automated security response and team notifications
  
#### Detection-as-Code

- CloudFormation/Terraform: Deploy GuardDuty across organization with IaC (enable protection plans, configure data sources)
- Custom Detection Rules: Build suppression rules & IP whitelists to reduce false positives and adapt to your environment
- Infrastructure-as-Code: Automated org-wide GuardDuty setup and protection plan rollout
- Version-Controlled Logic: Track detection rules in Git to DevSecOps pipeline integration for rule testing & deployment

#### Incident response

- Prepare automation handler for incident
- Predict future incident and design plan for response
- Lesson learned after each incidents

### Applying to Work

- Specify least privilege policy for project
- Apply MFA for every accounts
- Predict and prepare for future incident

### Event Experience

Attending the **“​Theo AWS Well-Architected Security Pillar”** workshop helps me improve my knowleagde in security and incident response through experiencing AWS Security Pillars, include:

#### Learn from skilfully speaker

- Learn how senior handle when incident happen and lesson learned after
- Learn to protect data and network with AWS security features

#### Explore some Cloud Club activites

- Introduce to Cloud Club activities thats help connect AWS Learner from everywhere

#### Alerting & Automation

- Prepare infrastructure like CloudTrail, EventBrigde, CloudWatch to manage resource in real-time as soon as incident occure

#### Some event photos

![piture_1](/images/event-4/3a8ff2ca-21b1-490b-a3e0-4c7bafeb2ac0.jpeg)
![piture_2](/images/event-4/8eb6febb-c015-41a3-a1c8-16a78d59edd6.jpeg)
![piture_3](/images/event-4/22b0e28c-748a-4ad9-a5ac-3a9373cece83.jpeg)
![piture_4](/images/event-4/41d9c737-718c-4eb5-992d-b979aaa30981.jpeg)
![piture_5](/images/event-4/63ce99ec-ac4f-4646-a3af-46a268cd3f64.jpeg)
![piture_6](/images/event-4/404da2be-4353-4261-9287-b6d91a7efe4c.jpeg)
![piture_7](/images/event-4/725ceae7-e342-4d73-88cd-fd5793f9ec5b.jpeg)
![piture_8](/images/event-4/17644578-8cd2-43f6-918f-9848b3d44951.jpeg)
![piture_9](/images/event-4/20407698-bdd4-42c7-8f33-85bed8ed02a2.jpeg)
![piture_10](/images/event-4/a1363d36-e3e5-48c2-b76b-07ec826900e3.jpeg)
![piture_11](/images/event-4/c2edcc1b-1c59-45c6-94c6-d078d337ecd1.jpeg)
![piture_12](/images/event-4/c72d08c9-5928-4f03-ae1a-aed17e9401ab.jpeg)
![piture_13](/images/event-4/de53e0de-10f7-479e-a2e7-54fc47928e9c.jpeg)
![piture_14](/images/event-4/e0c65198-929e-4a94-aaab-7e6e51364085.jpeg)
![piture_15](/images/event-4/e17e281a-6baf-4746-808e-26cc8504eadb.jpeg)
![piture_16](/images/event-4/ec3a8649-cc3e-43e3-a9ea-2673dd8acb27.jpeg)
![piture_17](/images/event-4/fedc1cf4-6796-41d5-98ee-9e51f19fc28c.jpeg)

> The event is a chance for me to expand my knowledge in Alerting, Automation, Security and Incident Response. I have gained a lot of experience through listening to senior Cloud Engineer talking about there work.
