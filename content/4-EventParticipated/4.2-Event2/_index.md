---
title: "Event 2"
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---

# Workshop Report: AWS Cloud Mastery Series #2 — DevOps on AWS

**Date:** Monday, November 17, 2025  
**Time:** 8:30 AM – 5:00 PM  
**Location:** Bitexco Financial Tower, Ho Chi Minh City  
**Host:** Kha Van  
**Attendees:** 316 participants

## Overview

The second workshop in the AWS Cloud Mastery Series delivered a comprehensive, full-day deep dive into DevOps practices on AWS. The session spanned CI/CD automation, infrastructure-as-code, containerization, and monitoring, with live demonstrations and real-world case studies.

## Morning Session: Culture & CI/CD Pipeline (8:30 AM – 12:00 PM)

### 8:30 – 9:00 AM | Welcome & DevOps Mindset

The session began with a recap of the previous AI/ML workshop and introduced DevOps culture and principles. Key metrics discussed:
- **DORA Metrics:** Deployment frequency, lead time, mean time to recovery (MTTR), change failure rate
- **DevOps Benefits:** Faster delivery, reduced risk, improved team collaboration

### 9:00 – 10:30 AM | AWS DevOps Services – CI/CD Pipeline

A comprehensive walkthrough of the AWS CodePipeline ecosystem:

#### Source Control
- **AWS CodeCommit:** Native Git repositories with IAM integration
- **Git Strategies:** GitFlow vs. Trunk-based development (tradeoffs and when to use each)

#### Build & Test
- **CodeBuild Configuration:** Docker-based build environments, caching, artifact management
- **Testing Pipelines:** Unit tests, integration tests, and security scanning

#### Deployment
- **CodeDeploy Strategies:**
  - **Blue/Green:** Zero-downtime deployments with instant rollback
  - **Canary:** Gradual rollout to a percentage of traffic
  - **Rolling:** Sequential instance updates
- **Target Instances:** EC2, On-premises, Lambda

#### Orchestration
- **CodePipeline Automation:** Connecting source → build → deploy stages
- **Approval Gates:** Manual review steps for production deployments

#### Live Demo
A full CI/CD pipeline walkthrough, showing:
1. Code commit triggering CodeBuild
2. Automated tests running and reporting
3. Artifact storage in S3
4. CodeDeploy executing blue/green deployment
5. Automatic rollback on failed health checks

### 10:30 – 10:45 AM | Break

### 10:45 AM – 12:00 PM | Infrastructure as Code (IaC)

Two dominant IaC approaches on AWS were compared:

#### AWS CloudFormation
- **Templates & Stacks:** JSON/YAML templates defining complete environments
- **Drift Detection:** Monitoring infrastructure changes outside CloudFormation
- **Stack Policies:** Preventing accidental updates to critical resources

#### AWS CDK (Cloud Development Kit)
- **Constructs:** Reusable, composable infrastructure building blocks
- **Language Support:** TypeScript, Python, Java, .NET
- **Higher Abstraction:** Write infrastructure like application code

#### Comparison & Selection
- CloudFormation: Lower-level control, JSON/YAML syntax, mature ecosystem
- CDK: Higher productivity, familiar programming languages, abstraction

#### Live Demo
Deploying infrastructure using both CloudFormation and CDK, highlighting:
1. CloudFormation template structure and parameters
2. CDK construct hierarchy and reuse
3. Deployment timings and rollback behavior

## Afternoon Session: Containers & Observability (1:00 PM – 5:00 PM)

### 1:00 – 2:30 PM | Container Services on AWS

#### Docker Fundamentals
- **Microservices & Containerization:** Breaking monoliths, independent scaling
- **Image Layering:** Optimizing image size and build cache

#### Amazon ECR (Elastic Container Registry)
- **Image Storage & Scanning:** Vulnerability detection for container images
- **Lifecycle Policies:** Automatic cleanup of old or unused images
- **IAM Integration:** Fine-grained access to registries

#### Amazon ECS vs. EKS
- **ECS:** Simpler orchestration, AWS-native, lower learning curve
- **EKS:** Kubernetes compatibility, multi-cloud options, richer ecosystem
- **Deployment Strategies:** Task placement, auto-scaling, service discovery

