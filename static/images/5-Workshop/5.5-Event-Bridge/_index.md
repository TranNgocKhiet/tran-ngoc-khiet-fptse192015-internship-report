---
title : "Event Bridge"
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---

#### Overview
This section will guide you through setting up **Amazon EventBridge** to route and react to events in the workshop architecture. Add your step-by-step instructions below.

#### Prerequisites
- AWS account with sufficient IAM permissions (EventBridge, Lambda, IAM, CloudWatch).
- AWS CLI configured locally (or use the console).
#### 1 — Create SNS

![sns.png](/images/5-Workshop/5.5-Event-Bridge/sns.png)

Create an SNS topic that will receive alerts from EventBridge rules. In the AWS Console: Services → Amazon SNS → Topics → Create topic. Give the topic a clear name (for example `SmartOffice-Alerts`) and configure display name and delivery settings as needed.

![subscription.png](/images/5-Workshop/5.5-Event-Bridge/subscription.png)

After creating the topic, create one or more subscriptions so alerts are delivered to recipients or endpoints (email, Lambda, HTTP(S), SQS). Here add a subscription and choose the protocol.

![email.png](/images/5-Workshop/5.5-Event-Bridge/email.png)

If you use email as a subscription protocol, confirm the subscription from the inbox. Email endpoints require confirmation before they receive messages.

---

#### 2 — Create a rule and attach it to the SNS topic

![rule_1.png](/images/5-Workshop/5.5-Event-Bridge/rule_1.png)

Create a new EventBridge rule to match the events you want to route to SNS. In the Console: Services → Amazon EventBridge → Rules → Create rule.

![rule_2.png](/images/5-Workshop/5.5-Event-Bridge/rule_2.png)

Define the event pattern or choose a schedule. Event patterns can match on `source`, `detail-type`, or specific fields inside `detail`.

![rule_3.png](/images/5-Workshop/5.5-Event-Bridge/rule_3.png)

Select the target for the rule — choose the SNS topic you created earlier. Configure input transformation if you need to change the event payload sent to SNS.

![rule_4.png](/images/5-Workshop/5.5-Event-Bridge/rule_4.png)

Review and create the rule. After creation, EventBridge will forward matching events to the SNS topic which will deliver to its subscriptions.

---

#### 3 — Create AutomationSetup (Lambda + rules)

![lambda_setup.png](/images/5-Workshop/5.5-Event-Bridge/lambda_setup.png)

Create a Lambda function (AutomationSetup) whose job is to read automation configuration (for example from DynamoDB) and define two EventBridge rules: one to turn automation ON and another to turn it OFF. The Lambda should have a clear name such as `SmartOffice-AutomationSetup`.

![trigger_1.png](/images/5-Workshop/5.5-Event-Bridge/trigger_1.png)

Configure the Lambda triggers — this function may be invoked manually, via CloudWatch Events, or triggered by deployment pipelines. Ensure the trigger is correct for your workflow.

![trigger_2.png](/images/5-Workshop/5.5-Event-Bridge/trigger_2.png)

Set required Environment Variables in the Lambda configuration to point to the configuration table, SNS topic ARN, or other parameters used by the function (DB table name, region, etc.).

![environment.png](/images/5-Workshop/5.5-Event-Bridge/environment.png)

Grant the Lambda the IAM permissions it needs: read access to the configuration database (DynamoDB), EventBridge write/put-rule/put-targets, and permissions to manage SNS subscriptions if required.

![setup_permission_1.png](/images/5-Workshop/5.5-Event-Bridge/setup_permission_1.png)

Attach the minimal policy that allows the Lambda to create/update EventBridge rules and targets.

![setup_permission_2.png](/images/5-Workshop/5.5-Event-Bridge/setup_permission_2.png)

After the AutomationSetup Lambda creates the rules, you should see supporting artifacts (rules) in the EventBridge console.

![2rule.png](/images/5-Workshop/5.5-Event-Bridge/2rule.png)

These two rules correspond to the ON and OFF automation behaviours. Ensure naming and tagging so it's easy to manage.

---

#### 4 — Create AutomationHandler (Lambda to forward events to AWS IoT Core)

![handler.png](/images/5-Workshop/5.5-Event-Bridge/handler.png)

Create the AutomationHandler Lambda that receives events from EventBridge and forwards them to AWS IoT Core (or other downstream systems). This function is responsible for parsing the EventBridge `detail` payload and translating it into IoT messages.

![handler_policy.png](/images/5-Workshop/5.5-Event-Bridge/handler_policy.png)

Attach an appropriate IAM policy so the handler can publish messages to AWS IoT Core and read any other resources it needs (for example, secrets from Secrets Manager).

![handler_policy_detail.png](/images/5-Workshop/5.5-Event-Bridge/handler_policy_detail.png)

Review the policy details and remove excessive permissions — prefer least-privilege.

![handler_trigger.png](/images/5-Workshop/5.5-Event-Bridge/handler_trigger.png)

Add EventBridge as a trigger for the handler Lambda (or attach the handler as a target on the rule). Test by sending a sample event and verify it reaches IoT Core.

---

#### Testing and verification
- Verify SNS subscriptions by sending a test message to the topic or executing a rule that triggers the topic.
- Use CloudWatch Logs for both Lambdas to inspect events, errors, and successful deliveries.
- Use EventBridge metrics to confirm rule matches and delivery counts.

{{% notice warning %}}
Replace `REGION`, `ACCOUNT`, ARNs and resource names with values from your account before running CLI/automation. Grant only the minimum required IAM permissions for production use.
{{% /notice %}}

You can add more detailed console screenshots, code snippets for the Lambda handlers, and exact EventBridge event patterns here later.
