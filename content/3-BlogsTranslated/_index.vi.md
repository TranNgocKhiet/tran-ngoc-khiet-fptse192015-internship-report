---
title: "Các bài blogs đã dịch"
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

###  [Blog 1 - Khởi đầu sự nghiệp đám mây của bạn với AWS SimuLearn](3.1-Blog1/)
Bài viết “Jumpstart your cloud career with AWS SimuLearn” giới thiệu AWS SimuLearn – nền tảng học tập tương tác kết hợp AI tạo sinh (Generative AI) với mô phỏng tình huống khách hàng thực tế. Người học có thể rèn luyện kỹ năng kỹ thuật và giao tiếp trong môi trường an toàn, nhận phản hồi tức thì và luyện tập theo vai trò hoặc ngành nghề. Ba câu chuyện từ Hetvi, Karishma và Kattie minh họa cách SimuLearn giúp họ phát triển từ kỹ năng giao tiếp khách hàng, chuyên môn kỹ thuật, đến kiến thức chuyên sâu theo ngành y tế (HCLS). AWS SimuLearn mang đến hơn 200 khóa học và mô phỏng theo vai trò, giúp người mới trong lĩnh vực đám mây xây dựng tự tin, hiểu sâu về AWS và sẵn sàng cho sự nghiệp điện toán đám mây.

###  [Blog 2 - Thiết lập cảnh báo tự động cho các AWS Savings Plans mới mua](3.2-Blog2/)
Bài viết “How to Set Up Automated Alerts for Newly Purchased AWS Savings Plans” hướng dẫn cách triển khai hệ thống tự động giám sát và gửi cảnh báo cho các Savings Plans mới mua có mức sử dụng thấp. Giải pháp sử dụng AWS CloudFormation để tạo các dịch vụ như Step Functions, SNS, EventBridge, và các IAM Role cần thiết. Quy trình gồm hai phần triển khai:
- Tài khoản Member: tạo Step Function để kiểm tra Savings Plans mua trong 7 ngày gần nhất và tháng hiện tại, sau đó gửi thông báo qua email nếu mức sử dụng thấp.
- Tài khoản Management: thiết lập quyền truy cập để Step Function có thể đọc dữ liệu Savings Plans của toàn tổ chức.
Người dùng có thể xác định ngưỡng sử dụng, tần suất kiểm tra và danh sách email nhận cảnh báo. Khi nhận cảnh báo, cần đánh giá lý do sử dụng thấp và cân nhắc hoàn trả Savings Plan (nếu đủ điều kiện). Giải pháp giúp FinOps teams tối ưu hóa chi phí đám mây, phát hiện sớm Savings Plans chưa khai thác hiệu quả và tránh lãng phí trong cam kết tài chính AWS.

###  [Blog 3 - Vận hành hiệu quả khối lượng công việc Windows Server BYOL trên AWS](3.3-Blog3/)
Bài viết của AWS hướng dẫn cách vận hành hiệu quả các khối lượng công việc Windows Server theo mô hình Bring Your Own License (BYOL) trên AWS để giảm chi phí. Nội dung bao gồm cách xác định giấy phép đủ điều kiện BYOL, chuẩn bị hình ảnh máy chủ Windows bằng VM Import/Export và Migration Hub Orchestrator, cũng như chuyển đổi loại giấy phép qua AWS License Manager. Bài viết còn hướng dẫn cách phát hiện lỗi cấu hình bằng AWS Config và phân tích chi phí với AWS Cost and Usage Reports (CUR). Việc áp dụng các thực tiễn này giúp tổ chức tối ưu chi phí, tuân thủ bản quyền và nâng cao hiệu quả vận hành trên AWS.
