---
title : "Chuẩn bị Amazon DynamoDB"
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

#### Tổng quan

- Trong phần này, bạn sẽ cấu hình các bảng Amazon DynamoDB để lưu trữ và quản lý dữ liệu Smart Office. Mỗi bảng có vai trò riêng như lưu cấu hình phòng, lịch tự động của người dùng, và log theo thời gian thực. Bạn cũng sẽ bật TTL để tự động xóa dữ liệu cũ, PITR để bảo vệ dữ liệu, và DynamoDB Streams để kích hoạt Lambda khi có thay đổi dữ liệu.

- Lý do sử dụng DynamoDB với TTL, PITR, và Streams:
<br> &emsp;- TTL (Time to Live) giúp tự động xóa dữ liệu hết hạn (ví dụ log cũ), tiết kiệm dung lượng và chi phí.
<br> &emsp;-  PITR (Point-in-Time Recovery) đảm bảo khả năng khôi phục dữ liệu trong vòng 35 ngày khi có sự cố.
<br> &emsp;-  Streams ghi nhận thay đổi dữ liệu theo thời gian thực (cả giá trị cũ và mới), giúp Lambda đồng bộ chế độ phòng hoặc lịch tự động với IoT Core ngay lập tức.
    




