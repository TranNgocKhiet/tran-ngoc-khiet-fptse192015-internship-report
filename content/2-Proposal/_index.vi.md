---
title: "Bản đề xuất"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# Hệ thống Quản lý Văn phòng Thông minh cho Phòng Nghiên cứu
## Giải pháp AWS Serverless hợp nhất cho giám sát và điều khiển văn phòng thông minh theo thời gian thực 

### 1. Tóm tắt điều hành  
Hệ thống Quản lý Văn phòng Thông minh (Smart Office Management System) được đề xuất bởi Nhóm **Skyscraper** từ **FPTU HCM Campus**, lấy cảm hứng từ sự vận hành xuất sắc quan sát được trong chuyến đi thực tế đến văn phòng AWS tại TP. Hồ Chí Minh. Việc quản lý văn phòng truyền thống hiện nay thiếu khả năng hiển thị thời gian thực về điều kiện phòng (nhiệt độ, độ ẩm, ánh sáng) và phụ thuộc nhiều vào sự giám sát thủ công. Để giải quyết vấn đề này, chúng tôi đề xuất xây dựng một **Bảng điều khiển Quản lý (Management Console)** tập trung, được xây dựng trên **kiến trúc AWS Serverless** hoàn chỉnh. Bằng cách tận dụng các dịch vụ như AWS IoT Core, Lambda và DynamoDB, hệ thống thu thập dữ liệu cảm biến mỗi 2-5 phút để hỗ trợ giám sát thời gian thực và cho phép quản trị viên quản lý cấu hình thiết bị từ xa. Dự án này cũng đóng vai trò là chiến lược "First Cloud AI Journey", giúp nhóm thu hẹp khoảng cách giữa kiến thức lý thuyết và ứng dụng thực tế của Điện toán Đám mây.

### 2. Tuyên bố vấn đề  
#### Vấn đề hiện tại
Hiện nay, việc quản lý môi trường văn phòng trong các phòng lab nghiên cứu đòi hỏi sự can thiệp thủ công để kiểm tra trạng thái thiết bị (đèn, điều hòa) và điều kiện môi trường. Các quản lý thường thiếu dữ liệu cần thiết để đưa ra quyết định sáng suốt về việc sử dụng năng lượng hoặc sự thoải mái của phòng. Việc vận hành thiết bị theo lịch trình cố định (ví dụ: 8 giờ sáng đến 5 giờ chiều) mà không quan tâm đến mức độ sử dụng thực tế hoặc các yếu tố môi trường dẫn đến lãng phí năng lượng. Hơn nữa, nếu không có bảng điều khiển tập trung, quản trị viên không thể nhanh chóng phát hiện các bất thường hoặc cấu hình cài đặt cho nhiều phòng một cách hiệu quả.

#### Giải pháp
Nền tảng sử dụng **AWS IoT Core** để tiếp nhận dữ liệu MQTT từ cảm biến phòng, **AWS Lambda** và **API Gateway** cho logic xử lý backend, **Amazon DynamoDB** để lưu trữ nhật ký cảm biến và cấu hình phòng, cùng với **Amazon S3** kết hợp **CloudFront** để lưu trữ bảng điều khiển quản lý web. Quyền truy cập được bảo mật nghiêm ngặt thông qua **Amazon Cognito**. **Amazon EventBridge** được sử dụng để xử lý các tác vụ tự động hóa theo lịch trình, trong khi **Amazon SNS** đảm bảo thông báo kịp thời cho các cảnh báo hệ thống. Giải pháp này thay thế việc theo dõi thủ công bằng một bảng điều khiển quản lý kỹ thuật số, thời gian thực, có khả năng giám sát nhiều phòng cùng lúc.

