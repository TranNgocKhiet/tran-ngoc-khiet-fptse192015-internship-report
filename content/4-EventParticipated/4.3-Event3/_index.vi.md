---
title: "Event 3"
weight: 3
chapter: false
pre: " <b> 4.3. </b> "
---

# Báo cáo Workshop: AWS Cloud Mastery Series #3 — Well-Architected Security Pillar

**Ngày:** Thứ Sáu, 29 tháng 11, 2025  
**Thời gian:** 8:30 AM – 12:00 PM  
**Địa điểm:** Tòa nhà Bitexco Financial, Thành phố Hồ Chí Minh  
**Người tổ chức:** Kha Van  
**Số lượng tham gia:** 355+ người

## Tổng quan

Workshop thứ ba và cuối cùng trong AWS Cloud Mastery Series tập trung vào bảo mật đám mây thông qua lăng kính Security Pillar của AWS Well-Architected Framework. Phiên bán ngày bao gồm năm trụ cột chính: IAM, Detection, Infrastructure Protection, Data Protection, và Incident Response.

## Phân tích phiên làm việc

### 8:30 – 8:50 AM | Mở cửa & Nền tảng bảo mật

Phiên bắt đầu với một cái nhìn tổng quan về vai trò của Security Pillar trong thiết kế well-architected:

- **Nguyên tắc cốt lõi:**
  - **Least Privilege:** Chỉ cấp quyền cần thiết
  - **Zero Trust:** Không bao giờ tin tưởng, luôn xác minh
  - **Defense in Depth:** Nhiều lớp kiểm soát bảo mật

- **Shared Responsibility Model:** AWS quản lý bảo mật cơ sở hạ tầng; khách hàng quản lý bảo mật ứng dụng và dữ liệu

- **Mối đe dọa hàng đầu ở Việt Nam:** Ransomware, xâm phạm thông tin xác thực, cơ sở dữ liệu bị phơi bày, API không an toàn

### 8:50 – 9:30 AM | Trụ cột 1: Identity & Access Management

#### Kiến trúc IAM hiện đại

- **Users, Roles, Policies:** Cơ bản của mô hình quyền AWS
- **Tránh thông tin xác thực dài hạn:** Vai trò dịch vụ và thông tin xác thực tạm thời
- **AWS IAM Identity Center:** Enterprise SSO và permission sets cho triển khai đa tài khoản

#### Kiểm soát truy cập ở quy mô

- **Service Control Policies (SCP):** Guardrails trên toàn tổ chức ngăn chặn các hành động nguy hiểm
- **Permission Boundaries:** Giới hạn quyền tối đa cho IAM users và roles
- **Tùy chọn MFA:** TOTP (Time-based One-Time Password) so với FIDO2 (khóa phần cứng)

#### Xác thực liên tục

- **Access Analyzer:** Xác định các chính sách quá cấp và quyền truy cập bên ngoài
- **Credential Rotation:** Tự động hóa xoay vòng khóa cho truy cập lập trình
- **Giới hạn thời gian phiên:** Yêu cầu xác thực lại cho các hoạt động nhạy cảm

#### Mini Demo: Xác thực chính sách IAM
- Tạo một chính sách và mô phỏng truy cập
- Xác định những khoảng trống quyền
- Sử dụng Access Analyzer để phát hiện quyền truy cập công khai

### 9:30 – 9:55 AM | Trụ cột 2: Detection & Continuous Monitoring

#### Cơ sở hạ tầng ghi nhật ký

- **CloudTrail (Organization-level):** Tất cả các lệnh gọi API trên các tài khoản AWS
- **GuardDuty:** Phát hiện mối đe dọa được quản lý sử dụng machine learning
- **Security Hub:** Trạng thái kết quả bảo mật tập trung và tuân thủ

#### Ghi nhật ký ở mọi tầng

- **VPC Flow Logs:** Phân tích lưu lượng mạng (kết nối được chấp nhận và bị từ chối)
- **ALB/Application Logs:** Khả năng hiển thị cấp yêu cầu
- **S3 Access Logs:** Theo dõi truy cập cấp đối tượng
- **Database Audit Logs:** Hoạt động truy vấn và người dùng

#### Cảnh báo & Tự động hóa

