---
title : "Chuẩn bị Amazon Cognito"
weight : 4 
chapter : false
pre : " <b> 5.4. </b> "
---

#### Tổng quan

- Trong phần này, bạn sẽ cấu hình **Amazon Cognito User Pool** để quản lý và xác thực tất cả người dùng cho Smart Office. Dịch vụ này xác thực thông tin đăng nhập của người dùng (email/mật khẩu) thông qua **Lambda `AuthenticateHandler`** và cấp **JSON Web Tokens (JWT)** khi đăng nhập thành công. Bạn cũng sẽ cấu hình User Pool này làm **API Gateway Authorizer** để bảo mật tất cả các API endpoint được bảo vệ.

- Tại sao sử dụng Kiến trúc Cognito này:
<br> &emsp;- **Luồng `ADMIN_NO_SRP_AUTH`** tập trung logic xác thực vào bên trong Lambda `AuthenticateHandler`, tăng cường bảo mật bằng cách giữ logic nhạy cảm của app client và thông tin đăng nhập (credentials) khỏi frontend.
<br> &emsp;- **JWT (JSON Web Tokens)** cung cấp một "hộ chiếu" an toàn, không trạng thái (stateless) mà frontend sử dụng để chứng minh danh tính cho tất cả các lệnh gọi API tiếp theo.
<br> &emsp;- **API Gateway Authorizer** tự động xác thực JWT trên mọi yêu cầu, chặn truy cập trái phép vào các API được bảo vệ (như điều khiển thiết bị) trước khi chúng có thể được thực thi.




