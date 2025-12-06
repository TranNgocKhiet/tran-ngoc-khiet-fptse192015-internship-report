---
title : "Prerequiste"
weight : 2 
chapter : false
pre : " <b> 5.2. </b> "
---

#### Create IAM User for this workshop

1. In **AWS Management Console**, search and choose **IAM**

![iam_mangement_console](/images/5-Workshop/5.2-Prerequisite/iam_mangement_console.png)

2. Navigate to **User**, click **Create user**

![iam_create_user](/images/5-Workshop/5.2-Prerequisite/iam_create_user.png)

3. For **User name**, enter ```admin-user```
4. Check **Provide user access to the AWS Management Console - optional**
5. For **Console password**, check **Custom password**
6. Enter password for your user
7. Uncheck **Users must create a new password at next sign-in - Recommended** for easy operation
8. Click **Next**

![iam_create_user_step_1](/images/5-Workshop/5.2-Prerequisite/iam_create_user_step_1.png)

9. For **Permissions options**, check **Attach policies directly**
10. Click **Create policy**

![iam_create_user_step_2_1](/images/5-Workshop/5.2-Prerequisite/iam_create_user_step_2_1.png)

11. You will be directed to **Create policy** page
12. For **Policy editor**, switch to **JSON**
13. Copy and paste this policy

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "InfrastructureManagement",
            "Effect": "Allow",
            "Action": [
                "cloudformation:*",
                "iam:*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "BackendComputeAndAPI",
            "Effect": "Allow",
            "Action": [
                "lambda:*",
                "apigateway:*",
                "execute-api:*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "DatabaseAndAuth",
            "Effect": "Allow",
            "Action": [
                "dynamodb:*",
                "cognito-idp:*",
                "cognito-identity:*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "IoTServices",
            "Effect": "Allow",
            "Action": [
                "iot:*" 
            ],
            "Resource": "*"
        },
        {
            "Sid": "StorageAndHosting",
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "cloudfront:*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "MonitoringAndLogging",
            "Effect": "Allow",
            "Action": [
                "logs:*",
                "cloudwatch:*",
                "events:*"
            ],
            "Resource": "*"
        }
    ]
}
```

14. Click **Next**

![iam_create_policy_step_1](/images/5-Workshop/5.2-Prerequisite/iam_create_policy_step_1.png)

15. For **Policy name**, enter your policy name (E.g. ```SmartOfficeAdminFullAcccess```)
16. Add **Tags** for cost and operation management (Key: ```Project```, Value: ```SmartOffice```; Key: ```Environment```, Value: ```Dev```)
17. Click **Create policy**

![iam_create_policy_step_2](/images/5-Workshop/5.2-Prerequisite/iam_create_policy_step_2.png)

18. Go back to **Step 2 Set permissions** of **Create user**
19. Search and choose your policy name
20. Click **Next**

![iam_create_user_step_2_2](/images/5-Workshop/5.2-Prerequisite/iam_create_user_step_2_2.png)

21. Add **Tags** for cost and operation management (Key: ```Project```, Value: ```SmartOffice```; Key: ```Environment```, Value: ```Dev```)
22. Click **Create user**
23. Login with your User account to begin this workhop