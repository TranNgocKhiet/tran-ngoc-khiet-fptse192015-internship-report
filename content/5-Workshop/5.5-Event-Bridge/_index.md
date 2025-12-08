---
title : "EventBridge and Lambda Setup"
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---

#### Overview
This section will guide you through setting up **Amazon EventBridge** and **Lambda** to route and react to events happening in **DynamoDB**. For SNS setup (used to send alerts), please refer to section **5.6 - SNS Setup**.


#### Create AutomationSetup (Lambda + rules)

1. Create a Lambda function (**AutomationSetup**) whose job is to read automation configuration from **DynamoDB** and define two **EventBridge rules**: one to turn automation ON and another to turn it OFF.

![lambda_setup.png](/images/5-Workshop/5.5-Event-Bridge/lambda_setup.png)

```
import boto3
import json
import os
from boto3.dynamodb.types import TypeDeserializer

deserializer = TypeDeserializer()
events_client = boto3.client('events')
HANDLER_ARN = os.environ.get('HANDLER_LAMBDA_ARN') 

def ddb_deserialize(image):
    d = {}
    for key in image:
        d[key] = deserializer.deserialize(image[key])
    return d

def time_to_cron(time_str):
    try:
        hour, minute = map(int, time_str.split(':'))
        utc_hour = hour - 7
        if utc_hour < 0: utc_hour += 24
        return f"cron({minute} {utc_hour} * * ? *)"
    except: return None

# --- UPDATE 1: Add office_id parameter to function ---
def create_or_update_schedule(room_id, office_id, time_str, action):
    rule_name = f"Room_{room_id}_Auto_{action}"
    cron_expr = time_to_cron(time_str)
    
    if not cron_expr: return

    print(f"Updating Rule: {rule_name} with Input")
    
    events_client.put_rule(
        Name=rule_name,
        ScheduleExpression=cron_expr,
        State='ENABLED',
        Description=f'Auto {action} for {room_id} in {office_id}'
    )
    
    # --- UPDATE 2: Add officeId to Input JSON ---
    target_input = json.dumps({
        "roomId": room_id,
        "officeId": office_id,  # <--- IMPORTANT: Include officeId
        "command": action.upper(), 
        "source": "Scheduled_Event"
    })
    
    events_client.put_targets(
        Rule=rule_name,
        Targets=[{
            'Id': '1', 
            'Arn': HANDLER_ARN, 
            'Input': target_input 
        }]
    )

def lambda_handler(event, context):
    print("Raw Event:", json.dumps(event))
    
    if 'Records' in event:
        for record in event['Records']:
            if record['eventName'] in ['INSERT', 'MODIFY']:
                raw_image = record['dynamodb']['NewImage']
                data = ddb_deserialize(raw_image)
                
                room_id = data.get('roomId')
                # --- UPDATE 3: Get officeId from DynamoDB ---
                office_id = data.get('officeId') 
                
                auto_control = data.get('autoControl')
                auto_on = data.get('autoOnTime')
                auto_off = data.get('autoOffTime')
                
                if auto_control == "ON" and room_id:
                    # Pass office_id to schedule creation function
                    if auto_on: create_or_update_schedule(room_id, office_id, auto_on, 'ON')
                    if auto_off: create_or_update_schedule(room_id, office_id, auto_off, 'OFF')
    
    return {'statusCode': 200, 'body': 'Processed'}
```

2. Go to **Configuration** --> **Trigger** to configure the Lambda **triggers** — this will be used to invoke the lambda whenever there is any new stream from **DynamoDB**

![trigger_1.png](/images/5-Workshop/5.5-Event-Bridge/trigger_1.png)

3. Select **Add Trigger**, Select **DynamoDB** and choose the table that contains rooms's config.

![trigger_2.png](/images/5-Workshop/5.5-Event-Bridge/trigger_2.png)

4. In **Configuration** --> **Environment Variable**, add this key-value pair (replace accordingly with your personal information)

