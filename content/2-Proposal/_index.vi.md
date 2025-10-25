---
title: "Bản đề xuất"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# Smart Office Management Console
## Giải pháp AWS Serverless hợp nhất cho giám sát và điều khiển văn phòng thông minh theo thời gian thực 

### 1. Tóm tắt điều hành  
Hệ thống Smart Office Management Console được phát triển dựa trên ý tưởng từ những chuyến thăm định kỳ đến văn phòng AWS tại TP. Hồ Chí Minh. Giải pháp hỗ trợ tự động hóa văn phòng thông qua các thiết bị thông minh như đèn, cửa sổ cảm biến, và máy điều hòa, bằng cách thu thập, truyền và xử lý dữ liệu từ cảm biến IoT. Hệ thống sử dụng kiến trúc AWS Serverless, cho phép truyền dữ liệu qua MQTT và xử lý định kỳ mỗi 5 phút để cung cấp giám sát thời gian thực, điều khiển dựa trên dự đoán thời tiết, tiết kiệm chi phí điện năng, đồng thời giới hạn truy cập cho người dùng được xác thực qua Amazon Cognito.

### 2. Tuyên bố vấn đề  
#### Vấn đề hiện tại
Phần lớn các văn phòng hiện nay vẫn phải điều khiển thủ công các thiết bị như đèn, cửa sổ, và máy lạnh. Các thiết bị thường được bật liên tục trong giờ làm việc (8:00–17:00), ngay cả khi không cần thiết. Ví dụ, ánh sáng tự nhiên từ 10:00–15:00 có thể đủ sáng để không cần đèn, hoặc độ ẩm cao trong mùa mưa có thể tạo môi trường mát mẻ tương tự điều hòa. Việc điều khiển tự động dựa trên điều kiện môi trường giúp tiết kiệm năng lượng và chi phí vận hành.

#### Giải pháp
Nền tảng sử dụng AWS IoT Core để tiếp nhận dữ liệu MQTT, AWS Lambda và API Gateway để xử lý, DynamoDB để lưu trữ dữ liệu, Amazon S3 để lưu trữ và cung cấp giao diện web, Amazon Cognito để xác thực truy cập, và AWS SNS để gửi thông báo khi phát hiện bất thường hoặc điều kiện thời tiết đặc biệt. Giống như Thingsboard và CoreIoT, hệ thống cho phép đăng ký thiết bị mới và quản lý kết nối, nhưng hoạt động ở quy mô nhỏ hơn, phục vụ cho môi trường nội bộ. Các tính năng chính bao gồm giám sát thời gian thực, dự báo thời tiết, điều khiển tự động và chi phí vận hành thấp.

#### Lợi ích và hoàn vốn đầu tư (ROI)
Giải pháp giúp nâng cao tự động hóa, giám sát, và hiệu quả năng lượng trong môi trường văn phòng, đồng thời là nền tảng nghiên cứu và mở rộng ứng dụng IoT thực tế. Hệ thống cung cấp nền tảng tập trung, giảm cấu hình thủ công, cải thiện độ tin cậy dữ liệu và đơn giản hóa bảo trì.

Chi phí vận hành hàng tháng ước tính 11,81 USD (bao gồm DynamoDB, IoT Core, CloudFront, CloudWatch và SNS), tương đương 21,72 USD mỗi năm. Do các thiết bị IoT đã được triển khai, không phát sinh chi phí phần cứng. Thời gian hoàn vốn từ 6–12 tháng, nhờ tiết kiệm thời gian và chi phí vận hành, đảm bảo khả năng mở rộng và hiệu quả lâu dài.

### 3. Kiến trúc giải pháp  
Hệ thống áp dụng kiến trúc AWS Serverless tối ưu chi phí và khả năng mở rộng. Dữ liệu từ nhiều trạm cảm biến được gửi đến AWS IoT Core, xử lý bằng Lambda, và lưu trữ trong DynamoDB để giám sát thời gian thực. EventBridge tự động kích hoạt các tác vụ định kỳ và phát hiện bất thường, trong khi SNS gửi thông báo. Giao diện web được lưu trữ trên S3 và phân phối qua CloudFront, được bảo mật bởi Cognito.

![Sơ đồ kiến trúc](/images/2-Proposal/Smart-Office-Architect-Diagram.drawio.png)

#### Dịch vụ AWS sử dụng
- **AWS IoT Core**: Tiếp nhận và quản lý dữ liệu MQTT từ 8 trạm cảm biến.
- **AWS Lambda**: Xử lý dữ liệu, cập nhật cấu hình, và điều khiển tự động.
- **Amazon API Gateway**: Kết nối frontend và backend qua RESTful API.
- **Amazon DynamoDB**: Lưu trữ hồ sơ người dùng, cấu hình phòng, và nhật ký cảm biến.
- **Amazon EventBridge**: Kích hoạt các tác vụ định kỳ và phát hiện bất thường.
- **Amazon SNS**: Gửi thông báo khi phát hiện sự kiện bất thường.
- **Amazon S3**: Lưu trữ bảng điều khiển web và các tài nguyên tĩnh.
- **Amazon CloudFront**: Phân phối nội dung toàn cầu qua HTTPS với độ trễ thấp.
- **Amazon Cognito**: Quản lý xác thực người dùng.
- **Amazon CloudWatch**: Theo dõi và ghi nhật ký hoạt động.

