---
title: "Sự kiện 2"
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---

# Báo cáo Workshop: AWS Cloud Mastery Series #2 — DevOps trên AWS

**Ngày:** Thứ Hai, 17 tháng 11, 2025  
**Thời gian:** 8:30 AM – 5:00 PM  
**Địa điểm:** Tòa nhà Bitexco Financial, Thành phố Hồ Chí Minh  
**Người tổ chức:** Kha Van  
**Số lượng tham gia:** 316 người

## Tổng quan

Workshop thứ hai trong AWS Cloud Mastery Series cung cấp một bài đáy sâu toàn diện, kéo dài cả ngày, về các thực tiễn DevOps trên AWS. Phiên bao gồm tự động hóa CI/CD, infrastructure-as-code, containerization và monitoring, với các bài demo trực tiếp và các nghiên cứu trường hợp thực tế.

## Phiên sáng: Văn hóa & CI/CD Pipeline (8:30 AM – 12:00 PM)

### 8:30 – 9:00 AM | Chào mừng & Tư duy DevOps

Phiên bắt đầu với một bài tóm tắt về workshop AI/ML trước đó và giới thiệu văn hóa và nguyên tắc DevOps. Các chỉ số chính được thảo luận:
- **DORA Metrics:** Deployment frequency, lead time, mean time to recovery (MTTR), change failure rate
- **Lợi ích DevOps:** Giao hàng nhanh hơn, giảm rủi ro, cải thiện hợp tác nhóm

### 9:00 – 10:30 AM | Dịch vụ DevOps AWS – CI/CD Pipeline

Một hướng dẫn toàn diện về hệ sinh thái AWS CodePipeline:

#### Kiểm soát mã nguồn
- **AWS CodeCommit:** Các kho Git gốc với tích hợp IAM
- **Git Strategies:** GitFlow so với Trunk-based development (những lợi ích và khi nào nên sử dụng mỗi cái)

#### Xây dựng & Kiểm thử
- **CodeBuild Configuration:** Môi trường xây dựng dựa trên Docker, bộ nhớ cache, quản lý tạo tác
- **Testing Pipelines:** Unit tests, integration tests, và security scanning

#### Triển khai
- **Chiến lược CodeDeploy:**
  - **Blue/Green:** Triển khai không có thời gian chết với khôi phục tức thì
  - **Canary:** Triển khai dần dần cho một phần trăm lưu lượng
  - **Rolling:** Cập nhật instance tuần tự
- **Target Instances:** EC2, On-premises, Lambda

#### Điều phối
- **CodePipeline Automation:** Kết nối source → build → deploy stages
- **Approval Gates:** Các bước xem xét thủ công cho triển khai production

#### Demo trực tiếp
Một hướng dẫn toàn bộ CI/CD pipeline, thể hiện:
1. Commit mã kích hoạt CodeBuild
2. Các bài kiểm tra tự động chạy và báo cáo
3. Lưu trữ tạo tác trong S3
4. CodeDeploy thực hiện triển khai blue/green
5. Khôi phục tự động khi các kiểm tra sức khỏe thất bại

### 10:30 – 10:45 AM | Giờ nghỉ

### 10:45 AM – 12:00 PM | Infrastructure as Code (IaC)

Hai cách tiếp cận IaC chủ yếu trên AWS được so sánh:

#### AWS CloudFormation
- **Templates & Stacks:** Mẫu JSON/YAML xác định toàn bộ môi trường
- **Drift Detection:** Giám sát các thay đổi cơ sở hạ tầng bên ngoài CloudFormation
- **Stack Policies:** Ngăn chặn các cập nhật vô tình đối với các tài nguyên quan trọng

#### AWS CDK (Cloud Development Kit)
- **Constructs:** Các khối xây dựng cơ sở hạ tầng có thể tái sử dụng, có thể kết hợp
- **Language Support:** TypeScript, Python, Java, .NET
- **Higher Abstraction:** Viết cơ sở hạ tầng giống như mã ứng dụng