- **EventBridge:** Định tuyến các sự kiện bảo mật tới Lambda, SNS hoặc SQS để tự động hóa phản hồi
- **CloudWatch Alarms:** Kích hoạt cảnh báo trên các mẫu nhật ký cụ thể
- **Detection-as-Code:** Kiểm soát phiên bản các quy tắc phát hiện cùng với cơ sở hạ tầng

### 9:55 – 10:10 AM | Giờ cà phê

### 10:10 – 10:40 AM | Trụ cột 3: Infrastructure Protection

#### Bảo mật mạng

- **VPC Segmentation:** Subnets riêng cho cơ sở dữ liệu, công khai cho bộ cân bằng tải
- **Security Groups vs. NACLs:** Lọc stateful so với stateless
- **Mô hình ứng dụng:** Kiến trúc nhiều tầng với cách ly mạng

#### Bảo vệ nâng cao

- **AWS WAF (Web Application Firewall):** Bảo vệ các ứng dụng web khỏi các cuộc tấn công phổ biến
- **AWS Shield:** Bảo vệ DDoS (Tiêu chuẩn tự động, Nâng cao cho các ứng dụng có giá trị cao)
- **AWS Network Firewall:** Tường lửa tập trung cho VPCs

#### Bảo mật khối lượng công việc

- **EC2 Security:** Security groups, Systems Manager Session Manager (không có SSH keys)
- **ECS/EKS Security:** Pod security policies, network policies, container scanning
- **Secrets in Transit:** mTLS, encrypted API endpoints

### 10:40 – 11:10 AM | Trụ cột 4: Data Protection

#### Chiến lược mã hóa

- **Mã hóa tại chỗ:**
  - S3: SSE-KMS với khóa do khách hàng quản lý
  - RDS: Transparent Data Encryption (TDE)
  - EBS: Khối lượng được mã hóa với khóa KMS tùy chỉnh
  - DynamoDB: Mã hóa với AWS KMS

- **Mã hóa trong quá trình truyền:** HTTPS/TLS cho tất cả chuyển động dữ liệu

#### Quản lý chìa khóa

- **AWS KMS:** Chính sách chìa khóa, cấp phép, xoay vòng tự động
- **Tách rời nhiệm vụ:** Vai trò quản trị viên chìa khóa so với người dùng chìa khóa
- **Chiến lược xoay vòng chìa khóa:** Cân bằng bảo mật với phức tạp hoạt động

#### Quản lý bí mật

- **AWS Secrets Manager:** Thông tin xác thực cơ sở dữ liệu, khóa API, chứng chỉ
- **Parameter Store:** Các tham số cấu hình (được mã hóa bằng KMS)
- **Mẫu xoay vòng:** Xoay vòng tự động dựa trên Lambda
- **Kiểm soát truy cập:** Các chính sách IAM hạn chế các ứng dụng nào có thể truy cập bí mật

#### Phân loại dữ liệu

- **Xác định dữ liệu PII/Sensitive:** Macie để khám phá tự động
- **Guardrails truy cập:** Hạn chế quyền truy cập vào các kho dữ liệu nhạy cảm
- **Audit Trails:** Theo dõi ai đã truy cập cái gì và khi nào

### 11:10 – 11:40 AM | Trụ cột 5: Incident Response

#### Vòng đời IR (theo AWS)

1. **Preparation:** Công cụ, runbooks, đào tạo đội ngũ
2. **Detection & Analysis:** Xác định và phân loại sự cố
3. **Containment:** Dừng cuộc tấn công và giới hạn thiệt hại
4. **Eradication:** Loại bỏ hiện diện của kẻ tấn công
5. **Recovery:** Khôi phục hệ thống về hoạt động bình thường
6. **Post-Incident Review:** Học từ sự cố

#### Playbooks sự cố

**Kịch bản 1: Khóa IAM bị xâm phạm**
- Phát hiện: GuardDuty cảnh báo về các lệnh gọi API bất thường
- Containment: Vô hiệu hóa thông tin xác thực bị xâm phạm ngay lập tức
- Eradication: Xoay vòng access keys, xem lại CloudTrail cho các hành động không được phép
- Recovery: Xác minh không có backdoors còn lại

**Kịch bản 2: Bộ chứa S3 bị phơi bày công khai**
- Phát hiện: CloudTrail hiển thị chính sách bộ chứa được sửa đổi hoặc ACL đối tượng được thay đổi
- Containment: Hạn chế quyền truy cập công khai ngay lập tức
- Eradication: Xem lại ai đã sửa đổi chính sách (audit trail)
- Recovery: Xác minh không có dữ liệu nhạy cảm bị truy cập

