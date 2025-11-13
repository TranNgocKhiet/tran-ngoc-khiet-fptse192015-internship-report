---
title : "Set up client AWS Lambda Functions"
weight : 1
chapter : false
pre : " <b> 5.6.1 </b> "
---

## Create Function

1. Open **Management Console**, search and choose ```Lambda```

![Lambda Function 1](/images/5-Workshop/5.6-Lambda-Function/Lambda-Function-1.png)

2. Navigate to tab **Functions**, click **Create function**

![Lambda Function 2](/images/5-Workshop/5.6-Lambda-Function/Lambda-Function-2.png)

3. Choose **Author from scratch**
4. For **Function name**, enter ```SmartOfficeProfileUpdateHandler```
5. For **Runtime**, choose **Python 3.14**
6. For **Architecture**, choose **arm64**
7. Expand the **Change default execution role**, choose **Use an existing role**
8. For Existing role, choose ```SmartOfficeProfileUpdateHandler```

![Lambda Function 3](/images/5-Workshop/5.6-Lambda-Function/Lambda-Function-3.png)

9. Click **Create Function**
10. In the **Code source** IDE, paste this code to it

```python
import boto3
import json
import os

# Create client and handler
dynamodb = boto3.resource('dynamodb')
cognito_client = boto3.client('cognito-idp')

# Get environment variables
TABLE_NAME = os.environ.get('TABLE_NAME')
USER_POOL_ID = os.environ.get('USER_POOL_ID')

table = dynamodb.Table(TABLE_NAME)

def build_update_params(updates):
    update_expression = "SET "
    expression_names = {}
    expression_values = {}
    
    # Use #name and #email to avoid reserved words
    attribute_map = {
        "name": "#name",
        "email": "#email",
    }
    
    for key, value in updates.items():
        if key in attribute_map:
            placeholder = f":{key}"
            attr_name = attribute_map[key]
            
            update_expression += f"{attr_name} = {placeholder}, "
            expression_values[placeholder] = value
            expression_names[attr_name] = key

    update_expression = update_expression.rstrip(", ")

    return update_expression, expression_names, expression_values

def lambda_handler(event, context):
    try:

        if "body" in event:
            body = json.loads(event["body"])
        else:
            body = event
                        
        user_id = body.get('userId')
        updates = body.get('updates') 

        if not user_id or not updates:
            return {'statusCode': 400, 'body': 'Lỗi: Thiếu "userId" hoặc "updates"'}

        update_expr, attr_names, attr_values = build_update_params(updates)

        if not attr_values:
            return {'statusCode': 400, 'body': 'Không có trường hợp lệ nào để cập nhật'}

        dynamo_response = table.update_item(
            Key={'userId': user_id},
            UpdateExpression=update_expr,
            ExpressionAttributeNames=attr_names,
            ExpressionAttributeValues=attr_values,
            ReturnValues="UPDATED_NEW"
        )

        if 'email' in updates:
            new_email = updates['email']
            try:
                cognito_client.admin_update_user_attributes(
                    UserPoolId=USER_POOL_ID,
                    Username=user_id, 
                    UserAttributes=[
                        {
                            'Name': 'email',
                            'Value': new_email
                        },
                        {
                            'Name': 'email_verified',
                            'Value': 'true'
                        }
                    ]
                )
            except Exception as e:
                print(f"Cognito Error: {e}")
                return {
                    'statusCode': 500,
                    'body': f'Update DynamoDB success, but failed to update Cognito: {str(e)}'
                }

        success_body = {
            "message": "Update success",
            "updatedAttributes": dynamo_response.get('Attributes')
        }
        return {
            'statusCode': 200,
            'body': json.dumps(success_body)
        }

    except Exception as e:
        print(f"Unknow error: {e}")
        return {
            'statusCode': 500,
            'body': f'Error when handle request: {str(e)}'
        }
```

![Lambda Function 4](/images/5-Workshop/5.6-Lambda-Function/Lambda-Function-4.png)

11. Click **Deploy**
12. Navigate to tab **Configuration**, choose **Environment variables**
13. Click **Edit** 

![Lambda Function 5](/images/5-Workshop/5.6-Lambda-Function/Lambda-Function-5.png)

14. Click **Add environment variable** twice
15. For first **Key**, enter ```TABLE_NAME```
16. For first **Value**, enter ```SmartOffice_User_Prod```
17. For second **Key**, enter ```USER_POOL_ID```
18. For second **Value**, enter your user pool ID from AWS Cognito User Pool (Go to **Cognito** ->  **User pools** -> Choose your User pool -> **Overview** -> **User pool ID**)