#### So sánh & Lựa chọn
- CloudFormation: Kiểm soát cấp thấp hơn, cú pháp JSON/YAML, hệ sinh thái trưởng thành
- CDK: Năng suất cao hơn, các ngôn ngữ lập trình quen thuộc, trừu tượng hóa

#### Demo trực tiếp
Triển khai cơ sở hạ tầng bằng cả CloudFormation và CDK, nhấn mạnh:
1. Cấu trúc mẫu CloudFormation và tham số
2. Phân cấp construct CDK và tái sử dụng
3. Thời gian triển khai và hành vi khôi phục

## Phiên chiều: Containers & Observability (1:00 PM – 5:00 PM)

### 1:00 – 2:30 PM | Dịch vụ Container trên AWS

#### Docker Fundamentals
- **Microservices & Containerization:** Phá vỡ monoliths, mở rộng quy mô độc lập
- **Image Layering:** Tối ưu hóa kích thước hình ảnh và bộ nhớ cache xây dựng

#### Amazon ECR (Elastic Container Registry)
- **Lưu trữ hình ảnh & Quét:** Phát hiện lỗ hổng cho hình ảnh container
- **Lifecycle Policies:** Làm sạch tự động các hình ảnh cũ hoặc không sử dụng
- **IAM Integration:** Quyền truy cập chi tiết vào các đăng ký

#### Amazon ECS so với EKS
- **ECS:** Điều phối đơn giản hơn, gốc AWS, đường cong học tập thấp hơn
- **EKS:** Tương thích Kubernetes, các tùy chọn đa đám mây, hệ sinh thái phong phú hơn
- **Deployment Strategies:** Đặt vị trí tác vụ, tự động mở rộng, phát hiện dịch vụ

#### AWS App Runner
- **Triển khai Container Simplified:** Không cần quản lý cluster
- **Lý tưởng cho:** Các ứng dụng web không trạng thái, API, microservices
- **Tự động mở rộng:** Dựa trên lưu lượng hoặc các chỉ số tùy chỉnh

#### Demo & Nghiên cứu trường hợp
Một triển khai microservices so sánh:
1. Triển khai ECS với các định nghĩa tác vụ và dịch vụ
2. Triển khai EKS với pod manifests và toán tử
3. Triển khai App Runner cho một REST API đơn giản
4. Hành vi tự động mở rộng dưới tải

### 2:30 – 2:45 PM | Giờ nghỉ

### 2:45 – 4:00 PM | Monitoring & Observability

#### CloudWatch
- **Metrics & Logs:** Tập hợp tập trung từ các dịch vụ AWS
- **Alarms & Dashboards:** Trực quan hóa thời gian thực và cảnh báo
- **Log Insights:** Truy vấn nhật ký bằng cú pháp giống SQL

#### AWS X-Ray
- **Distributed Tracing:** Theo dõi các yêu cầu trên microservices
- **Service Map:** Biểu diễn trực quan của kiến trúc ứng dụng
- **Performance Insights:** Xác định nút cổ chai và những điểm gây trễ

#### Thiết lập Observability toàn ngăn xếp
- Tích hợp CloudWatch, X-Ray và nhật ký ứng dụng
- Correlation IDs để theo dõi các yêu cầu từ đầu đến cuối
- Đặt các ngưỡng cảnh báo thích hợp (tránh alert fatigue)

#### Thực tiễn tốt nhất
- **Alerting:** Cảnh báo về các triệu chứng (độ trễ, tỷ lệ lỗi) không chỉ là các số liệu thô
- **Dashboards:** Dashboards dành riêng cho các kỹ sư oncall
- **On-Call Processes:** Các chính sách escalation, runbooks, postmortems sự cố

#### Demo
Xây dựng một giải pháp observability hoàn chỉnh:
1. CloudWatch agent thu thập các chỉ số từ các instance EC2
2. Nhật ký ứng dụng chảy sang CloudWatch Logs
3. X-Ray tracing một ứng dụng đa tầng
4. Tạo dashboards và cảnh báo cho các chỉ số chính