#### Lợi ích và hoàn vốn đầu tư (ROI)
Hệ thống Quản lý Văn phòng Thông minh nâng cao hiệu quả vận hành bằng cách cung cấp một giao diện giám sát và cấu hình duy nhất. Nó trao quyền cho quản lý phòng lab điều khiển thiết bị từ xa và đưa ra quyết định dựa trên dữ liệu. Ngoài những cải tiến về vận hành, dự án cung cấp một nền tảng serverless có thể tái sử dụng cho các nghiên cứu IoT trong tương lai tại trường đại học.

Chi phí vận hành hàng tháng ước tính khoảng **$1.81 USD**, tận dụng AWS Free Tier cho các dịch vụ như Lambda, API Gateway và DynamoDB. Chi phí chính bao gồm CloudFront ($1.27) và CloudWatch ($0.25), tổng cộng khoảng **$21.72 USD mỗi năm**. Vì hệ thống tận dụng phần cứng ESP32 và cảm biến hiện có, không có thêm chi phí vốn đầu tư. Hệ thống mang lại giá trị ngay lập tức thông qua việc tiết kiệm thời gian và giảm nỗ lực quản lý.

### 3. Kiến trúc giải pháp  
Hệ thống Smart Office áp dụng kiến trúc AWS hoàn toàn serverless được tối ưu hóa cho hiệu quả chi phí và khả năng mở rộng. Dữ liệu từ nhiều hub cảm biến được truyền đến AWS IoT Core, được xử lý bởi các hàm Lambda và lưu trữ trong DynamoDB để giám sát thời gian thực và quản lý cấu hình. EventBridge tự động hóa các hành động thiết bị theo lịch trình, trong khi SNS xử lý thông báo hệ thống. Bảng điều khiển web được lưu trữ trên S3 và phân phối an toàn qua CloudFront, với xác thực người dùng được quản lý thông qua Amazon Cognito. Kiến trúc này giảm thiểu chi phí vận hành và đảm bảo độ tin cậy cao cho việc kiểm soát môi trường thông minh.

![Sơ đồ kiến trúc](/images/2-Proposal/Smart-Office-Architect-Diagram.drawio.png)

#### Dịch vụ AWS sử dụng
- **AWS IoT Core**: Tiếp nhận và quản lý dữ liệu MQTT từ các hub phòng thông minh, cho phép giao tiếp an toàn giữa thiết bị biên và đám mây.
- **AWS Lambda**: Thực thi logic backend để xử lý dữ liệu cảm biến, xử lý các yêu cầu API và thực hiện các lệnh quản lý (Tính toán Serverless).
- **Amazon API Gateway**: Cung cấp các điểm cuối RESTful an toàn cho bảng điều khiển web tương tác với các dịch vụ backend.
- **Amazon DynamoDB**: Cung cấp lưu trữ NoSQL nhanh chóng cho cấu hình phòng, trạng thái thiết bị và nhật ký cảm biến lịch sử.
- **Amazon EventBridge**: Điều phối các quy trình làm việc theo sự kiện, chẳng hạn như cập nhật cấu hình theo lịch trình hoặc kiểm tra nhịp tim (heartbeat).
- **Amazon SNS**: Gửi thông báo email cho quản trị viên liên quan đến cảnh báo hệ thống hoặc cập nhật quan trọng.
- **Amazon S3**: Lưu trữ các tài sản tĩnh frontend (HTML, CSS, JS) cho Bảng điều khiển Quản lý.
- **Amazon CloudFront**: Phân phối ứng dụng web toàn cầu với độ trễ thấp và bảo mật SSL.
- **Amazon Cognito**: Quản lý danh tính người dùng, xác thực và kiểm soát truy cập cho Bảng điều khiển Quản lý.
- **Amazon CloudWatch**: Thu thập nhật ký và số liệu để giám sát sức khỏe hệ thống và gỡ lỗi thực thi Lambda.

