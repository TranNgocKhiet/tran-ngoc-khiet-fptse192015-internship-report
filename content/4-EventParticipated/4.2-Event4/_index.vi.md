---
title: "Event 4"
weight: 4
chapter: false
pre: " <b> 4.4. </b> "
---

# Báo Cáo Tổng Hợp: "AWS Cloud Mastery Series #3: Theo AWS Well-Architected Security Pillar"

### Mục Đích Của Sự Kiện

- Nền tảng bảo mật
- Quản lý danh tính & truy cập
- Phát hiện
- Bảo vệ cơ sở hạ tầng
- Bảo vệ dữ liệu
- Ứng phó sự cố

### Danh Sách Diễn Giả

- Le Vu Xuan An
- Tran Duc Anh
- Tran Doan Cong Ly
- Danh Hoang Hieu Nghi
- Thinh Lam
- Viet Nguyen
- Mendel Branski (Long)

### Nội Dung Nổi Bật

#### Giới thiệu về Cloud Club

- Giới thiệu một số Cloud Club tại các trường đại học như UTE, SGU
- Các hoạt động tại Cloud Club

#### Nền tảng bảo mật

- Chính sách kiểm soát dịch vụ 
- Ranh giới phân quyền 
- Xác thực đa yếu tố (MFA)

#### Phát hiện và giám sát

- Khả năng hiển thị bảo mật đa lớp
- Cảnh báo & Tự động hóa với EventBridge
- Detection-as-code

#### Bảo vệ mạng và dữ liệu

- Chia sẻ VPC Security Group
- Các dịch vụ dựa trên API
- Quản lý bí secrets (Secret Management)

#### Ứng phó sự cố

- Phòng ngừa - Không ai có thời gian cho các sự cố
- Hướng dẫn để "ngủ ngon hơn"
- Quy trình ứng phó sự cố

### Những Gì Học Được

#### Service Control Policies (SCP)

- Chính sách tổ chức
- Kiểm soát quyền tối đa khả dụng cho tất cả tài khoản trong tổ chức
- Không bao giờ cấp quyền, nó chỉ có thể lọc (giới hạn) quyền

#### Permission Boundaries

- Tính năng IAM nâng cao được thiết kế để giải quyết vấn đề bảo mật trung tâm duy nhất
- Thiết lập các quyền tối đa mà chính sách dựa trên danh tính (identity-based policy) có thể cấp cho một Người dùng/Vai trò

#### Xác thực đa yếu tố (MFA)

- TOTP: Bí mật được chia sẻ, yêu cầu mã thủ công 6 chữ số (Google Authenticator), miễn phí, sao lưu và khôi phục linh hoạt
- FIDO2: Mã hóa khóa công khai, yêu cầu quét sinh trắc học chạm đơn giản, đa dạng, sao lưu và khôi phục nghiêm ngặt

#### Cảnh báo & Tự động hóa với EventBridge

- Sự kiện thời gian thực: Các sự kiện CloudTrail chuyển đến EventBridge để xử lý ngay lập tức
- Cảnh báo tự động: Phát hiện các hoạt động đáng ngờ trên tất cả tài khoản của tổ chức
- Định tuyến sự kiện liên tài khoản: Xử lý sự kiện tập trung và phản hồi tự động
- Tích hợp & Quy trình làm việc: Tích hợp SNS, Slack, SQS cho phản hồi bảo mật tự động và thông báo cho nhóm
  
#### Detection-as-Code

- CloudFormation/Terraform: Triển khai GuardDuty trên toàn tổ chức bằng IaC (bật các kế hoạch bảo vệ, cấu hình nguồn dữ liệu)
- Quy tắc phát hiện tùy chỉnh: Xây dựng các quy tắc ngăn chặn & danh sách trắng IP để giảm dương tính giả và thích ứng với môi trường của bạn
- Cơ sở hạ tầng như mã (IaC): Thiết lập GuardDuty và triển khai kế hoạch bảo vệ tự động trên toàn tổ chức
- Logic được kiểm soát phiên bản: Theo dõi các quy tắc phát hiện trong Git để tích hợp vào đường ống DevSecOps cho việc kiểm thử & triển khai quy tắc

