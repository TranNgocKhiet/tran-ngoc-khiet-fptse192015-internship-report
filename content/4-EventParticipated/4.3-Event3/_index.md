---
title: "Event 3"
weight: 3
chapter: false
pre: " <b> 4.3. </b> "
---

# Workshop Report: AWS Cloud Mastery Series #3 — Well-Architected Security Pillar

**Date:** Friday, November 29, 2025  
**Time:** 8:30 AM – 12:00 PM  
**Location:** Bitexco Financial Tower, Ho Chi Minh City  
**Host:** Kha Van  
**Attendees:** 355+ participants

## Overview

The third and final workshop in the AWS Cloud Mastery Series focused on cloud security through the lens of the AWS Well-Architected Framework's Security Pillar. The half-day session covered five key pillars: IAM, Detection, Infrastructure Protection, Data Protection, and Incident Response.

## Session Breakdown

### 8:30 – 8:50 AM | Opening & Security Foundations

The session began with an overview of the Security Pillar's role in well-architected design:

- **Core Principles:**
  - **Least Privilege:** Grant only necessary permissions
  - **Zero Trust:** Never trust, always verify
  - **Defense in Depth:** Multiple layers of security controls

- **Shared Responsibility Model:** AWS manages infrastructure security; customers manage application and data security

- **Top Threats in Vietnam:** Ransomware, credential compromise, exposed databases, insecure APIs

### 8:50 – 9:30 AM | Pillar 1: Identity & Access Management

#### Modern IAM Architecture

- **Users, Roles, Policies:** Fundamentals of AWS permission model
- **Avoiding Long-Term Credentials:** Service roles and temporary credentials
- **AWS IAM Identity Center:** Enterprise SSO and permission sets for multi-account deployments

#### Access Control at Scale

- **Service Control Policies (SCP):** Organization-wide guardrails preventing dangerous actions
- **Permission Boundaries:** Limiting maximum permissions for IAM users and roles
- **MFA Options:** TOTP (Time-based One-Time Password) vs. FIDO2 (hardware keys)

#### Continuous Validation

- **Access Analyzer:** Identifying overly permissive policies and external access
- **Credential Rotation:** Automating key rotation for programmatic access
- **Session Duration Limits:** Requiring re-authentication for sensitive operations

#### Mini Demo: IAM Policy Validation
- Creating a policy and simulating access
- Identifying permission gaps
- Using Access Analyzer to detect public access

### 9:30 – 9:55 AM | Pillar 2: Detection & Continuous Monitoring

#### Logging Infrastructure

- **CloudTrail (Organization-level):** All API calls across AWS accounts
- **GuardDuty:** Managed threat detection using machine learning
- **Security Hub:** Centralized security findings and compliance status

#### Logging at Every Layer

- **VPC Flow Logs:** Network traffic analysis (accepted and rejected connections)
- **ALB/Application Logs:** Request-level visibility
- **S3 Access Logs:** Object-level access tracking
- **Database Audit Logs:** Query and user activity

#### Alerting & Automation

- **EventBridge:** Route security events to Lambda, SNS, or SQS for automated response
- **CloudWatch Alarms:** Triggering alerts on specific log patterns
- **Detection-as-Code:** Version-controlling detection rules alongside infrastructure

### 9:55 – 10:10 AM | Coffee Break

### 10:10 – 10:40 AM | Pillar 3: Infrastructure Protection

#### Network Security

- **VPC Segmentation:** Private subnets for databases, public for load balancers
- **Security Groups vs. NACLs:** Stateful vs. stateless filtering
- **Application Models:** Tiered architecture with network isolation

#### Advanced Protection

- **AWS WAF (Web Application Firewall):** Protecting web applications from common attacks
- **AWS Shield:** DDoS protection (Standard automatic, Advanced for high-value applications)
- **AWS Network Firewall:** Centralized firewall for VPCs

#### Workload Security

- **EC2 Security:** Security groups, Systems Manager Session Manager (no SSH keys)
- **ECS/EKS Security:** Pod security policies, network policies, container scanning
- **Secrets in Transit:** mTLS, encrypted API endpoints

### 10:40 – 11:10 AM | Pillar 4: Data Protection

#### Encryption Strategy

- **At-Rest Encryption:**
  - S3: SSE-KMS with customer-managed keys
  - RDS: Transparent Data Encryption (TDE)
  - EBS: Encrypted volumes with custom KMS keys
  - DynamoDB: Encryption with AWS KMS

- **In-Transit Encryption:** HTTPS/TLS for all data movement

#### Key Management

- **AWS KMS:** Key policies, grants, automatic rotation
- **Separation of Duties:** Key administrator vs. key user roles
- **Key Rotation Strategy:** Balancing security with operational complexity

#### Secret Management

- **AWS Secrets Manager:** Database credentials, API keys, certificates
- **Parameter Store:** Configuration parameters (encrypted with KMS)
- **Rotation Patterns:** Lambda-based automatic rotation
- **Access Control:** IAM policies restricting which applications can access secrets