**Kịch bản 3: Phát hiện phần mềm độc hại EC2**
- Phát hiện: GuardDuty xác định hành vi EC2 đáng ngờ
- Containment: Cô lập instance trong security group, snapshot cho pháp y
- Eradication: Cập nhật OS/patch, xoay vòng thông tin xác thực
- Recovery: Triển khai lại instance sạch từ golden image

#### Tự động hóa & Công cụ

- **Snapshot & Isolation:** Tạo snapshot tự động và cách ly mạng
- **Evidence Collection:** Bảo tồn nhật ký và dữ liệu cho post-mortem
- **Auto-Response:** Các hàm Lambda kích hoạt khắc phục (vô hiệu hóa người dùng, cô lập instance)
- **Notification:** Cảnh báo SNS cho đội bảo mật và incident commander

### 11:40 – 12:00 PM | Tóm tắt & Q&A

#### Những bài học chính

- Năm trụ cột được kết nối với nhau: IAM mạnh mẽ là vô ích nếu không có phát hiện
- Các doanh nghiệp Việt Nam phải đối mặt với các mối đe dọa thực tế; sự chuẩn bị là cần thiết
- AWS cung cấp các công cụ end-to-end; rào cản là quy trình và văn hóa

#### Lộ trình học tập

- **AWS Security Fundamentals:** Cấp độ giới thiệu
- **AWS Certified Security – Specialty:** Kiến thức kỹ thuật sâu
- **AWS Solutions Architect Professional:** Ra quyết định kiến trúc
- **Thực hành bàn tay:** CloudLabs, xây dựng các kịch bản kiểm tra

#### Những cạm bẫy phổ biến ở Việt Nam

- Phụ thuộc quá mức vào bảo mật chu vi (giả định niềm tin nội bộ)
- Lưu trữ bí mật trong mã hoặc tệp cấu hình
- Bỏ qua các yêu cầu giữ lại nhật ký và tuân thủ

## Suy tư cá nhân

### Những gì tôi đã học

Bảo mật không phải là một kiểm soát duy nhất—đó là một hệ thống các phòng thủ chồng chéo. AWS cung cấp các công cụ toàn diện, nhưng thành công đòi hỏi kỷ luật quy trình và cam kết văn hóa đối với least privilege.

Sự nhấn mạnh vào ứng phó với sự cố đã gây ấn tượng mạnh. Quá nhiều tổ chức chuẩn bị cho các khai thác zero-day nhưng không thể ứng phó với thông tin xác thực bị xâm phạm (vectơ tấn công phổ biến nhất). Playbooks được ghi lại tốt và phản hồi tự động là các bộ nhân lực.

### Những hiểu biết chính

1. **Phát hiện > Ngăn chặn:** Giả định tinh thần vi phạm—tập trung vào phát hiện xâm phạm nhanh chóng.
2. **Tự động hóa rất quan trọng:** Ứng phó với sự cố thủ công quá chậm; Lambda/Step Functions phải xử lý các phản hồi thường xuyên.
3. **Ghi nhật ký là bắt buộc:** Không có nhật ký toàn diện, bạn không thể điều tra hoặc kiểm tra hiệu quả.
4. **IAM là nền tảng:** Mọi kiểm soát khác phụ thuộc vào quản lý danh tính và truy cập vững chắc.
5. **Văn hóa quan trọng:** Các kiểm soát kỹ thuật thất bại nếu không có các đội nhận thức bảo mật và quy trình.

### Các bước tiếp theo

- Kiểm toán các quyền IAM hiện tại và xác định các trường hợp quá đặc quyền
- Bật GuardDuty và Security Hub để phát hiện mối đe dọa liên tục
- Xây dựng playbooks ứng phó với sự cố cụ thể cho cơ sở hạ tầng của chúng tôi
- Thiết lập khắc phục tự động cho các phát hiện bảo mật phổ biến
- Triển khai mã hóa tại chỗ cho tất cả các cơ sở dữ liệu và bộ chứa S3

> Workshop bảo mật nửa ngày này cung cấp một cái nhìn tổng quan chiến lược về AWS Well-Architected Security Pillar và các khuôn khổ ứng phó với sự cố thực tế. Sự nhấn mạnh vào tự động hóa, phát hiện và playbooks sự cố sẽ trực tiếp cải thiện tư thế bảo mật của tổ chức chúng tôi.