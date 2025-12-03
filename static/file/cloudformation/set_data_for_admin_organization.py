import boto3
import json

# Config
TABLE_NAME = "SmartOffice-DynamoDB-Dev-Office" 
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

# Dữ liệu mẫu bạn đang có
data = [
  {
    "orgAlias": "FPT University",
    "entityId": "organization",
    "adminFullName": "Admin",
    "adminEmail": "admin@smartoffice.com",
  },
  {
    "orgAlias": "FPT University",
    "entityId": "Office HCM Campus",
    "address": "Khu Công Nghệ Cao, Q9, TP.HCM",
  },
  {
    "orgAlias": "FPT University",
    "entityId": "Office Ha Noi Campus",
    "address": "... TP.Ha Noi",
  }
]

# Batch Write (Ghi hàng loạt)
with table.batch_writer() as batch:
    for item in data:
        batch.put_item(Item=item)
        print(f"Added: {item['entityId']}")

print("Done!")