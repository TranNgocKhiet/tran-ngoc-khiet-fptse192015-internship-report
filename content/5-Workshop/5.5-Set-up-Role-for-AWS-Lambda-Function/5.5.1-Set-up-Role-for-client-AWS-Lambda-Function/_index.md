---
title : "Set up IAM Role for client AWS Lambda Functions"
weight : 1
chapter : false
pre : " <b> 5.5.1 </b> "
---

## Create Policy

1. Open **Management Console**, search and choose ```IAM```

![IAM Role 1](/images/5-Workshop/5.5-IAM-Role/IAM-Role-1.png)

2. Navigate to tab **Policies**, click **Create policy**

![IAM Role 2](/images/5-Workshop/5.5-IAM-Role/IAM-Role-2.png)

3. Choose **JSON**
4. Enter
```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "AllowCognitoUpdate",
			"Effect": "Allow",
			"Action": "cognito-idp:AdminUpdateUserAttributes",
			"Resource": ""
		},
		{
			"Sid": "AllowLambdaCRUDOnUserTable",
			"Effect": "Allow",
			"Action": [
				"dynamodb:PutItem",
				"dynamodb:GetItem",
				"dynamodb:UpdateItem",
				"dynamodb:DeleteItem"
			],
			"Resource": ""
		}
	]
}
```

{{% notice note %}}
You need to find the **ARN** (Amazon Resource Name), copy it and paste for each Resource
<br> - The first **Resource** for Amazon Cognito is your User Pool ARN (Go to **Cognito** -> **User pools** -> Choose your User pool -> **Overview** -> **ARN**)
<br> -  The second **Resource** for Amazon DynamoDB is your DynamoDB Table ARN (Go to **DynamoDB** -> **Tables** -> Choose your Table -> **Settings** -> **Amazon Resource Name (ARN)**)
{{% /notice %}}

![IAM Role 3](/images/5-Workshop/5.5-IAM-Role/IAM-Role-3.png)

5. Click **Next**
6. For **Policy name**, type ```SmartOfficeProfileUpdate```
7. For **Description** (optional), type ```Allow CRUD on Amazon DynamoDB and update user in Amazon Cognito```
8. Add **Tag** for management (**Key**: ```Project```, **Value**: ```SmartOffice```; **Key**: ```Environment```, **Value**: ```Dev```)

![IAM Role 4](/images/5-Workshop/5.5-IAM-Role/IAM-Role-4.png)

9. Click Create policy

---

## Create role

1.  Navigate to tab **Roles**, click **Create role**
 
![IAM Role 5](/images/5-Workshop/5.5-IAM-Role/IAM-Role-5.png)

2. For **Trusted entity type**, choose **AWS service**
3. For **Use case**, search and choose ```Lambda```

![IAM Role 6](/images/5-Workshop/5.5-IAM-Role/IAM-Role-6.png)

4. Click **Next**
5. For Permissions policies, search and check ```SmartOfficeProfileUpdate```

![IAM Role 7](/images/5-Workshop/5.5-IAM-Role/IAM-Role-7.png)

6. For **Role name**, enter ```SmartOfficeProfileUpdateHandler```
7. For **Description** (optional), enter ```Role for Lambda to perform CRUD on DynamoDB and update user on Cognito```
8. Add **Tag** for management (**Key**: ```Project```, **Value**: ```SmartOffice```; **Key**: ```Environment```, **Value**: ```Dev```)

![IAM Role 7](/images/5-Workshop/5.5-IAM-Role/IAM-Role-8.png)

9. Click **Create Role**

---

## Do the same for role RoomConfig:
- **Policy name**: ```SmartOfficeRoomConfig```
- **Description** (optional): ```Allow CRUD on Amazon DynamoDB```
- **Policy editor**: 
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowLambdaCRUDOnRoomConfigTable",
      "Effect": "Allow",
      "Action": [
        "dynamodb:PutItem",
        "dynamodb:GetItem",
        "dynamodb:UpdateItem",
        "dynamodb:DeleteItem",
        "dynamodb:Query",
        "dynamodb:Scan"
      ],
      "Resource": ""
    }
  ]
}
```
- **Role Name**: ```SmartOfficeRoomConfigHandler```
- **Description** (optional), enter ```Role for Lambda to perform CRUD on DynamoDB```
- Other setting same as **SmartOfficeProfileUpdateHandler**