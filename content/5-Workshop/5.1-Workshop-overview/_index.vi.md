---
title : "Giới thiệu"
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

#### Kiến trúc Phi Máy Chủ & Hướng Sự kiện (Serverless & Event-Driven Architecture)
+ **Kiến trúc Phi Máy Chủ (Serverless Architecture)**: Workshop này áp dụng mô hình gốc đám mây (cloud-native) với các dịch vụ như **AWS Lambda**, **Amazon API Gateway**, và **Amazon DynamoDB**. Cách tiếp cận này cho phép mã chạy để phản hồi các yêu cầu mà không cần cấp phát hay quản lý máy chủ, vì AWS sẽ xử lý tất cả việc tự động điều chỉnh quy mô và quản lý cơ sở hạ tầng.
+ **Kiến trúc Hướng Sự kiện (Event-Driven Architecture)**: Cốt lõi của hệ thống hoạt động trên cơ sở hướng sự kiện. Thay vì các dịch vụ liên tục thăm dò dữ liệu, các sự kiện cụ thể—như dữ liệu đọc từ cảm biến IoT hoặc các cuộc gọi API từ người dùng—sẽ kích hoạt các quy trình làm việc tiếp theo. Điều này được điều phối bởi **AWS IoT Core** và **Amazon EventBridge**, tạo ra một hệ thống có tính linh hoạt và khả năng mở rộng cao.

#### Tổng quan về Workshop (Workshop Overview)
Trong workshop này, bạn sẽ triển khai một nền tảng dữ liệu phi máy chủ toàn diện trên AWS để quản lý giám sát môi trường theo thời gian thực cho **thiết lập văn phòng thông minh 8 phòng**. Hệ thống tích hợp **AWS IoT Core**, **Lambda**, **DynamoDB**, **S3**, **CloudFront**, và **Amazon Cognito**. Dữ liệu cảm biến được chuyển tiếp từ thiết bị biên (hoặc tập lệnh mô phỏng), được đưa vào AWS, lưu trữ trong các bảng DynamoDB và được xử lý bởi các hàm Lambda để cập nhật bảng điều khiển quản lý. Các sự kiện quan trọng được định tuyến qua EventBridge để kích hoạt cảnh báo, thể hiện một kiến trúc có tính sẵn sàng cao, chi phí thấp và khả năng mở rộng liền mạch.

![overview](/images/5-Workshop/5.1-Workshop-overview/Smart-Office-Architect-Diagram.drawio.png)
