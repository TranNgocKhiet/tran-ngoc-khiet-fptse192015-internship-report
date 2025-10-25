---
title: "Translated Blogs"
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

###  [Blog 1 - Jumpstart your cloud career with AWS SimuLearn](3.1-Blog1/)
The blog post “Jumpstart your cloud career with AWS SimuLearn” introduces AWS SimuLearn, an interactive learning platform that combines Generative AI with realistic customer simulations. It allows learners to build both technical and communication skills in a safe, feedback-driven environment, with training tailored by role or industry. Through the stories of Hetvi, Karishma, and Kattie, the post highlights how SimuLearn helps users strengthen customer engagement skills, deepen technical expertise, and gain industry-specific knowledge in areas like healthcare. With over 200 training modules and simulations, AWS SimuLearn empowers early-career cloud professionals to grow their AWS knowledge, boost confidence, and accelerate their cloud career readiness.

###  [Blog 2 - How to Set Up Automated Alerts for Newly Purchased AWS Savings Plans](3.2-Blog2/)
The blog post “How to Set Up Automated Alerts for Newly Purchased AWS Savings Plans” explains how to implement an automated monitoring and alerting system for newly purchased AWS Savings Plans with low utilization. The solution leverages AWS CloudFormation to create Step Functions, SNS topics, EventBridge schedulers, and necessary IAM roles. The deployment is split into two parts:
- Member Account: hosts a Step Function that checks Savings Plans purchased within the last 7 days and the current month, sending email alerts if utilization is below a defined threshold.
- Management Account: provides IAM roles and access so the Step Function can analyze Savings Plans across the organization.
Users can configure thresholds, scheduling frequency, and alert recipients. Upon receiving alerts, FinOps teams should review utilization data and consider returning underused Savings Plans if eligible. This solution helps FinOps teams proactively manage cloud costs, detect underutilized commitments, and improve overall Savings Plans utilization efficiency across AWS environments.

###  [Blog 3 - Operating BYOL Windows Server Workloads Effectively on AWS](3.3-Blog3/)
This AWS blog explains how to effectively operate Bring Your Own License (BYOL) Windows Server workloads on AWS to reduce costs. It covers eligibility requirements for BYOL licenses, preparing Windows Server images using VM Import/Export and Migration Hub Orchestrator, and managing license type conversions with AWS License Manager. The post also shows how to detect configuration issues using AWS Config custom rules and analyze cost data with AWS Cost and Usage Reports (CUR). By following these best practices, organizations can optimize Windows Server costs, ensure license compliance, and improve operational efficiency on AWS.