#### Thiết kế thành phần
- **Sensor Hubs**: Each IoT-enabled room device collects environmental data (temperature, humidity, light, etc.) and sends it to **AWS IoT Core** every two minutes.  
- **Sensor Hubs**: Các thiết bị hỗ trợ IoT (ESP32) trong mỗi phòng thu thập dữ liệu từ xa (nhiệt độ, độ ẩm, ánh sáng) và truyền đến **AWS IoT Core** vài phút một lần.
- **Data Ingestion (Tiếp nhận dữ liệu)**: Các quy tắc **AWS IoT Core** kích hoạt **HandleTelemetry Lambda**, chức năng này xác thực dữ liệu và lưu vào **Amazon DynamoDB**.
- **Configuration Management (Quản lý cấu hình)**: Quản trị viên sử dụng bảng điều khiển để cập nhật cài đặt phòng. **RoomConfigHandler Lambda** cập nhật DynamoDB và đẩy các thay đổi xuống thiết bị qua IoT Core Shadows hoặc MQTT.
- **User Interaction (Tương tác người dùng)**: **Bảng điều khiển Web Next.js** (trên **S3/CloudFront**) trực quan hóa dữ liệu thời gian thực và cung cấp giao diện điều khiển.
- **User Authentication (Xác thực người dùng)**: **Amazon Cognito** đảm bảo chỉ các thành viên phòng lab được ủy quyền mới có thể đăng nhập và truy cập dữ liệu phòng nhạy cảm.
- **Monitoring & Reliability (Giám sát & Độ tin cậy)**: **Amazon CloudWatch** theo dõi hiệu suất hệ thống, đảm bảo tính sẵn sàng cao và khắc phục sự cố nhanh chóng.

### 4. Triển khai kỹ thuật  
#### Giai đoạn triển khai
- **Nghiên cứu & Nền tảng (Tuần 1-7)**: Nghiên cứu các dịch vụ AWS cốt lõi (IoT Core, Lambda, DynamoDB, S3, API Gateway, Cognito) và hiểu các mô hình thiết kế Serverless.
- **Thiết kế Kiến trúc & Dự toán (Tuần 8)**: Hoàn thiện sơ đồ giải pháp cho thiết lập 8 phòng và sử dụng AWS Pricing Calculator để dự báo ngân sách.
- **Phát triển (Tuần 9-11)**:
    - Triển khai firmware/kịch bản mô phỏng dữ liệu IoT.
    - Phát triển Backend: Các hàm Lambda, bảng DynamoDB và tài nguyên API Gateway sử dụng CloudFormation/CDK.
    - Phát triển Frontend: Xây dựng Bảng điều khiển Quản lý và tích hợp với các API.
- **Kiểm thử & Triển khai (Tuần 12)**: Thực hiện kiểm thử toàn diện (end-to-end), xác thực luồng dữ liệu từ cảm biến đến bảng điều khiển và triển khai hệ thống lên môi trường production.

#### Yêu cầu kỹ thuật
- **Tầng Phần cứng**: Các Sensor Hub dựa trên ESP32 giám sát các chỉ số môi trường.
- **Tầng Đám mây**: Một stack hoàn toàn serverless trên AWS (IoT Core, Lambda, DynamoDB, API Gateway, S3, CloudFront, Cognito, EventBridge, SNS).
- **DevOps**: Cơ sở hạ tầng dưới dạng Mã (IaC) sử dụng AWS CloudFormation để triển khai có thể tái lập.
- **Giao diện**: Bảng điều khiển web tương thích (responsive) cho phép giám sát thời gian thực và cập nhật cấu hình.

### 5. Lộ trình & Mốc triển khai  
#### Lộ trình
- **Tuần 1–7**: Tìm hiểu sâu về các dịch vụ AWS và hoàn thành khóa đào tạo cơ bản "First Cloud AI Journey".
- **Tuần 8**: Thiết kế kiến trúc hệ thống và hoàn thiện dự toán chi phí.
- **Tuần 9–11**: Giai đoạn phát triển cốt lõi (Logic Backend, Lược đồ Database, Tích hợp giao diện Frontend).
- **Tuần 12**: Kiểm thử tích hợp hệ thống, gỡ lỗi và trình bày Go-Live cuối cùng.