#### Ứng phó sự cố

- Chuẩn bị trình xử lý tự động cho sự cố
- Dự đoán sự cố trong tương lai và thiết kế kế hoạch ứng phó
- Bài học rút ra sau mỗi sự cố

### Áp dụng vào công việc

- Chỉ định chính sách đặc quyền tối thiểu (least privilege) cho dự án
- Áp dụng MFA cho mọi tài khoản
- Dự đoán và chuẩn bị cho sự cố trong tương lai

### Trải nghiệm trong event

Tham gia workshop **“Theo AWS Well-Architected Security Pillar”** giúp tôi nâng cao kiến thức về bảo mật và ứng phó sự cố thông qua việc trải nghiệm các Trụ cột Bảo mật AWS, bao gồm:

#### Học hỏi từ các diễn giả có chuyên môn cao

- Học cách các chuyên gia (senior) xử lý khi sự cố xảy ra và bài học rút ra sau đó
- Học cách bảo vệ dữ liệu và mạng với các tính năng bảo mật của AWS

#### Khám phá một số hoạt động của Cloud Club

- Giới thiệu các hoạt động của Cloud Club giúp kết nối người học AWS từ khắp mọi nơi

#### Cảnh báo & Tự động hóa

- Chuẩn bị cơ sở hạ tầng như CloudTrail, EventBridge, CloudWatch để quản lý tài nguyên trong thời gian thực ngay khi sự cố xảy ra

#### Một số hình ảnh khi tham gia sự kiện

![piture_1](/images/event-4/3a8ff2ca-21b1-490b-a3e0-4c7bafeb2ac0.jpeg)
![piture_2](/images/event-4/8eb6febb-c015-41a3-a1c8-16a78d59edd6.jpeg)
![piture_3](/images/event-4/22b0e28c-748a-4ad9-a5ac-3a9373cece83.jpeg)
![piture_4](/images/event-4/41d9c737-718c-4eb5-992d-b979aaa30981.jpeg)
![piture_5](/images/event-4/63ce99ec-ac4f-4646-a3af-46a268cd3f64.jpeg)
![piture_6](/images/event-4/404da2be-4353-4261-9287-b6d91a7efe4c.jpeg)
![piture_7](/images/event-4/725ceae7-e342-4d73-88cd-fd5793f9ec5b.jpeg)
![piture_8](/images/event-4/17644578-8cd2-43f6-918f-9848b3d44951.jpeg)
![piture_9](/images/event-4/20407698-bdd4-42c7-8f33-85bed8ed02a2.jpeg)
![piture_10](/images/event-4/a1363d36-e3e5-48c2-b76b-07ec826900e3.jpeg)
![piture_11](/images/event-4/c2edcc1b-1c59-45c6-94c6-d078d337ecd1.jpeg)
![piture_12](/images/event-4/c72d08c9-5928-4f03-ae1a-aed17e9401ab.jpeg)
![piture_13](/images/event-4/de53e0de-10f7-479e-a2e7-54fc47928e9c.jpeg)
![piture_14](/images/event-4/e0c65198-929e-4a94-aaab-7e6e51364085.jpeg)
![piture_15](/images/event-4/e17e281a-6baf-4746-808e-26cc8504eadb.jpeg)
![piture_16](/images/event-4/ec3a8649-cc3e-43e3-a9ea-2673dd8acb27.jpeg)
![piture_17](/images/event-4/fedc1cf4-6796-41d5-98ee-9e51f19fc28c.jpeg)

> Sự kiện là cơ hội để tôi mở rộng kiến thức về Cảnh báo, Tự động hóa, Bảo mật và Ứng phó sự cố. Tôi đã tích lũy được nhiều kinh nghiệm thông qua việc lắng nghe các Kỹ sư Cloud cấp cao chia sẻ về công việc của họ.