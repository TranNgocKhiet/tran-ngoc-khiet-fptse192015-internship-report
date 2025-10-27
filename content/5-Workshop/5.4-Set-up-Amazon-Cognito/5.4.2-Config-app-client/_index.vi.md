---
title : "Cấu hình app client"
weight : 2
chapter : false
pre : " <b> 5.4.2 </b> "
---

1. Trong tab **User pools**, chọn pool bạn đã tạo 

![Cognito 4](/images/5-Workshop/5.4-Cognito/Cognito-4.png)

2. Điều hướng đến tab **App Clients**, chọn **SmartOffice**

![Cognito 5](/images/5-Workshop/5.4-Cognito/Cognito-5.png)

3. Nhấn **Edit**   

![Cognito 6](/images/5-Workshop/5.4-Cognito/Cognito-6.png)

4. Đối với **Authentication flows**:
<br> &emsp;- Bỏ chọn **Choice-based sign-in: ALLOW_USER_AUTH**
<br> &emsp;- Bỏ chọn **Sign in with username and password: ALLOW_USER_PASSWORD_AUTH**
<br> &emsp;- Bỏ chọn **Sign in with secure remote password (SRP): ALLOW_USER_SRP_AUTH**
<br> &emsp;- Chọn **Sign in with server-side administrative credentials: ALLOW_ADMIN_USER_PASSWORD_AUTH**
<br> &emsp;- Bỏ chọn **Sign in with custom authentication flows from Lambda triggers: ALLOW_CUSTOM_AUTH**
<br> &emsp;- Chọn **Get new user tokens from existing authenticated sessions: ALLOW_REFRESH_TOKEN_AUTH**

![Cognito 7](/images/5-Workshop/5.4-Cognito/Cognito-7.png)

5. Để các cài đặt khác ở mặc định
6. Nhấn **Save changes**