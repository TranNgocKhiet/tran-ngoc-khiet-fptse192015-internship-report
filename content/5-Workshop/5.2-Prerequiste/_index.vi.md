---
title : "Các bước chuẩn bị"
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

#### Tạo IAM User cho workshop này

1. Trong **AWS Management Console**, tìm kiếm và chọn **IAM**

![iam_mangement_console](/images/5-Workshop/5.2-Prerequisite/iam_mangement_console.png)

2. Điều hướng đến **User**, nhấp vào **Create user**

![iam_create_user](/images/5-Workshop/5.2-Prerequisite/iam_create_user.png)

3. Tại mục **User name**, nhập `admin-user`
4. Tích chọn **Provide user access to the AWS Management Console - optional**
5. Tại mục **Console password**, chọn **Custom password**
6. Nhập mật khẩu cho user của bạn
7. Bỏ chọn **Users must create a new password at next sign-in - Recommended** để thao tác dễ dàng hơn
8. Nhấp **Next**

![iam_create_user_step_1](/images/5-Workshop/5.2-Prerequisite/iam_create_user_step_1.png)

9. Tại mục **Permissions options**, chọn **Attach policies directly**
10. Nhấp **Create policy**

![iam_create_user_step_2_1](/images/5-Workshop/5.2-Prerequisite/iam_create_user_step_2_1.png)

11. Bạn sẽ được điều hướng đến trang **Create policy**
12. Tại mục **Policy editor**, chuyển sang **JSON**
13. Sao chép và dán đoạn policy này vào

```json
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

14. Nhấp **Next**

![iam_create_policy_step_1](/images/5-Workshop/5.2-Prerequisite/iam_create_policy_step_1.png)

15. Tại mục **Policy name**, nhập tên policy của bạn (Ví dụ: `SmartOfficeAdminFullAcccess`)
16. Thêm **Tags** để quản lý chi phí và vận hành (Key: `Project`, Value: `SmartOffice`; Key: `Environment`, Value: `Dev`)
17. Nhấp **Create policy**

![iam_create_policy_step_2](/images/5-Workshop/5.2-Prerequisite/iam_create_policy_step_2.png)

18. Quay lại **Step 2 Set permissions** của phần **Create user**
19. Tìm kiếm và chọn tên policy của bạn
20. Nhấp **Next**

![iam_create_user_step_2_2](/images/5-Workshop/5.2-Prerequisite/iam_create_user_step_2_2.png)

21. Thêm **Tags** để quản lý chi phí và vận hành (Key: `Project`, Value: `SmartOffice`; Key: `Environment`, Value: `Dev`)
22. Nhấp **Create user**
23. Đăng nhập bằng tài khoản User của bạn để bắt đầu workshop này