![environment_var.png](/images/5-Workshop/5.5-Event-Bridge/environment_var.png)

5. Select **Configuration** -->**Role name**, and make sure you have those 3 policies: 
- **AutomationSetup_RuleExecuiton** for creating **rules** in **EventBridge** 
- **AWSLambdaBasicExecutionRole** for basic lambda execution permissions 
- **AWSLambdaDynamoDBExecutionRole** for interacting with **DynamoDB**.

![setup_role.png](/images/5-Workshop/5.5-Event-Bridge/setup_role.png)


```
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "VisualEditor0",
			"Effect": "Allow",
			"Action": [
				"events:DeleteRule",
				"events:PutTargets",
				"events:EnableRule",
				"events:PutRule",
				"events:DisableRule"
			],
			"Resource": "*"
		}
	]
}
```
Only for **AutomationSetup_RuleExecuiton**, select **Add permissions** --> **Create inline policy**


```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "arn:aws:logs:ap-southeast-1:261899902491:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:ap-southeast-1:261899902491:log-group:/aws/lambda/AutomationSetup:*"
            ]
        }
    ]
}
```
**AWSLambdaBasicExecutionRole**
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:DescribeStream",
                "dynamodb:GetRecords",
                "dynamodb:GetShardIterator",
                "dynamodb:ListStreams",
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
```
**AWSLambdaDynamoDBExecutionRole**

These two **rules** correspond to the ON and OFF automation behaviours.

![2rule.png](/images/5-Workshop/5.5-Event-Bridge/2rule.png)

---

#### Create AutomationHandler (Lambda to forward events to AWS IoT Core)

1. Create the **AutomationHandler** Lambda to receives events from **EventBridge** and forwards them to **AWS IoT Core**.

![handler.png](/images/5-Workshop/5.5-Event-Bridge/handler.png)

```
import boto3
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

iot_client = boto3.client('iot-data', region_name='ap-southeast-1')

def lambda_handler(event, context):
    """
    Input from EventBridge: {"roomId": "test2", "officeId": "...", "command": "ON", ...}
    """
    # Log entire event to verify payload
    logger.info(f"Executing Automation: {json.dumps(event)}")

    # 1. Extract data from Event
    room_id = event.get('roomId')
    command = event.get('command') # ON / OFF
    office_id = event.get('officeId') 
    
    # 2. Validate input data
    if not room_id or not command:
        logger.error("Missing roomId or command")
        return {'statusCode': 400, 'body': 'Missing roomId or command'}

    if not office_id:
        logger.error("Missing officeId")
        return {'statusCode': 400, 'body': 'Missing officeId'}

    # 3. Create Topic and Payload
    topic = f"office/{office_id}/room/{room_id}/config"
    
    payload = {
        "command": "SET_STATE",
        "value": command,
        "triggeredBy": "Schedule"
    }
    
    # 4. Send command to IoT Core
    try:
        # This line must be aligned with lines above
        response = iot_client.publish(
            topic=topic,
            qos=1,
            payload=json.dumps(payload)
        )
        
        logger.info(f"SUCCESS: Sent {command} to {topic}")
        return {'statusCode': 200, 'body': 'Command sent'}
        
    except Exception as e:
        logger.error(f"IoT Publish Error: {e}")
        # Raise error for EventBridge to know it failed (trigger Retry/DLQ)
        raise e
```

2. Go to **Configuration** --> **Permissions** and add resource-based policy. (To allow **EventBridge** to access this lambda function)

![handler_policy.png](/images/5-Workshop/5.5-Event-Bridge/handler_policy.png)

![handler_policy_detail.png](/images/5-Workshop/5.5-Event-Bridge/handler_policy_detail.png)

3. Add the 2 **rules** created by **AutomationSetup** as a trigger for this Lambda.

![handler_trigger.png](/images/5-Workshop/5.5-Event-Bridge/handler_trigger.png)

---


{{% notice warning %}}
Replace `REGION`, `ACCOUNT`, ARNs and resource names with values from your account before running.
{{% /notice %}}

