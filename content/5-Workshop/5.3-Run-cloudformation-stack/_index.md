---
title : "Set up cloudformation"
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

#### Download resources

Download these **CloudFormation** template files:

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

#### Deploy CloudFormation Stacks

1. In **AWS Management Console**, search and choose **CloudFormation**

![cloudformation_management_console](/images/5-Workshop/5.3-CloudFormation/cloudformation_management_console.png)

2. Click **Create stack**
3. For **Prepare template**, check **Choose an existing template**
4. For **Template source**, check **Upload a template file**
5. Click **Choose file**
6. Choose file ```smart_office_budget.yaml```
7. Click **Next**

![cloudformation_step_1.png](/images/5-Workshop/5.3-CloudFormation/cloudformation_step_1.png)

8. For **Stack name**, enter ```SmartOffice-Budget-Dev```
9.  Click **Next**

![cloudformation_step_2.png](/images/5-Workshop/5.3-CloudFormation/cloudformation_step_2.png)

10.  Add **Tags** for cost and operation management (Key: ```Project```, Value: ```SmartOffice```; Key: ```Environment```, Value: ```Dev```)
11.  For **Stack failure options**, check **Preserve successfully provisioned resources** (To keep created resource for debugging)
12.  Click **Next**

![cloudformation_step_3.png](/images/5-Workshop/5.3-CloudFormation/cloudformation_step_3.png)

13.  Check again and click **Submit**

## Do the same for other files with exactly name

| Template name                                               | Stack name                                |
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
