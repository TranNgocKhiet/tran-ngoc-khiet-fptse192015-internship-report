import boto3
import json

# Config
TABLE_NAME = "SmartOffice-DynamoDB-Dev-Manager"
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

# Dữ liệu mẫu bạn đang có
data = [
  {
    "orgAlias": "FPT University",
    "email": "manager1@smartoffice.com",
    "name": "Manager One",
    "assignedOfficeId": "Office Ha Noi Campus",
  },
  {
    "orgAlias": "FPT University",
    "email": "manager2@smartoffice.com",
    "name": "Manager Two",
    "assignedOfficeId": "Office HCM Campus",
  }
]

# Batch Write (Ghi hàng loạt)
with table.batch_writer() as batch:
    for item in data:
        batch.put_item(Item=item)
        print(f"Added: {item['email']}")

print("Done!")