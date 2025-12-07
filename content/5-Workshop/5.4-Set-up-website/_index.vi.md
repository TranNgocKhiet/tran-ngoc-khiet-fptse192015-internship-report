---
title : "Thiết lập website"
weight : 4
chapter : false
pre : " <b> 5.4. </b> "
---

#### Thiết lập Gitlab repository để triển khai website và lambda code

1. Truy cập **Gitlab** repository này: <https://gitlab.com/tranngockhiet22062005/smart-office>
2. Tải xuống và triển khai trên repository của riêng bạn

#### Thiết lập role cho Gitlab để triển khai website lên S3 và triển khai code lên Lambda Function

1. Tạo một IAM User với các thuộc tính sau (xem lại phần 5.2 nếu bạn quên)

- **User name**: ```smart-office-gitlab-ci```
- **Policy**:
```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "S3ListBucketAccess",
			"Effect": "Allow",
			"Action": [
				"s3:ListBucket",
				"s3:GetBucketLocation"
			],
			"Resource": [
				"arn:aws:s3:::fcj-smart-office-frontend-ACCOUNT_ID-dev",
				"arn:aws:s3:::fcj-smart-office-lambda-ACCOUNT_ID-dev"
			]
		},
		{
			"Sid": "S3ReadWriteAccess",
			"Effect": "Allow",
			"Action": [
				"s3:PutObject",
				"s3:GetObject",
				"s3:DeleteObject",
				"s3:PutObjectAcl"
			],
			"Resource": [
				"arn:aws:s3:::fcj-smart-office-frontend-ACCOUNT_ID-dev/*",
				"arn:aws:s3:::fcj-smart-office-lambda-ACCOUNT_ID-dev/*"
			]
		},
		{
			"Sid": "LambdaUpdateAccess",
			"Effect": "Allow",
			"Action": [
				"lambda:UpdateFunctionCode",
				"lambda:GetFunction",
				"lambda:GetFunctionConfiguration"
			],
			"Resource": "arn:aws:lambda:*:*:function:SmartOffice-*"
		},
		{
			"Sid": "CloudFrontInvalidation",
			"Effect": "Allow",
			"Action": [
				"cloudfront:CreateInvalidation",
				"cloudfront:GetDistribution"
			],
			"Resource": "*"
		}
	]
}
```

{{% notice warning %}} Bạn nên thay thế ACCOUNT_ID bằng AWS Account ID của bạn {{% /notice %}}

- **Policy name**: `SmartOfficeGitlabAccess`

1. Điều hướng đến user đó
2. Trong phần **Summary**, nhấp vào **Create access key**
   
![iam_create_access_key.png](/images/5-Workshop/5.4-Gitlab/iam_create_access_key.png)

4. Tại mục **Use case**, tích chọn **Command Line Interface (CLI)**
5. Tích chọn **I understand the above recommendation and want to proceed to create an access key.**
6. Nhấp **Next**
   
![iam_create_access_key_step_1.png](/images/5-Workshop/5.4-Gitlab/iam_create_access_key_step_1.png)

7. Nhấp **Create access key**
8. Nhấp **Download .csv file**

![iam_create_access_key_step_3.png](/images/5-Workshop/5.4-Gitlab/iam_create_access_key_step_3.png)

#### Cấu hình các biến Gitlab

1. Truy cập **Gitlab** repository của bạn, nhấp vào **Setting** > **Variables**
2. Nhấp **Add variable**

![gitlab_variables.png](/images/5-Workshop/5.4-Gitlab/gitlab_variables.png)

3. Đối với mỗi **Key** và **Value**, hãy làm theo bảng dưới đây để biết nơi lấy giá trị
| Key                        | Value 																						|
|----------------------------|----------------------------------------------------------------------------------------------|
| AWS_ACCESS_KEY_ID          | In your ```smart-office-gitlab-ci_accessKeys.csv``` you have downloaded 						|
| AWS_DEFAULT_REGION         | ```ap-southeast-1``` (or anywhere you deploy the workshop)								 	|
| AWS_SECRET_ACCESS_KEY      | In your ```smart-office-gitlab-ci_accessKeys.csv``` you have downloaded 						|
| CLOUDFRONT_DISTRIBUTION_ID | **CloudFront** > **Distributions** > Your distribution ID 									|
| S3_BUCKET_FRONTEND         | ```fcj-smart-office-frontend-ACCOUNT_ID-dev``` (replace ACCOUNT_ID with your AWS Account ID) |
| S3_BUCKET_LAMBDA           | ```fcj-smart-office-lambda-ACCOUNT_ID-dev``` (replace ACCOUNT_ID with your AWS Account ID) 	|
| STACK_NAME_AUTH            | ```SmartOffice-Authenticate-Lambda-Dev``` 													|
| STACK_NAME_CRUD            | ```SmartOffice-Crud-Lambda-Dev``` 															|
| STACK_NAME_IOT             | ```SmartOffice-IoT-Lambda-Dev``` 															|
| STACK_NAME_READONLY        | ```SmartOffice-ReadOnly-Lambda-Dev``` 														|
| VITE_API_BASE_URL          | **API Gateway** > **SmartOffice-API-Gateway-Dev-Api** > **Stages** > **Invoke URL** 			|

4. Push code vào nhánh `init`
5. Merge các branch theo thứ tự sau: `init` -> `dev`, `dev` -> `main`