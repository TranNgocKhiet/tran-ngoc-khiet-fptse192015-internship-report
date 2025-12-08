---
title: "Blog 3"
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---

# Introducing Just-in-time node access using AWS Systems Manager

by Chetan Makvana, Anthony Verleysen, and Mark Brealey | on 29 APR 2025 | in [Announcements](https://aws.amazon.com/blogs/mt/category/post-types/announcements/), [AWS Systems Manager](https://aws.amazon.com/blogs/mt/category/management-tools/aws-systems-manager/), [Management Tools](https://aws.amazon.com/blogs/mt/category/management-tools/), [Security](https://aws.amazon.com/blogs/mt/category/security-identity-compliance/security/) | [Permalink](https://aws.amazon.com/blogs/mt/introducing-just-in-time-node-access-using-aws-systems-manager/) | Share

Today, we're excited to announce the general availability of [just-in-time node access](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access.html), a new capability in [AWS Systems Manager](https://aws.amazon.com/systems-manager/). Just-in-time node access enables dynamic, time-bound access to [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/), on-premises, and multicloud nodes managed by AWS Systems Manager. It uses a policy-based approval process, allowing you to remove long-standing access while maintaining operational efficiency and enhancing security.

Organizations expanding their operations to thousands of nodes require identity driven granular permissions to support their audit and compliance objectives. They want to eliminate long term credentials entirely. The practice of using long-term credentials for node access creates security vulnerabilities, increasing the risk of unauthorized access and potential breaches.

Previously, customers faced a challenging trade-off between security and operational efficiency. Rather than carefully determining who needed access to specific resources, IT teams would grant excessive permissions to large groups of users. This practice created increased risk of accidental operator errors, and opportunity for bad actors, driven by the need for operational convenience. They either maintained long term credentials, which increased risk of compromised security, or implemented restrictive access controls that slowed incident response. Custom-built solutions proved complex to maintain and scale; whereas non-AWS tools using agents require identity and permissions to access nodes.

## Overview

Just-in-time node access helps you implement least-privilege access while ensuring operational teams can quickly respond to issues. It works seamlessly across your [AWS Organization](https://aws.amazon.com/organizations/), allowing you to set up consistent access controls whether you're managing a single account or multiple accounts. This new capability allows administrators to define precise access controls through approval policies that specify who can access which nodes and under what conditions. Organizations can choose between manual approval processes with multiple approvers or condition-based auto-approval policies, providing flexibility to match their security requirements.

For example, administrators can establish auto-approval policy to quickly provide on-call engineers access during incidents, granting access only to operators in an on-call [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) group. Through just-in-time node access, operators can request access to nodes when they need it. Based on pre-configured approval policies, they receive temporary access that automatically expire after a defined time window. Upon approval, they can directly access these nodes via a one-click browser-based shell, [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/) or Remote Desktop Protocol (RDP) supported by Systems Manager, without the need to open inbound ports or manage SSH keys.

To simplify the approval process, just-in-time node access integrates with tools like Slack and Microsoft Teams through [Amazon Q Developer](https://aws.amazon.com/q/developer/), and email to notify approvers of pending requests. Systems Manager also emits events to [Amazon EventBridge](https://aws.amazon.com/eventbridge/) for status updates to just-in-time node session access request. These events can be routed to [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/) for notifications or integrated with your internal systems, allowing your teams to track and respond to access requests through your existing workflows. This enables you to monitor access requests and maintain audit trails across your organization. Furthermore, just-in-time node access can provide additional visibility into operator activities by logging commands run during sessions and recording their actions during RDP sessions.

Systems Manager offers a free trial of just-in-time node access per account per Region, allowing you to fully explore and evaluate the feature for your organization. This trial period includes the remainder of the billing period in which you enable the feature, plus the entire next billing period. During this trial period, you'll have access to all capabilities, enabling you to test configurations and access policies without any additional charges. After the trial concludes, just-in-time node access becomes a paid service, with charges based on your usage patterns. For detailed pricing information and cost breakdowns, please refer to [AWS Systems Manager Pricing](https://aws.amazon.com/systems-manager/pricing/).

## Using Just-in-Time Node Access

When you implement just-in-time node access, you'll work with three distinct roles: Administrator, Operator, and Approver. Administrator establishes and maintains approval policies. Operator initiates access requests for specific nodes. And approver reviews and authorizes access requests.

Let's walk through how you can set up and use this feature, using a scenario where your on-call engineer needs access to a production system, specifically to an instance named 'r2d2-app-01' from the below fleet of instances as shown in figure 1.

![Amazon EC2 console showing list of EC2 instances](/images/blog-3/ec2-instances.png)

*Figure 1: Amazon EC2 console showing list of EC2 instances*

We will explore how an on-call engineer (Operator) can request access to production system, with the DevOps lead (Approver) managing the approval, all within the approval policy defined by the Administrator.

## Setting up Just-in-time node access as an Administrator

### Step 1 – Enabling Just-in-Time Node Access

In this walk-through, we are going to enable just-in-time node access for the AWS Organization. To get started, you must first set up the [Systems Manager unified console](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-organizations.html). Once the unified console is setup, you can then enable just-in-time node access in Systems Manager.

You can then choose which Organization Units (OUs) and AWS Regions to target for deployment. This lets you precisely control where the solution is implemented, whether across your entire organization or in specific areas as shown in figure 2.

![AWS System Manager console to enable just-in-time node access for Organizational Units and Regions](/images/blog-3/onboarding.png)

*Figure 2: Enable just-in-time node access*

### Step 2 – Creating approval policies

After enabling the feature, the next crucial step is creating approval policies. Approval policies determine how users gain access to nodes. These policies come in three types: auto-approval, manual approval, and deny-access policies. Auto-approval policy defines which nodes users can connect to automatically. Manual approval policy defines the number and levels of manual approvals that must be provided to access the nodes you specify. Deny-access policy explicitly prevents the auto-approval of access requests to the nodes you specify.

In our example, we will focus on creating a manual approval policy for nodes tagged with `Workload:Application01`, which includes our 'r2d2-app-01' node.

To create the policy, navigate to the [AWS Systems Manager console](https://console.aws.amazon.com/systems-manager/home), choose just-in-time node access in the navigation pane, select the Approval policies tab, and choose Create manual policy. The policy configuration requires several key components.

First, in the Approval policy details section, provide a name and description for the approval policy, along with setting the maximum access duration as shown in figure 3. This duration determines how long approved access remains valid before automatically expiring.

![Create manual approval policy page to enter Approval policy details](/images/blog-3/approval-policy-details-section.png)

*Figure 3: Manual approval policy page*

In the Targets section, use tag key-value pairs to define which nodes the policy applies to. For this example, we'll target nodes tagged with `Workload:Application01`, which includes our 'r2d2-app-01' node. This approach ensures the policy applies to all nodes associated with `Application01` as shown in figure 4.

![Specifying targets for a manual approval policy](/images/blog-3/manual-policy-targets.png)

*Figure 4: Manual approval policy targets*

In the Access request approvers section, you'll designate individuals or groups authorized to approve access requests. In our scenario, we'll assign the DevOps lead role as the approver. Access requests approvers can be IAM Identity Center users and groups or IAM users, groups, and roles as shown in figure 5.

![Create manual approval policy page to enter Access request approvals](/images/blog-3/access-requests-approvals.png)

*Figure 5: Access requests approval*

You can also define automated access rules using the [Cedar policy language](https://www.cedarpolicy.com/en), eliminating the need for manual approvals in trusted scenarios. Think of auto-approval policies as your organization's pre-approved access rulebook. These policies specify which nodes users can access automatically, based on predefined conditions and trust levels. For more information, see [Create an auto-approval policy for just-in-time node access](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-create-auto-approval-policies.html) and [Statement structure and built-in operators for auto-approval and deny-access policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/auto-approval-deny-access-policy-statement-structure.html).

For example, you can create an auto-approval policy that automatically allows members of the "DevOpsTeam" group to access nodes tagged with `Environment: Development` using the following Cedar policy:

```cedar
// Policy to permit access to Development nodes for members of the DevOpsTeam IDC group
permit (
    principal in AWS::IdentityStore::Group::"911b8590-7041-70fa-d20b-12345EXAMPLE",
    action == AWS::SSM::Action::"getTokenForInstanceAccess", 
    resource)
  when {
    resource.hasTag("Environment") && 
    resource.getTag("Environment") == "Development"
  };
```

## Requesting access as an Operator

When you need to access a protected node as an operator, you'll see a streamlined request process. Instead of immediate access, you'll be prompted to submit an access request when attempting to connect through Session Manager. You'll need to provide a justification for access as shown in figure 6.

![Operator raising a request to access the node](/images/blog-3/access-request-1.gif)

*Figure 6: Operator raising a request to access the node*

After submitting your request, you can monitor its status through the Access Requests tab as shown in figure 7. You'll be able to track your request through the approval process and know exactly when your access becomes available. You'll receive notifications via your preferred communication channel, whether that's email, Slack, Microsoft Teams, or another integrated platform. For more information, see [Configure notifications for just-in-time access requests](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-notifications.html).

![Just-in-time node access page showing list of access requests raised by operator](/images/blog-3/requests-for-me-page.png)

*Figure 7: List of access request page*

## Managing approvals

As an approver, you'll receive notifications of pending access requests through your configured notification channel. You can programmatically approve requests using the [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI), or your preferred [SDK](https://aws.amazon.com/developer/tools/). Or you can review these requests in the Systems Manager console under the Requests for me tab as shown in figure 8.

![Just-in-time node access page showing list of access requests pending for approval by the approver](/images/blog-3/requests-approval.png)

*Figure 8: List of access requests pending for approval*

After reviewing the request, you can either approve or reject the request and optionally add a comment related to the decision.

## Completing the access cycle

Once request is approved, as an operator, you receive notification that your access has been granted. You can then connect to the node using the AWS Management console or AWS CLI for the duration in the approval policy as shown in figure 9.

![Operator accessing the managed node](/images/blog-3/access-approval.gif)

*Figure 9: Operator accessing the managed node*

## Conclusion

In this blog, we introduced [just-in-time node access](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access.html), a new capability in AWS Systems Manager. Just-in-time node access solves the challenge of balancing operational efficiency with security requirements by eliminating standing privileges while ensuring swift access to Amazon EC2, on-premises, and multicloud nodes. Through its flexible policy-based approach, and support for both manual and automatic approvals, you can now implement zero standing privileges without compromising operational capabilities.

Systems Manager offers a free trial of just-in-time node access, allowing you to fully explore and evaluate the feature for your organization.

To learn more, see [Just-in-time node access using Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access.html) for more details.

Check out this [interactive demo](https://aws-cloudops.storylane.io/share/qazsu1mgqiho) for a full visual tour of the just-in-time node access experience.

## About the authors

![Chetan Makvana](/images/blog-3/Chetan-Makvana.jpeg)

### Chetan Makvana

Chetan Makvana is an Enterprise Solutions Architect at Amazon Web Services. He helps enterprise customers in designing scalable, resilient, secured and cost effective enterprise grade solution using AWS services. He is a technology enthusiast and a builder with a core area of interest on generative AI, serverless, app modernization and DevOps. Outside of work, he enjoys binge-watching, traveling and music.

![Anthony Verleysen](/images/blog-3/Anthony-Headshot.jpg)

### Anthony Verleysen

Anthony Verleysen is a Senior Product Manager - Technical within the AWS Systems Manager team. He is the the product manager for Patch Manager and Distributor. Outside of work, Anthony is an avid soccer and tennis player.

![Mark Brealey](/images/blog-3/brealeym.jpg)

### Mark Brealey

Mark Brealey is a Senior Migration Solutions Architect, he empowers partners to build robust, secure, and efficient cloud architectures. He specializes in designing scalable solutions that help organizations maximize their AWS infrastructure while ensuring operational excellence.
