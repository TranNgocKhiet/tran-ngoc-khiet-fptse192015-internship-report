---
title: "Nhật ký công việc"
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

## Tổng quan Nhật ký Công việc Thực tập

Phần này ghi lại hành trình thực tập 13 tuần tại **CÔNG TY CỔ PHẦN AMAZON WEB SERVICES VIỆT NAM** (06/08/2025 - 12/24/2025). Chương trình bao gồm các module AWS nền tảng (Tuần 1-8) tiếp theo là triển khai dự án Smart Office IoT thực tế (Tuần 6-13).

---

### **Tuần 1-5: Nền tảng AWS**

**[Tuần 1: Nền tảng AWS & Cài đặt Tài khoản](1.1-week1/)**
- Thiết lập môi trường AWS an toàn với MFA và cảnh báo lập hóa đơn
- Xây dựng mạng cơ bản: VPC, Public Subnet, Internet Gateway
- Khởi chạy EC2 instance trong public subnet với SSH access
- Tạo và kiểm thử Lambda function cơ bản
- *Thành tích:* Nền tảng cơ sở hạ tầng đám mây được thiết lập

**[Tuần 2: Linux, Python, IAM & Cơ sở dữ liệu](1.2-week2/)**
- Nắm vững điều hướng hệ thống tệp Linux và quyền trên EC2
- Viết script Python với biến và hàm
- Tạo IAM Users, Groups và các chính sách JSON tùy chỉnh
- Gắn các role IAM vào EC2 để truy cập S3 an toàn
- Tìm hiểu kiến thức cơ bản về cơ sở dữ liệu RDS
- *Thành tích:* Khả năng scripting và quản lý danh tính

**[Tuần 3: Lưu trữ, Cơ sở dữ liệu & API](1.3-week3/)**
- Cài đặt và chạy các ứng dụng Node.js
- Quản lý các bucket S3 với Versioning và Lifecycle policies
- Tạo và điền dữ liệu vào bảng NoSQL DynamoDB
- Nghiên cứu giao thức MQTT cho kết nối IoT
- *Thành tích:* Hiểu biết toàn diện về lưu trữ và cơ sở dữ liệu

**[Tuần 4: Serverless & Kiến trúc Hướng sự kiện](1.4-week4/)**
- Tạo Lambda function Python và kiểm thử thông qua console
- Cấu hình S3 events để kích hoạt Lambda tự động
- Expose Lambda function thông qua API Gateway
- Củng cố kiến thức mạng VPC với private subnets
- Thiết kế mô hình kiến trúc IoT hướng sự kiện
- *Thành tích:* Ứng dụng serverless hướng sự kiện

**[Tuần 5: Dịch vụ Nhắn tin & Chuẩn bị Dự án](1.5-week5/)**
- Cấu hình SNS topics và đăng ký email
- Tạo các sự kiện theo lịch trình bằng EventBridge với biểu thức Cron
- Có được sự hiểu biết lý thuyết về AWS IoT Core
- Xem xét lại JSON, chính sách IAM và cú pháp Python
- *Thành tích:* Hoàn toàn chuẩn bị cho khởi động dự án Smart Office

---

### **Tuần 6-13: Triển khai Dự án Smart Office IoT**

**[Tuần 6: Cài đặt Môi trường IoT Core](1.6-week6/)**
- Khởi tạo môi trường AWS IoT Core
- Tạo Thing Type và đăng ký "Things" (cảm biến mô phỏng)
- Tạo và bảo mật chứng chỉ và khóa thiết bị
- Gắn chính sách IoT cho phép Connect, Publish, Subscribe
- Xác minh kết nối bằng MQTT Test Client
- *Thành tích:* Cơ sở hạ tầng IoT an toàn được thiết lập

**[Tuần 7: Sâu về Bảo mật & Khả năng Phục hồi](1.7-week7/)**
- Nghiên cứu chính sách IAM, mã hóa (KMS, TLS) và Secrets Manager
- So sánh Security Groups vs NACLs (stateful vs stateless)
- Xem xét dịch vụ bảo mật AWS WAF, Shield và GuardDuty
- Nắm vững khái niệm High Availability và Disaster Recovery
- Cấu hình Route 53 routing policies và chiến lược sao lưu
- *Thành tích:* Kiến thức bảo mật cấp doanh nghiệp