### 6. Ước tính ngân sách  
Có thể xem chi phí trên [AWS Pricing Calculator](https://calculator.aws/#/estimate?id=0db12150c448b012356e475becefd549c37094d8)  
Hoặc tải [tệp ước tính ngân sách](/file/proposal/smart_office_pricing_caculator.pdf).  

#### Chi phí hạ tầng
**Dịch vụ AWS:**
- **Amazon DynamoDB**: Miễn phí (Gói Always Free: 25GB Lưu trữ).
- **AWS Lambda**: Miễn phí (Gói Always Free: 1 triệu yêu cầu/tháng).
- **AWS IoT Core**: $0.18/tháng (8 thiết bị, gửi dữ liệu mỗi 2 phút).
- **Amazon API Gateway**: Miễn phí (Gói Free Tier: 1 triệu cuộc gọi/tháng trong 12 tháng).
- **Amazon S3**: Miễn phí (Lưu trữ Standard < 5GB).
- **Amazon CloudFront**: $1.27/tháng (Dựa trên ước tính truyền dữ liệu và yêu cầu).
- **Amazon EventBridge**: Miễn phí (Sự kiện trong gói Free Tier).
- **Amazon SNS**: $0.02/tháng (Thông báo qua Email).
- **Amazon CloudWatch**: $0.25/tháng (Thu thập và lưu trữ log).
- **Amazon Cognito**: Miễn phí (Gói Free Tier: 50,000 MAUs).

**Phần cứng:** Giả lập script
**Tổng cộng:** ≈ **$1.81/tháng**, hoặc **$21.72/năm** (được tối ưu hóa trong giới hạn AWS Free Tier).

### 7. Đánh giá rủi ro  
#### Ma trận rủi ro
- **Vấn đề Kết nối IoT**: Tác động trung bình, xác suất trung bình.
- **Dữ liệu Cảm biến Không chính xác**: Tác động trung bình, xác suất thấp.
- **Phí AWS Ngoài dự kiến**: Tác động thấp, xác suất thấp (do cảnh báo ngân sách chặt chẽ).
- **Cấu hình Bảo mật Sai**: Tác động cao, xác suất thấp.

#### Chiến lược giảm thiểu
- **Kết nối**: Triển khai logic thử lại (retry) trên thiết bị biên và lưu đệm cục bộ.
- **Chi phí**: Cấu hình AWS Budgets để cảnh báo khi chi tiêu vượt quá $1.00.
- **Bảo mật**: Thực thi các chính sách IAM nghiêm ngặt (Đặc quyền Tối thiểu) và yêu cầu xác thực cho tất cả truy cập API qua Cognito.
- **Độ tin cậy**: Sử dụng CloudWatch Logs để truy vết lỗi trong thực thi Lambda ngay lập tức.

#### Kế hoạch dự phòng
- Kích hoạt các điều khiển ghi đè thủ công nếu hệ thống đám mây không khả dụng.
- Duy trì bản sao lưu của các mẫu CloudFormation để triển khai lại nhanh chóng.

### 8. Kết quả kỳ vọng  
#### Cải tiến kỹ thuật:
- Thay thế việc kiểm tra thủ công bằng **giám sát kỹ thuật số thời gian thực**.
- Cung cấp một **nền tảng tập trung** để quản lý cấu hình trên nhiều phòng.
- Thiết lập một **kiến trúc có khả năng mở rộng** để hỗ trợ nhiều thiết bị hơn trong tương lai.

#### Giá trị dài hạn:
- Phục vụ như một **trung tâm học tập** thực tế cho sinh viên để làm chủ các công nghệ AWS Serverless.
- Cung cấp thông tin chi tiết về dữ liệu có thể dẫn đến các chính sách sử dụng năng lượng tốt hơn trong phòng lab.
- Chứng minh một giải pháp đám mây hiệu quả về chi phí, sẵn sàng cho sản xuất.

## Proposal Link

[Smart_Office_Proposal](/file/proposal/Smart_Office_Proposal.docx)