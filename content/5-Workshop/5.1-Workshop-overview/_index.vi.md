---
title : "Giới thiệu"
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

#### Kiến trúc Serverless & Hướng sự kiện
+ **Kiến trúc Serverless (Phi máy chủ)**: Dự án này sử dụng các dịch vụ đám mây như AWS Lambda, API Gateway và DynamoDB. Mô hình này cho phép mã chạy để phản hồi các sự kiện mà không cần quản lý hoặc cấp phát máy chủ, vì AWS sẽ xử lý toàn bộ việc mở rộng quy mô và cơ sở hạ tầng.
+ **Kiến trúc Hướng sự kiện (Event-Driven)**: Cốt lõi của hệ thống là hướng sự kiện. Thay vì các dịch vụ liên tục thăm dò (polling) lẫn nhau, các sự kiện (như một thông số cảm biến hoặc một yêu cầu của người dùng) sẽ kích hoạt các quy trình xử lý. Điều này được quản lý bởi các dịch vụ như Amazon EventBridge, SQS và AWS IoT Core, tạo nên một hệ thống linh hoạt và có khả năng mở rộng.

#### Tổng quan về workshop
Trong workshop này, bạn sẽ triển khai một nền tảng dữ liệu serverless trên AWS để xử lý dữ liệu môi trường theo thời gian thực từ 8 phòng. Hệ thống sử dụng IoT Core, Lambda, DynamoDB, S3, EventBridge, và SNS. Dữ liệu từ thiết bị edge hoặc script mô phỏng được gửi lên AWS, lưu trong DynamoDB, xử lý bằng Lambda, và được EventBridge định tuyến để gửi cảnh báo hoặc kích hoạt các quy trình tự động. Kiến trúc này đảm bảo tính sẵn sàng cao, chi phí thấp, và mở rộng dễ dàng khi tăng thêm phòng hoặc cảm biến.

![overview](/images/5-Workshop/5.1-Workshop-overview/Smart-Office-Architect-Diagram.drawio.png)