### 4:00 – 4:45 PM | DevOps Best Practices & Nghiên cứu trường hợp

#### Chiến lược triển khai
- **Feature Flags:** Tách biệt triển khai khỏi bản phát hành
- **A/B Testing:** Thử nghiệm với tập hợp con lưu lượng
- **Dark Launches:** Chạy cơ sở hạ tầng mới song song

#### Kiểm thử tự động & Tích hợp CI/CD
- **Test Pyramid:** Unit, integration, và end-to-end tests
- **Test as Code:** Giữ các bài kiểm tra trong kiểm soát phiên bản
- **Performance Testing:** Bắt các hồi quy trước production

#### Quản lý sự cố
- **Postmortems:** Các bài đánh giá vô tội tập trung vào các cải tiến hệ thống
- **Runbooks:** Các thủ tục được ghi lại cho các sự cố phổ biến
- **On-Call Rotation:** Phân phối công bằng và các chính sách escalation

#### Các nghiên cứu trường hợp thực tế
- **Startup:** Từ monolith đến microservices, mở rộng quy mô từ 10 đến 1M người dùng
- **Enterprise:** Hiện đại hóa hệ thống kế thừa đồng thời duy trì 99,99% uptime

### 4:45 – 5:00 PM | Q&A & Tóm tắt

**Lộ trình sự nghiệp DevOps:** Lộ trình chứng chỉ AWS (Developer Associate, Solutions Architect Pro, DevOps Professional)

## Suy tư cá nhân

### Những gì tôi đã học

Phạm vi của hệ sinh thái DevOps AWS trở nên rõ ràng—có một dịch vụ được xây dựng đặc biệt cho mỗi giai đoạn của quy trình triển khai. Thay vì dán các công cụ không liên quan, các nhóm DevOps trên AWS được hưởng lợi từ tích hợp sâu.

Sự tương phản giữa ECS và EKS làm nổi bật một quyết định quan trọng: quản lý đơn giản so với tính di động. Đối với hầu hết các trường hợp sử dụng, ECS là đủ; phức tạp của Kubernetes chỉ có lợi nhuận khi cần multi-cloud hoặc orchestration phức tạp.

### Những hiểu biết chính

1. **Tự động hóa là bắt buộc:** Triển khai thủ công rất dễ bị lỗi và chậm; CI/CD là điều kiện tiên quyết.
2. **Observability vượt trội hơn monitoring:** Ghi lại những gì xảy ra (logs/traces) có giá trị hơn chỉ là các chỉ số.
3. **Infrastructure as Code là bắt buộc:** Cơ sở hạ tầng được kiểm soát phiên bản và có thể xem xét giảm rủi ro hoạt động.
4. **DevOps là một văn hóa, không phải một tiêu đề công việc:** Thành công đòi hỏi hợp tác giữa các nhà phát triển, ops và bảo mật.
5. **Chọn công cụ phù hợp:** ECS cho đơn giản, EKS cho tính di động, App Runner cho dễ sử dụng.

### Các bước tiếp theo

- Thiết lập một CI/CD pipeline cơ bản sử dụng CodePipeline cho các dự án của đội ngũ tôi
- Di chuyển một ứng dụng sang container và triển khai thông qua ECS
- Triển khai CloudWatch dashboards và X-Ray tracing cho các dịch vụ hiện có
- Thiết kế các template cơ sở hạ tầng sử dụng CDK cho các triển khai có thể tái sản xuất

## Một số hình ảnh từ sự kiện

![event-picture-1](/images/event-2/IMG_20251117_121134%20(2).jpg)

> Workshop toàn ngày này cung cấp cho tôi kiến thức DevOps thực tế và chứng minh rằng AWS cung cấp các giải pháp end-to-end cho toàn bộ vòng đời triển khai. Sự nhấn mạnh vào tự động hóa, observability và văn hóa có ý nghĩa đối với tất cả các kích thước nhóm.