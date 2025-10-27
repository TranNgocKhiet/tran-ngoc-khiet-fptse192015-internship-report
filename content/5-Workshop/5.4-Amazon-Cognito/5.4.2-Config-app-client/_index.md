---
title : "Config app client"
weight : 2
chapter : false
pre : " <b> 5.4.2 </b> "
---

1. In tab **User pools**, choose the pool you have created 

![Cognito 4](/images/5-Workshop/5.4-Cognito/Cognito-4.png)

2. Navigate to tab **App Clients**, choose **SmartOffice**

![Cognito 5](/images/5-Workshop/5.4-Cognito/Cognito-5.png)

3. Click **Edit**   

![Cognito 6](/images/5-Workshop/5.4-Cognito/Cognito-6.png)

4. For **Authentication flows**:
<br> &emsp;- Uncheck **Choice-based sign-in: ALLOW_USER_AUTH**
<br> &emsp;- Uncheck **Sign in with username and password: ALLOW_USER_PASSWORD_AUTH**
<br> &emsp;- Uncheck **Sign in with secure remote password (SRP): ALLOW_USER_SRP_AUTH**
<br> &emsp;- Check **Sign in with server-side administrative credentials: ALLOW_ADMIN_USER_PASSWORD_AUTH**
<br> &emsp;- Uncheck **Sign in with custom authentication flows from Lambda triggers: ALLOW_CUSTOM_AUTH**
<br> &emsp;- Check **Get new user tokens from existing authenticated sessions: ALLOW_REFRESH_TOKEN_AUTH**

![Cognito 7](/images/5-Workshop/5.4-Cognito/Cognito-7.png)

5. Leave other settings at default
6. Click **Save changes**