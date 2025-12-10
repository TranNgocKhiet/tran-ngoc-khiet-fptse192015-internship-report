---
title: "Workshop"
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Smart Office Management System Workshop

#### Tổng quan (Overview)

**Smart Office Management System** cung cấp giải pháp giám sát và quản lý môi trường thời gian thực cho văn phòng, được xây dựng hoàn toàn trên nền tảng **AWS Serverless** giúp tối ưu hóa chi phí và khả năng mở rộng.

Trong bài lab này, bạn sẽ học cách triển khai, cấu hình và kiểm thử một hệ thống IoT full-stack, cho phép các thiết bị cảm biến gửi dữ liệu lên đám mây và người quản trị có thể điều khiển thiết bị thông qua Web Dashboard.

Bạn sẽ làm việc với hai mô hình kiến trúc chính để vận hành hệ thống Smart Office:
+ **Serverless Architecture** - Sử dụng **AWS Lambda**, **API Gateway**, và **DynamoDB** để xử lý logic và lưu trữ dữ liệu. Mô hình này cho phép mã chạy để phản hồi các yêu cầu mà không cần quản lý máy chủ.
+ **Event-Driven Architecture** - Sử dụng **AWS IoT Core**, **EventBridge**, và **SNS**. Hệ thống hoạt động dựa trên sự kiện, nơi dữ liệu từ cảm biến hoặc hành động của người dùng sẽ kích hoạt các quy trình tự động hóa và gửi thông báo cảnh báo.

#### Nội dung (Content)

1. [Giới thiệu](5.1-Workshop-overview/)
2. [Các bước chuẩn bị](5.2-Prerequiste/)
3. [Thiết lập CloudFormation](5.3-Run-cloudformation-stack/)
4. [Thiết lập website](5.4-Set-up-website/)
5. [Thiết lập EventBridge và Lambda](5.5-Event-Bridge/)
6. [Thiết lập SNS](5.6-SNS/)
7. [Kiểm thử kết nối giữa website và thiết bị IoT](5.7-Test-website-iot-connection/)