#### Thiết kế thành phần
- **Sensor Hubs**: Each IoT-enabled room device collects environmental data (temperature, humidity, light, etc.) and sends it to **AWS IoT Core** every two minutes.  
- **Data Ingestion**: **AWS IoT Core** routes incoming MQTT messages to the **SensorProcessor Lambda**, which validates and logs the data into **Amazon DynamoDB**.  
- **Configuration Management**: The **RoomConfigHandler Lambda** updates room settings (auto/manual modes, thresholds, timers) in **DynamoDB** when users make changes through the dashboard.  
- **Automation Control**: **AutomationSetup Lambda** listens to **DynamoDB Streams** for configuration updates and registers automation events in **Amazon EventBridge**.  
- **Event Handling**: **EventBridge** triggers **AutomationHandler Lambda** at scheduled times or when anomalies are detected, sending alerts via **Amazon SNS** if needed.  
- **User Interaction**: The **web dashboard** (hosted on **Amazon S3** and delivered via **CloudFront**) allows users to view sensor data and manage configurations.  
- **User Authentication**: **Amazon Cognito** secures user access with sign-up, sign-in, and token-based authorization integrated through **API Gateway**.  
- **Monitoring & Reliability**: **Amazon CloudWatch** collects logs and metrics from all **Lambda functions**, with **SQS** queues as **DLQs** to capture failed executions for debugging.  

### 4. Triển khai kỹ thuật  
#### Giai đoạn triển khai
- Nghiên cứu và thử nghiệm dịch vụ AWS: IoT Core, Lambda, S3, API Gateway, EventBridge, CloudFront, Cognito (7 tuần).
Thiết kế kiến trúc và ước tính chi phí: Dựng sơ đồ cho văn phòng 8 phòng, tính toán bằng AWS Pricing Calculator (1 tuần).
- Phát triển và tối ưu: Viết script mô phỏng dữ liệu cảm biến, phát triển Lambda, kết nối API Gateway và DynamoDB (3 tuần).
- Kiểm thử và triển khai: Kiểm thử hệ thống, xác nhận quy trình dữ liệu và giám sát kết quả trên dashboard (1 tuần).

#### Yêu cầu kỹ thuật
- Thiết bị cảm biến: ESP32 hoặc tương đương, gửi dữ liệu qua MQTT mỗi 2 phút.
- Hệ thống AWS: IoT Core, Lambda, DynamoDB, S3, API Gateway, EventBridge, SNS, CloudFront, Cognito.
- Triển khai: Dùng AWS CDK/SDK; giao diện Next.js triển khai trên S3 + CloudFront; xác thực bằng Cognito.

### 5. Lộ trình & Mốc triển khai  
#### Lộ trình
- Tuần 1–7: Nghiên cứu dịch vụ AWS.
- Tuần 8: Thiết kế kiến trúc, ước tính chi phí.
- Tuần 9–11: Phát triển, tích hợp, cấu hình hệ thống.
- Tuần 12: Kiểm thử, khắc phục lỗi, triển khai chính thức.

### 6. Ước tính ngân sách  
Có thể xem chi phí trên [AWS Pricing Calculator](https://calculator.aws/#/estimate?id=0db12150c448b012356e475becefd549c37094d8)  
Hoặc tải [tệp ước tính ngân sách](/file/f8e2d281-aba2-48c2-adf8-d8ec828d2ec9.pdf).  

#### Chi phí hạ tầng
- DynamoDB: 0,09 USD/tháng.
- IoT Core: 0,18 USD/tháng.
- CloudFront: 1,27 USD/tháng.
- CloudWatch: 0,25 USD/tháng.
- SNS: 0,02 USD/tháng.
- Các dịch vụ khác: Miễn phí (trong Free Tier).
Tổng cộng: ≈ 1,81 USD/tháng, tương đương 21,72 USD/năm.

### 7. Đánh giá rủi ro  
#### Ma trận rủi ro
- Mất kết nối IoT: Ảnh hưởng trung bình, xác suất trung bình.
- Lỗi phần cứng cảm biến: Ảnh hưởng cao, xác suất thấp.
- Phát sinh chi phí AWS bất ngờ: Ảnh hưởng trung bình, xác suất thấp.
- Dữ liệu sai lệch hoặc chậm trễ: Ảnh hưởng trung bình, xác suất trung bình.

#### Chiến lược giảm thiểu
- Lưu trữ tạm tại cảm biến khi mất kết nối.
- Duy trì thiết bị dự phòng, kiểm tra định kỳ.
- Theo dõi chi phí bằng AWS Budgets.
- Xác minh dữ liệu tại Lambda trước khi lưu vào DynamoDB.

#### Kế hoạch dự phòng
- Chuyển sang chế độ thủ công nếu hệ thống IoT ngừng hoạt động.
- Kích hoạt cảnh báo qua CloudWatch khi lỗi xảy ra.
- Sử dụng CloudFormation/CDK rollback để khôi phục nhanh cấu hình.

### 8. Kết quả kỳ vọng  
#### Cải tiến kỹ thuật:
- Giám sát và điều khiển thời gian thực thay thế hoàn toàn việc vận hành thủ công trong từng phòng.
- Nền tảng tập trung giúp nâng cao độ chính xác và tính nhất quán của dữ liệu.
- Kiến trúc linh hoạt, có khả năng mở rộng để tích hợp thêm nhiều phòng hoặc thiết bị IoT khác trong tương lai.

#### Giá trị dài hạn:
- Cung cấp nền tảng có thể tái sử dụng cho nghiên cứu và phát triển các giải pháp tòa nhà thông minh và tự động hóa IoT.
- Cho phép phân tích dữ liệu để tối ưu hiệu suất năng lượng và điều kiện môi trường.
- Minh chứng cho một kiến trúc AWS serverless hoàn chỉnh, chi phí thấp (dưới 2 USD mỗi tháng).