#### AWS App Runner
- **Simplified Container Deployment:** No cluster management required
- **Ideal for:** Stateless web applications, APIs, microservices
- **Automatic Scaling:** Based on traffic or custom metrics

#### Demo & Case Study
A microservices deployment comparing:
1. ECS deployment with task definitions and services
2. EKS deployment with pod manifests and operators
3. App Runner deployment for a simple REST API
4. Auto-scaling behavior under load

### 2:30 – 2:45 PM | Break

### 2:45 – 4:00 PM | Monitoring & Observability

#### CloudWatch
- **Metrics & Logs:** Centralized collection from AWS services
- **Alarms & Dashboards:** Real-time visualization and alerting
- **Log Insights:** Query logs with SQL-like syntax

#### AWS X-Ray
- **Distributed Tracing:** Track requests across microservices
- **Service Map:** Visual representation of application architecture
- **Performance Insights:** Identify bottlenecks and latency contributors

#### Full-Stack Observability Setup
- Integrating CloudWatch, X-Ray, and application logs
- Correlation IDs for tracking requests end-to-end
- Setting appropriate alarm thresholds (avoiding alert fatigue)

#### Best Practices
- **Alerting:** Alert on symptoms (latency, error rates) not just raw metrics
- **Dashboards:** Task-specific dashboards for oncall engineers
- **On-Call Processes:** Escalation policies, runbooks, incident postmortems

#### Demo
Building a complete observability solution:
1. CloudWatch agent collecting metrics from EC2 instances
2. Application logs flowing to CloudWatch Logs
3. X-Ray tracing a multi-tier application
4. Creating dashboards and alarms for key metrics

### 4:00 – 4:45 PM | DevOps Best Practices & Case Studies

#### Deployment Strategies
- **Feature Flags:** Decoupling deployment from release
- **A/B Testing:** Experimentation with subsets of traffic
- **Dark Launches:** Running new infrastructure in parallel

#### Automated Testing & CI/CD Integration
- **Test Pyramid:** Unit, integration, and end-to-end tests
- **Test as Code:** Keeping tests in version control
- **Performance Testing:** Catching regressions before production

#### Incident Management
- **Postmortems:** Blameless reviews focusing on system improvements
- **Runbooks:** Documented procedures for common incidents
- **On-Call Rotation:** Fair distribution and escalation policies

#### Real-World Case Studies
- **Startup:** From monolith to microservices, scaling from 10 to 1M users
- **Enterprise:** Legacy system modernization while maintaining 99.99% uptime

### 4:45 – 5:00 PM | Q&A & Wrap-up

**DevOps Career Pathways:** AWS certification roadmap (Developer Associate, Solutions Architect Pro, DevOps Professional)

## Personal Reflections

### What I Learned

The breadth of the AWS DevOps ecosystem became clear—there's a purpose-built service for each stage of the deployment pipeline. Rather than gluing together disparate tools, DevOps teams on AWS benefit from deep integration.

The contrast between ECS and EKS highlighted a key decision: simplified management vs. portability. For most use cases, ECS suffices; Kubernetes complexity pays off only when multi-cloud or complex orchestration is required.

### Key Insights

1. **Automation is non-negotiable:** Manual deployments are error-prone and slow; CI/CD is table stakes.
2. **Observability beats monitoring:** Recording what happened (logs/traces) is more valuable than just metrics.
3. **Infrastructure as Code is mandatory:** Version-controlled, reviewable infrastructure reduces operational risk.
4. **DevOps is a culture, not a job title:** Success requires collaboration between developers, ops, and security.
5. **Pick the right tool:** ECS for simplicity, EKS for portability, App Runner for ease-of-use.

### Next Steps

- Set up a basic CI/CD pipeline using CodePipeline for my team's projects
- Migrate an application to containers and deploy via ECS
- Implement CloudWatch dashboards and X-Ray tracing for existing services
- Design infrastructure templates using CDK for reproducible deployments

## Some pictures from the event

![event-picture-1](/images/event-2/IMG_20251117_121134%20(2).jpg)

> This full-day workshop equipped me with practical DevOps knowledge and demonstrated that AWS provides end-to-end solutions for the entire deployment lifecycle. The emphasis on automation, observability, and culture resonates across all team sizes.
