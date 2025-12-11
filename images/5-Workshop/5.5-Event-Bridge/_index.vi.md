---
title : "Event Bridge"
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---

#### Tổng quan
Phần này sẽ hướng dẫn cách thiết lập **Amazon EventBridge** để định tuyến và phản hồi các sự kiện trong kiến trúc workshop. Thêm hướng dẫn chi tiết ở đây.

#### Yêu cầu trước
- Tài khoản AWS với quyền IAM phù hợp (EventBridge, Lambda, IAM, CloudWatch).
- AWS CLI đã cấu hình hoặc sử dụng giao diện console.

#### Các bước mẫu (mẫu placeholder)
1. Tạo (hoặc dùng) một Event Bus tùy chỉnh.

```
aws events create-event-bus --name SmartOfficeBus
```

2. Tạo rule để khớp sự kiện và gửi đến target (Lambda/SQS/SNS).

3. Thêm target vào rule (ví dụ: Lambda) và cấp quyền cho EventBridge gọi Lambda.

4. Gửi sự kiện thử nghiệm:

```
aws events put-events --entries '[{"Source":"my.source","DetailType":"TestEvent","Detail":"{\"msg\":\"hello\"}","EventBusName":"SmartOfficeBus"}]'
```

#### Kiểm tra
- Kiểm tra CloudWatch Logs của Lambda target để xác nhận nhận sự kiện.

{{% notice warning %}}
Thay thế `REGION` và `ACCOUNT` bằng thông tin tương ứng của bạn. Cập nhật ARN cho phù hợp.
{{% /notice %}}

#### Dọn dẹp
- Xoá targets, rule và event bus sau khi hoàn tất kiểm thử để tránh phát sinh chi phí.
