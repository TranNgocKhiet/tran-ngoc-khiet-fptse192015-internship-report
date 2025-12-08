---
title: "Sự Kiện 1"
weight: 1
chapter: false
pre: " <b> 4.1. </b> "
---

# Báo cáo Workshop: AWS Cloud Mastery Series #1 — AI/ML/GenAI trên AWS

**Ngày:** Thứ Bảy, 15 tháng 11, 2025  
**Thời gian:** 8:30 AM – 12:00 PM  
**Địa điểm:** Tòa nhà Bitexco Financial, Thành phố Hồ Chí Minh  
**Người tổ chức:** Kha Van  
**Số lượng tham gia:** 348 người

## Tổng quan

Phiên đầu tiên của AWS Cloud Mastery Series giới thiệu các cách tiếp cận hiện đại về machine learning và generative AI trên AWS, tập trung vào ứng dụng thực tế và các bài tập thực hành. Workshop bao gồm cả SageMaker cho các quy trình ML truyền thống và Amazon Bedrock để xây dựng với foundation models.

## Phân tích phiên làm việc

### 8:30 – 9:00 AM | Chào mừng & Giới thiệu

Phiên bắt đầu với đăng ký tham gia và tạo mạng lưới, tiếp theo là tổng quan về bối cảnh AI/ML ở Việt Nam. Các tổ chức viên đặt ra kỳ vọng cho mục tiêu học tập của ngày hôm đó và tổ chức một hoạt động phá băng (ice-breaker) để khuyến khích hợp tác giữa 348 người tham gia.

### 9:00 – 10:30 AM | Tổng quan dịch vụ AWS AI/ML

Phân đoạn này giới thiệu Amazon SageMaker như một nền tảng ML toàn diện:

- **Chuẩn bị & Gán nhãn dữ liệu:** Các kỹ thuật chuẩn bị tập dữ liệu và gán nhãn cho supervised learning
- **Huấn luyện & Điều chỉnh mô hình:** Tối ưu hóa siêu tham số (hyperparameter) và khả năng AutoML
- **Triển khai:** Di chuyển các mô hình đã huấn luyện đến production với hỗ trợ MLOps tích hợp
- **Demo trực tiếp:** Một bài hướng dẫn chi tiết về SageMaker Studio, cho thấy cách khởi chạy các thử nghiệm và giám sát công việc huấn luyện

Điểm chính: SageMaker loại bỏ nhu cầu quản lý cơ sở hạ tầng cơ bản đồng thời cung cấp kiểm soát toàn phần đối với huấn luyện và triển khai mô hình.

### 10:30 – 10:45 AM | Giờ cà phê

### 10:45 AM – 12:00 PM | Generative AI với Amazon Bedrock

Nửa thứ hai tập trung vào xây dựng với foundation models sử dụng Amazon Bedrock:

#### Tổng quan Foundation Models
- **So sánh Claude, Llama, Titan:** Các mô hình khác nhau cho các trường hợp sử dụng khác nhau (reasoning, sáng tạo, đa ngôn ngữ)
- **Hướng dẫn chọn mô hình:** Cách chọn mô hình đúng dựa trên độ trễ, chi phí và độ chính xác

#### Kỹ thuật Prompt Engineering
- **Chain-of-Thought Reasoning:** Chia nhỏ các vấn đề phức tạp thành các luồng công việc từng bước
- **Few-Shot Learning:** Sử dụng ví dụ để hướng dẫn hành vi của mô hình
- **Prompting nâng cao:** Mẫu để trích xuất dữ liệu có cấu trúc và kiểm soát định dạng đầu ra

#### Retrieval-Augmented Generation (RAG)
- **Kiến trúc & Tích hợp:** Kết nối các cơ sở kiến thức bên ngoài với Bedrock
- **Tích hợp Kho tri thức:** Giữ cho các mô hình cập nhật với dữ liệu độc quyền
- **Giảm Hallucinations:** Sử dụng retrieval để neo các phản hồi của mô hình vào sự thật

#### Bedrock Agents
- **Quy trình multi-bước:** Tự động hóa các quy trình kinh doanh phức tạp
- **Tích hợp công cụ:** Kết nối các mô hình với cơ sở dữ liệu, API và các dịch vụ khác
- **Xử lý lỗi:** Suy giảm uyển chuyển và logic thử lại

#### Bảo mật & Tuân thủ
- **Guardrails:** Các cơ chế lọc nội dung và an toàn của AWS
- **Lọc đầu ra:** Ngăn chặn các phản hồi có hại hoặc không thích hợp

#### Demo trực tiếp: Xây dựng Chatbot Generative AI
Các giảng viên đã trình diễn một chatbot được hỗ trợ bởi RAG hoàn chỉnh trên Bedrock, thể hiện:
1. Tải tài liệu và indexing cơ sở kiến thức
2. Xử lý truy vấn với retrieval
3. Suy luận mô hình với guardrails được áp dụng
4. Tạo ra phản hồi thời gian thực

## Suy tư cá nhân

### Những gì tôi đã học

Workshop làm rõ sự phân biệt giữa ML truyền thống (SageMaker) và generative AI (Bedrock). ML truyền thống vẫn cần thiết cho phân loại, hồi quy và dự báo chuỗi thời gian, trong khi Bedrock vượt trội ở việc hiểu văn bản, tạo tác và reasoning.

Sự nhấn mạnh thực tế về prompt engineering và RAG đã gây ấn tượng mạnh—các kỹ thuật này có thể áp dụng ngay lập tức và không cần kiến thức về machine learning để thực hiện.

### Những hiểu biết chính

1. **Foundation models đã sẵn sàng cho production:** AWS đã đầu tư nặng nề vào bảo mật, tuân thủ và mở rộng quy mô cho khối lượng công việc doanh nghiệp.
2. **RAG là cần thiết cho AI doanh nghiệp:** Các tổ chức không thể chỉ dựa vào foundation models; tích hợp kiến thức là quan trọng đối với độ chính xác.
3. **Prompt engineering là một kỹ năng thực sự:** Các prompt được xây dựng tốt và ví dụ few-shot có thể cải thiện đáng kể chất lượng đầu ra mô hình.
4. **Bối cảnh AI ở Việt Nam đang phát triển:** Với 348 người tham gia, rõ ràng là có động lực mạnh mẽ trong cộng đồng AI địa phương.

### Các bước tiếp theo

- Thử nghiệm với prompt playground của Bedrock cho các dự án nội bộ
- Thiết kế kiến trúc RAG cho kho kiến thức của đội ngũ của chúng tôi
- Đánh giá các trường hợp sử dụng nào được hưởng lợi từ foundation models so với ML truyền thống
- Xem xét AWS Canvas SageMaker để xây dựng mô hình low-code

## Một số hình ảnh từ sự kiện

![event-picture-1](/images/event-1/IMG_20251115_100905.jpg)
![event-picture-2](/images/event-1/IMG_20251115_101516%20(2).jpg)

> Workshop này là một nền tảng tuyệt vời để hiểu AI hiện đại trên AWS. Sự kết hợp giữa lý thuyết, các bài demo trực tiếp và khám phá thực hành đã tạo ra một giới thiệu toàn diện về cả quy trình ML truyền thống và generative AI.