**[Tuần 8: Hiệu suất, Tối ưu hóa Chi phí & Kỳ thi Giữa kỳ](1.8-week8/)**
- So sánh các loại lưu trữ: S3 (classes), EFS, EBS
- Xem xét lại triển khai RDS read replicas và Multi-AZ
- Nghiên cứu tối ưu hóa chi phí: Cost Explorer, Budgets, Savings Plans, S3 Lifecycle
- Hợp nhất AWS Well-Architected Framework (6 trụ cột)
- **Hoàn thành thành công kỳ thi Giữa kỳ**
- *Thành tích:* Nắm vững kiến trúc AWS toàn diện

**[Tuần 9: Nhắn tin MQTT & Mô phỏng Dữ liệu](1.9-week9/)**
- Xác định cấu trúc chủ đề MQTT hợp lý (ví dụ: `office/room1/temp`)
- Viết script Python bằng AWSIoTPythonSDK với chứng chỉ thiết bị
- Triển khai mô phỏng dữ liệu telemetry JSON ngẫu nhiên
- Xác minh luồng dữ liệu bằng AWS Console MQTT client
- Thêm logic threading cho mô phỏng đa thiết bị
- *Thành tích:* Luồng dữ liệu cảm biến thực tế đến AWS

**[Tuần 10: IoT Rules & Tích hợp EventBridge](1.10-week10/)**
- Cấu hình AWS IoT Rules Engine với lọc SQL
- Tạo quy tắc định tuyến tin nhắn MQTT đến EventBridge
- Thiết kế mô hình EventBridge để phát hiện bất thường (ví dụ: Nhiệt độ cao > 40°C)
- Xác minh số liệu quy tắc và khớp sự kiện
- *Thành tích:* Đường ống xử lý dữ liệu thời gian thực

**[Tuần 11: Gỡ rối, Tinh chỉnh Mã & Kiểm thử](1.11-week11/)**
- Sửa lỗi trong chính sách IoT và quyền thiết bị
- Triển khai logic lập lịch cho chu kỳ ON/OFF thiết bị
- Tái cấu trúc và bình luận mã Python một cách rộng rãi
- Kiểm thử các trường hợp biên và xác thực hệ thống
- *Thành tích:* Hệ thống Smart Office sẵn sàng sản xuất

**[Tuần 12: Linux & Làm chủ Shell Scripting](1.12-week12/)**
- Hoàn thành khóa học Coursera: "Hands-on Introduction to Linux Commands and Shell Scripting"
- Nắm vững thao tác tệp, quyền, piping và shell scripting
- Xây dựng nền tảng vững chắc cho DevOps và tự động hóa cơ sở hạ tầng
- *Thành tích:* Chuyên môn Linux và tự động hóa

**[Tuần 13: Kiểm thử Cuối cùng, Workshop & Thuyết trình](1.13-week13/)**
- Tiến hành kiểm thử hệ thống end-to-end rộng rãi
- Xác minh luồng dữ liệu Frontend-to-Backend
- Kiểm thử lập lịch thiết bị thông qua điều khiển Frontend
- Tạo tài liệu workshop toàn diện
- Tạo video demo giới thiệu khả năng hệ thống
- Chuẩn bị và thực hiện thuyết trình cuối cùng
- **Hoàn thành Dự án:** Hệ thống Smart Office IoT được giao
- *Thành tích:* Giao hàng dự án thành công và truyền tải kiến thức

---

## Dự án: Hệ thống Smart Office IoT

### Tổng quan
Một giải pháp IoT hoàn chỉnh tích hợp:
- **AWS IoT Core** để quản lý thiết bị và nhắn tin MQTT
- **EventBridge** để xử lý dữ liệu hướng sự kiện
- Các hàm **Lambda** để chuyển đổi dữ liệu
- **SNS** để gửi thông báo cảnh báo
- **Ứng dụng Web Frontend** để giám sát thời gian thực và điều khiển thiết bị

### Những Bài Học Chính
✅ Thiết kế kiến trúc đám mây từ đầu đến cuối  
✅ Quản lý thiết bị IoT an toàn và xác thực dựa trên chứng chỉ  
✅ Điện toán serverless hướng sự kiện  
✅ Truyền phát và xử lý dữ liệu thời gian thực  
✅ Thực tiễn tốt nhất về bảo mật (IAM, mã hóa, nguyên tắc tối thiểu đặc quyền)  
✅ Nguyên tắc Well-Architected (Bảo mật, Độ tin cậy, Hiệu suất, Tối ưu hóa Chi phí)

---

**Để biết thêm chi tiết về các hoạt động hàng ngày, hãy xem báo cáo tuần lẻ [Tuần 1](1.1-week1/) đến [Tuần 13](1.13-week13/)**