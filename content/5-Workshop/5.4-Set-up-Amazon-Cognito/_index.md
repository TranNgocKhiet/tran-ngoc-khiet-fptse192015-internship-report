---
title : "Set up Amazon Cognito"
weight : 4
chapter : false
pre : " <b> 5.4. </b> "
---

#### Overview

- In this section, you will configure **Amazon Cognito User Pool** to manage and authenticate all users for the Smart Office. This service validates user credentials (email/password) via the **`AuthenticateHandler` Lambda** and issues **JSON Web Tokens (JWT)** upon successful login. You will also configure this User Pool as an **API Gateway Authorizer** to secure all protected API endpoints.

- Why using this Cognito Architecture:
<br> &emsp;- **`ADMIN_NO_SRP_AUTH` Flow** centralizes authentication logic within the `AuthenticateHandler` Lambda, enhancing security by keeping sensitive app client logic and credentials off the frontend.
<br> &emsp;- **JWT (JSON Web Tokens)** provide a stateless, secure "passport" that the frontend uses to prove identity for all subsequent API calls.
<br> &emsp;- **API Gateway Authorizer** automatically validates the JWT on every request, blocking unauthorized access to protected APIs (like controlling devices) before they can execute.