![Lambda Function 6](/images/5-Workshop/5.6-Lambda-Function/Lambda-Function-6.png)

19. Click **Save**

---

### Test Function

1. Navigate to tab **Test**
2. For **Event name**, enter ```test-update-name```
3. For **Event JSON**, copy and paste this test json

```json
{
  "userId": "692a45fc-0091-7055-703b-49b4db5cbe0c",
  "updates": {
    "name": "Tên Mới",
    "email": "email.moi@example.com"
  }
}
```

{{% notice note %}}
Get **userId** from **User** in **Amazon Cognito User Pool** (Go to **Cognito** -> **User pools** -> Choose your User pool -> **Users** -> Choose your User -> **User ID**)
{{% /notice %}}

4. Click **Test**

![Lambda Function 7](/images/5-Workshop/5.6-Lambda-Function/Lambda-Function-7.png)

## Do the same for 

```python
import boto3
import os
import json
from datetime import datetime, timezone

# Khởi tạo client
dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ.get('TABLE_NAME')
table = dynamodb.Table(TABLE_NAME)

# Danh sách các trường ĐƯỢC PHÉP cập nhật
# (Để ngăn người dùng vô tình cập nhật roomId, officeId)
ALLOWED_UPDATE_FIELDS = [
    "temperatureMode",
    "humidityMode",
    "lightMode",
    "targetTemperature",
    "targetHumidity",
    "targetLight",
    "autoOnTime",
    "autoOffTime"
]

def lambda_handler(event, context):
    """
    Cập nhật cấu hình phòng dựa trên officeId và roomId.
    Tự động cập nhật trường "lastUpdate".

    Event JSON mong đợi:
    {
      "officeId": "office-hcm",
      "roomId": "A101",
      "updates": {
        "temperatureMode": "manual",
        "targetTemperature": 24
      }
    }
    """
    try:
        # 1. Lấy thông tin từ event
        # (Giả sử event là JSON body, nếu dùng API Gateway, bạn có thể cần json.loads(event['body']))
        body = event 
        
        office_id = body.get('officeId')
        room_id = body.get('roomId')
        updates = body.get('updates')

        if not office_id or not room_id or not updates:
            return {'statusCode': 400, 'body': 'Lỗi: Thiếu "officeId", "roomId", hoặc "updates"'}

        # 2. Xây dựng các biểu thức (expressions) cho DynamoDB
        update_expression = "SET "
        expression_names = {}
        expression_values = {}

        # Lọc các trường hợp lệ
        valid_updates = False
        for key, value in updates.items():
            if key in ALLOWED_UPDATE_FIELDS:
                valid_updates = True
                placeholder_name = f"#{key}"  # Ví dụ: #temperatureMode
                placeholder_value = f":{key}" # Ví dụ: :temperatureMode
                
                update_expression += f"{placeholder_name} = {placeholder_value}, "
                expression_names[placeholder_name] = key
                expression_values[placeholder_value] = value

        if not valid_updates:
            return {'statusCode': 400, 'body': 'Không có trường hợp lệ nào trong "updates"'}

        # 3. Tự động thêm "lastUpdate"
        current_time_iso = datetime.now(timezone.utc).isoformat()
        
        update_expression += "#lastUpdate = :lastUpdate" # Thêm vào cuối, không có dấu phẩy
        expression_names["#lastUpdate"] = "lastUpdate"
        expression_values[":lastUpdate"] = current_time_iso

        # 4. Định nghĩa Khóa chính (Primary Key)
        # *** Giả định: (officeId là Khóa Phân vùng, roomId là Khóa Sắp xếp) ***
        key_to_update = {
            'officeId': office_id,
            'roomId': room_id
        }

        # 5. Gọi DynamoDB
        response = table.update_item(
            Key=key_to_update,
            UpdateExpression=update_expression,
            ExpressionAttributeNames=expression_names,
            ExpressionAttributeValues=expression_values,
            ReturnValues="UPDATED_NEW" # Trả về các giá trị vừa được cập nhật
        )

        success_body = {
            "message": "Cập nhật cấu hình phòng thành công",
            "updatedAttributes": response.get('Attributes')
        }
        return {
            'statusCode': 200,
            'body': json.dumps(success_body)
        }

    except Exception as e:
        print(f"Lỗi: {e}")
        # Xử lý lỗi nếu không tìm thấy item
        if "ConditionalCheckFailedException" in str(e):
             return {'statusCode': 404, 'body': 'Không tìm thấy phòng với officeId và roomId đã cho'}
        
        return {
            'statusCode': 500,
            'body': f'Lỗi khi xử lý yêu cầu: {str(e)}'
        }
```