---
title : "Set up website"
weight : 4
chapter : false
pre : " <b> 5.4. </b> "
---

#### Set up Gitlab repository to deploy website and lambda code

1. Go to this **Gitlab** repository: <https://gitlab.com/tranngockhiet22062005/smart-office>
2. Download and deploy on your own repository

#### Set up role for Gitlab to deploy website to S3 and deploy code to Lambda Function

1. Create an IAM User with following attribute (view 5.2 if you forget)

- **User name**: ```smart-office-gitlab-ci```
- **Policy**:
```
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

{{% notice warning %}}
You should replace ACCOUNT_ID with your AWS Account ID
{{% /notice %}}

- **Policy name**: ```SmartOfficeGitlabAccess```

1. Navigate to the user
2. In **Summary**, click **Create access key**
   
![iam_create_access_key.png](/images/5-Workshop/5.4-Gitlab/iam_create_access_key.png)

4. For **Use case**, check **Command Line Interface (CLI)**
5. Check **I understand the above recommendation and want to proceed to create an access key.**
6. Click **Next**
   
![iam_create_access_key_step_1.png](/images/5-Workshop/5.4-Gitlab/iam_create_access_key_step_1.png)

7. Click **Create access key**
8. Click **Download .csv file**

![iam_create_access_key_step_3.png](/images/5-Workshop/5.4-Gitlab/iam_create_access_key_step_3.png)

#### Config Gitlab variables

1. Go to your **Gitlab** repository, click **Setting** > **Variables**
2. Click **Add variable**

![gitlab_variables.png](/images/5-Workshop/5.4-Gitlab/gitlab_variables.png)

3. For each **Key** and **Value** follow the table bellow to know where to get value

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

4. Push code into an ```init``` branch 
5. Merge branchs in this order: ```init``` -> ```dev```, ```dev``` -> ```main```