#### Data Classification

- **PII/Sensitive Data Identification:** Macie for automatic discovery
- **Access Guardrails:** Restricting access to sensitive data stores
- **Audit Trails:** Tracking who accessed what and when

### 11:10 – 11:40 AM | Pillar 5: Incident Response

#### IR Lifecycle (per AWS)

1. **Preparation:** Tooling, runbooks, team training
2. **Detection & Analysis:** Identifying and characterizing incidents
3. **Containment:** Stopping the attack and limiting damage
4. **Eradication:** Removing the attacker's presence
5. **Recovery:** Restoring systems to normal operations
6. **Post-Incident Review:** Learning from the incident

#### Incident Playbooks

**Scenario 1: Compromised IAM Key**
- Detection: GuardDuty alerts on unusual API calls
- Containment: Disable compromised credentials immediately
- Eradication: Rotate access keys, review CloudTrail for unauthorized actions
- Recovery: Verify no backdoors remain

**Scenario 2: S3 Bucket Publicly Exposed**
- Detection: CloudTrail shows bucket policy modified or object ACL changed
- Containment: Restrict public access immediately
- Eradication: Review who modified policies (audit trail)
- Recovery: Verify no sensitive data was accessed

**Scenario 3: EC2 Malware Detection**
- Detection: GuardDuty identifies suspicious EC2 behavior
- Containment: Isolate instance in security group, snapshot for forensics
- Eradication: Update OS/patch, rotate credentials
- Recovery: Redeploy clean instance from golden image

#### Automation & Tooling

- **Snapshot & Isolation:** Automatic snapshot creation and network isolation
- **Evidence Collection:** Preserving logs and data for post-mortem
- **Auto-Response:** Lambda functions triggering remediation (disable user, isolate instance)
- **Notification:** SNS alerts to security team and incident commander

### 11:40 – 12:00 PM | Wrap-Up & Q&A

#### Key Takeaways

- The five pillars are interconnected: strong IAM is useless without detection
- Vietnamese enterprises face real threats; preparation is essential
- AWS provides end-to-end tools; the barrier is process and culture

#### Learning Roadmap

- **AWS Security Fundamentals:** Introduction level
- **AWS Certified Security – Specialty:** Deep technical knowledge
- **AWS Solutions Architect Professional:** Architectural decision-making
- **Hands-on Practice:** CloudLabs, building test scenarios

#### Common Pitfalls in Vietnam

- Over-reliance on perimeter security (assumes internal trust)
- Storing secrets in code or configuration files
- Neglecting log retention and compliance requirements
- Manual incident response processes (slow and error-prone)

## Personal Reflections

### What I Learned

Security is not a single control—it's a system of overlapping defenses. AWS provides comprehensive tools, but success requires process discipline and cultural commitment to least privilege.

The incident response emphasis resonated strongly. Too many organizations prepare for zero-day exploits but fail to respond to compromised credentials (the most common attack vector). Well-documented playbooks and automated response are force multipliers.

### Key Insights

1. **Detection > Prevention:** Assume breach mentality—focus on detecting compromise quickly.
2. **Automation is critical:** Manual incident response is too slow; Lambda/Step Functions should handle routine responses.
3. **Logging is mandatory:** Without comprehensive logs, you cannot investigate or audit effectively.
4. **IAM is the foundation:** Every other control depends on solid identity and access management.
5. **Culture matters:** Technical controls fail without security-conscious teams and processes.

### Next Steps

- Audit current IAM permissions and identify over-privilege cases
- Enable GuardDuty and Security Hub for continuous threat detection
- Build incident response playbooks specific to our infrastructure
- Set up automated remediation for common security findings
- Implement encryption at-rest for all databases and S3 buckets

> This half-day security workshop provided a strategic overview of the AWS Well-Architected Security Pillar and practical incident response frameworks. The emphasis on automation, detection, and incident playbooks will directly improve our organization's security posture.

- Scale least-privilege access enforcement using AWS organizational policies and permission boundaries across multiple accounts
- Leverage AWS services (EventBridge, SNS, SQS) to build automated security alerting and response workflows
- Codify security detection rules and store them in version control to enable collaborative incident response

### Implementation Strategy

- Roll out MFA across all accounts and implement fine-grained least-privilege policies for all roles
- Deploy automated event routing and alerting to reduce security response time
- Version security rules as infrastructure code and use pull requests for changes to detection logic

### Takeaway

The security pillar sessions significantly strengthened my practical abilities in designing alerting systems, building automation, and responding to incidents. The presenters shared lessons from large-scale cloud deployments, highlighting common mistakes and proven remediation patterns.

> The workshop expanded my grasp of cloud security operations and incident response procedures; I now have concrete steps to enhance alerting pipelines, operational automation, and policy controls.
