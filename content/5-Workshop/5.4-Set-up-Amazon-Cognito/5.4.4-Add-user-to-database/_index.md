---
title : "Add user to database"
weight : 4
chapter : false
pre : " <b> 5.4.4 </b> "
---

1. In tab **Users**, choose the User you have created

![Cognito 10](/images/5-Workshop/5.4-Cognito/Cognito-10.png)

2. Copy **User ID (Sub)** and **email**
3. Open **Management Console**, search and choose ```DynamoDB```
4. Navigate to tab **Tables**, choose **SmartOffice_User_Prod**
5. Choose **Action**, **Create item**
6. Choose **JSON view**, turn off **View DynamoDB JSON**
7. Enter this JSON with copied **userId** and **email**
```
{
 "userId": "",
 "companyId": "comp-abc",
 "name": "Nguyen Van B",
 "email": "",
 "role": "user",
 "offices": [
  "office-hcm"
 ]
}
```

![Cognito 11](/images/5-Workshop/5.4-Cognito/Cognito-11.png)

8. Click **Create item**