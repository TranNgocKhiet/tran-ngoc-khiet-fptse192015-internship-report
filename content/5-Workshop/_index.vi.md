---
title: "Workshop"
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Nền tảng IoT Văn phòng Thông minh không máy chủ

#### Tổng quan

Workshop này trình bày cách xây dựng một **nền tảng dữ liệu không máy chủ toàn diện** trên AWS để giám sát môi trường thời gian thực. Hệ thống triển khai một **kiến trúc hướng sự kiện và không máy chủ** hiện đại sử dụng các dịch vụ AWS gốc đám mây.

**Các nguyên tắc kiến trúc chính:**
+ **Kiến trúc không máy chủ** - Sử dụng **AWS Lambda**, **Amazon API Gateway**, và **Amazon DynamoDB** để chạy mã mà không cần cấp phát máy chủ. AWS tự động xử lý việc mở rộng quy mô và quản lý cơ sở hạ tầng.
+ **Kiến trúc hướng sự kiện** - Thay vì bẻ phi phiếu liên tục, các sự kiện cụ thể (đọc cảm biến IoT, lệnh gọi API của người dùng) kích hoạt các quy trình. **AWS IoT Core** và **Amazon EventBridge** điều phối các sự kiện này để đạt được tính linh hoạt và khả năng mở rộng.

**Các thành phần hệ thống:**
Nền tảng quản lý một **thiết lập văn phòng thông minh 8 phòng** tích hợp **AWS IoT Core** để nhập liệu cảm biến, các hàm **Lambda** để xử lý, **DynamoDB** để lưu trữ, **S3** và **CloudFront** để lưu trữ trang web, và **Amazon Cognito** để xác thực. Dữ liệu cảm biến từ các thiết bị biên chạy vào AWS, được lưu trữ và xử lý, cập nhật bảng điều khiển quản lý, và định tuyến các sự kiện quan trọng qua EventBridge để cảnh báo.

#### Nội dung

1. [Tổng quan về workshop](5.1-Workshop-overview/)
2. [Điều kiện tiên quyết](5.2-Prerequiste/)
3. [Chạy ngăn xếp CloudFormation](5.3-Run-cloudformation-stack/)
4. [Thiết lập trang web](5.4-Set-up-website/)
5. [Thiết lập EventBridge và Lambda](5.5-Event-Bridge/)
6. [Thiết lập SNS](5.6-SNS/)
7. [Kiểm tra trang web và kết nối IoT](5.7-Test-website-iot-connection/)