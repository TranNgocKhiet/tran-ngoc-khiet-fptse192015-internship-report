---
title : "Thiết lập CloudFormation"
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

#### Tải xuống tài nguyên

Tải xuống các tệp mẫu **CloudFormation** này:

- [smart_office_budget.yaml](/file/cloudformation/smart_office_budget.yaml)
- [smart_office_s3_cloudfront.yaml](/file/cloudformation/smart_office_s3_cloudfront.yaml)
- [smart_office_cognito.yaml](/file/cloudformation/smart_office_cognito.yaml)
- [smart_office_dynamodb.yaml](/file/cloudformation/smart_office_dynamodb.yaml)
- [smart_office_lambda_authenticate_with_dynamodb_cognito.yaml](/file/cloudformation/smart_office_lambda_authenticate_with_dynamodb_cognito.yaml)
- [smart_office_lambda_readonly_with_dynamodb.yaml](/file/cloudformation/smart_office_lambda_readonly_with_dynamodb.yaml)
- [smart_office_lambda_crud_with_dynamodb_cognito.yaml](/file/cloudformation/smart_office_lambda_crud_with_dynamodb_cognito.yaml)
- [smart_office_lambda_crud_with_dynamodb_iot.yaml](/file/cloudformation/smart_office_lambda_crud_with_dynamodb_iot.yaml)
- [smart_office_iot_core.yaml](/file/cloudformation/smart_office_iot_core.yaml)
- [smart_office_api_gateway.yaml](/file/cloudformation/smart_office_api_gateway.yaml)

#### Triển khai các CloudFormation Stack

1. Trong **AWS Management Console**, tìm kiếm và chọn **CloudFormation**

![cloudformation_management_console](/images/5-Workshop/5.3-CloudFormation/cloudformation_management_console.png)

2. Nhấp vào **Create stack**
3. Tại mục **Prepare template**, tích chọn **Choose an existing template**
4. Tại mục **Template source**, tích chọn **Upload a template file**
5. Nhấp vào **Choose file**
6. Chọn tệp ```smart_office_budget.yaml```
7. Nhấp vào **Next**

![cloudformation_step_1.png](/images/5-Workshop/5.3-CloudFormation/cloudformation_step_1.png)

8. Tại mục **Stack name**, nhập ```SmartOffice-Budget-Dev```
9. Nhấp vào **Next**

![cloudformation_step_2.png](/images/5-Workshop/5.3-CloudFormation/cloudformation_step_2.png)

10. Thêm **Tags** để quản lý chi phí và vận hành (Key: ```Project```, Value: ```SmartOffice```; Key: ```Environment```, Value: ```Dev```)
11. Tại mục **Stack failure options**, tích chọn **Preserve successfully provisioned resources** (Để giữ lại tài nguyên đã tạo phục vụ việc gỡ lỗi)
12. Nhấp vào **Next**

![cloudformation_step_3.png](/images/5-Workshop/5.3-CloudFormation/cloudformation_step_3.png)

13. Kiểm tra lại và nhấp vào **Submit**

## Thực hiện tương tự cho các tệp khác với tên chính xác như sau

| Tên Template                                                | Tên Stack                                 |
|-------------------------------------------------------------|-------------------------------------------|
| smart_office_s3_cloudfront.yaml                             | ```SmartOffice-S3-CloudFront-Dev```       |
| smart_office_cognito.yaml                                   | ```SmartOffice-Cognito-Dev```             |
| smart_office_dynamodb.yaml                                  | ```SmartOffice-DynamoDB-Dev```            |
| smart_office_lambda_authenticate_with_dynamodb_cognito.yaml | ```SmartOffice-Authenticate-Lambda-Dev``` |
| smart_office_lambda_readonly_with_dynamodb.yaml             | ```SmartOffice-ReadOnly-Lambda-Dev```     |
| smart_office_lambda_crud_with_dynamodb_cognito.yaml         | ```SmartOffice-Crud-Lambda-Dev```         |
| smart_office_lambda_crud_with_dynamodb_iot.yaml             | ```SmartOffice-IoT-Lambda-Dev```          |
| smart_office_iot_core.yaml                                  | ```SmartOffice-IoT-Core-Dev```            |
| smart_office_api_gateway.yaml                               | ```SmartOffice-API-Gateway-Dev```         |