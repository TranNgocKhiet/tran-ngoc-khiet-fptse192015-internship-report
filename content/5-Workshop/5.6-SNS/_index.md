---
title : "SNS Setup"
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

#### Overview
This section will guide you through setting up **Amazon SNS (Simple Notification Service)** to receive alerts from EventBridge when data anomalies are detected.


---

#### Create SNS Topic

1. Go to **Amazon SNS** Console
2. Select **Topic** and name your **Topic**

{{% notice warning %}}
DON'T TURN ON ENCRYPTION
{{% /notice %}}

![sns.png](/images/5-Workshop/5.6-SNS/sns.png)

#### Create SNS Subscription

After creating the topic, create one or more subscriptions so alerts are delivered to recipients or endpoints (in this case, **email**).

Steps:
1. Select **Subscription** in **SNS**
2. Choose **email** protocol, select the **topic** you just created, and write down the email you want to test.

![subcription.png](/images/5-Workshop/5.6-SNS/subcription.png)

Email endpoints require confirmation before they receive messages. Check your inbox for a confirmation email from AWS SNS and confirm the subscription.

![email.png](/images/5-Workshop/5.6-SNS/email.png)

---

#### Create a rule and attach it to the SNS topic

1. Go to **Amazon EventBridge** Console 
2. Select **Rules** and create a new **rule**

![rule_1.png](/images/5-Workshop/5.6-SNS/rule_1.png)

3. In step 2, we define the event pattern by choosing **Custom pattern**. Event patterns can match on `source`, `detail-type`.

4. Use the following Json:

```
{
  "source": ["com.smartoffice.iot"],
  "detail-type": ["sensor.anomaly"]
}
```

![rule_2.png](/images/5-Workshop/5.6-SNS/rule_2.png)

5. In step 3, Select the target for the rule — choose the **SNS topic** you created earlier.

![rule_3.png](/images/5-Workshop/5.6-SNS/rule_3.png)

After creation, **EventBridge** will forward matching events to the **SNS topic** which will deliver to its subscriptions.

![rule_4.png](/images/5-Workshop/5.6-SNS/rule_4.png)

{{% notice warning %}}
Replace email addresses and resource names with values from your account before running.
{{% /notice %}}
