---
title : "Thiết lập EventBridge và Lambda"
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---

#### Tổng quan
Phần này sẽ hướng dẫn bạn cách thiết lập **Amazon EventBridge** và **Lambda** để định tuyến và phản ứng với các sự kiện xảy ra trong **DynamoDB**. Để thiết lập SNS (được sử dụng để gửi cảnh báo), vui lòng tham khảo phần **5.6 - Thiết lập SNS**.


#### Tạo AutomationSetup (Lambda + rules)

1. Tạo một hàm **Lambda** (**AutomationSetup**) có nhiệm vụ đọc cấu hình tự động từ **DynamoDB** và xác định hai **rule EventBridge**: một để bật tự động hoá và một khác để tắt tự động hoá.

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

# --- CẬP NHẬT 1: Thêm tham số office_id vào hàm ---
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
    
    # --- CẬP NHẬT 2: Thêm officeId vào JSON Input ---
    target_input = json.dumps({
        "roomId": room_id,
        "officeId": office_id,  # <--- QUAN TRỌNG: Bao gồm officeId
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
                # --- CẬP NHẬT 3: Lấy officeId từ DynamoDB ---
                office_id = data.get('officeId') 
                
                auto_control = data.get('autoControl')
                auto_on = data.get('autoOnTime')
                auto_off = data.get('autoOffTime')
                
                if auto_control == "ON" and room_id:
                    # Chuyển office_id tới hàm tạo lịch biểu
                    if auto_on: create_or_update_schedule(room_id, office_id, auto_on, 'ON')
                    if auto_off: create_or_update_schedule(room_id, office_id, auto_off, 'OFF')
    
    return {'statusCode': 200, 'body': 'Processed'}
```

2. Đi tới **Configuration** --> **Trigger** để cấu hình các **trigger** Lambda — điều này sẽ được sử dụng để gọi lambda bất cứ khi nào có luồng mới từ **DynamoDB**

![trigger_1.png](/images/5-Workshop/5.5-Event-Bridge/trigger_1.png)

3. Chọn **Add Trigger**, chọn **DynamoDB** và chọn bảng chứa cấu hình phòng.

![trigger_2.png](/images/5-Workshop/5.5-Event-Bridge/trigger_2.png)

4. Trong **Configuration** --> **Environment Variable**, thêm cặp khóa-giá trị này (thay thế tương ứng bằng thông tin cá nhân của bạn)

![environment_var.png](/images/5-Workshop/5.5-Event-Bridge/environment_var.png)

5. Chọn **Configuration** -->**Role name**, và đảm bảo bạn có 3 chính sách này: 
- **AutomationSetup_RuleExecuiton** để tạo **rule** trong **EventBridge** 
- **AWSLambdaBasicExecutionRole** cho quyền thực thi lambda cơ bản 
- **AWSLambdaDynamoDBExecutionRole** để tương tác với **DynamoDB**.

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
Chỉ dành cho **AutomationSetup_RuleExecuiton**, chọn **Add permissions** --> **Create inline policy**


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

Hai **rule** này tương ứng với hành vi tự động hoá BẬT và TẮT.

![2rule.png](/images/5-Workshop/5.5-Event-Bridge/2rule.png)

---

#### Tạo AutomationHandler (Lambda để chuyển tiếp các sự kiện tới AWS IoT Core)

1. Tạo **Lambda AutomationHandler** để nhận các sự kiện từ **EventBridge** và chuyển tiếp chúng tới **AWS IoT Core**.

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
    Đầu vào từ EventBridge: {"roomId": "test2", "officeId": "...", "command": "ON", ...}
    """
    # Ghi nhật ký toàn bộ sự kiện để xác minh tải trọng
    logger.info(f"Executing Automation: {json.dumps(event)}")

    # 1. Trích xuất dữ liệu từ Sự kiện
    room_id = event.get('roomId')
    command = event.get('command') # BẬT / TẮT
    office_id = event.get('officeId') 
    
    # 2. Xác thực dữ liệu đầu vào
    if not room_id or not command:
        logger.error("Missing roomId or command")
        return {'statusCode': 400, 'body': 'Missing roomId or command'}

    if not office_id:
        logger.error("Missing officeId")
        return {'statusCode': 400, 'body': 'Missing officeId'}

    # 3. Tạo Chủ đề và Tải trọng
    topic = f"office/{office_id}/room/{room_id}/config"
    
    payload = {
        "command": "SET_STATE",
        "value": command,
        "triggeredBy": "Schedule"
    }
    
    # 4. Gửi lệnh tới IoT Core
    try:
        # Dòng này phải được căn chỉnh với các dòng ở trên
        response = iot_client.publish(
            topic=topic,
            qos=1,
            payload=json.dumps(payload)
        )
        
        logger.info(f"SUCCESS: Sent {command} to {topic}")
        return {'statusCode': 200, 'body': 'Command sent'}
        
    except Exception as e:
        logger.error(f"IoT Publish Error: {e}")
        # Nâng cao lỗi để EventBridge biết nó không thành công (kích hoạt Retry/DLQ)
        raise e
```

2. Đi tới **Configuration** --> **Permissions** và thêm resource-based policy. (Để cho phép **EventBridge** truy cập hàm lambda này)

![handler_policy.png](/images/5-Workshop/5.5-Event-Bridge/handler_policy.png)

![handler_policy_detail.png](/images/5-Workshop/5.5-Event-Bridge/handler_policy_detail.png)

3. Thêm **rule** được tạo bởi **AutomationSetup** làm kích hoạt cho Lambda này.

![handler_trigger.png](/images/5-Workshop/5.5-Event-Bridge/handler_trigger.png)

---


{{% notice warning %}}
Thay thế `REGION`, `ACCOUNT`, ARNs và tên tài nguyên bằng các giá trị từ tài khoản của bạn trước khi chạy.
{{% /notice %}}

