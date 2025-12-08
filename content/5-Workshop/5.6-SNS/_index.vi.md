---
title : "Thiết lập SNS"
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

#### Tổng quan
Phần này sẽ hướng dẫn bạn cách thiết lập **Amazon SNS (Dịch vụ Thông báo Đơn giản)** để nhận cảnh báo từ EventBridge khi phát hiện bất thường dữ liệu.


---

#### Tạo Topic SNS

1. Đi tới Bảng điều khiển **Amazon SNS**
2. Chọn **Topic** và đặt tên cho **Topic** của bạn

{{% notice warning %}}
KHÔNG BẬT MÃ HÓA
{{% /notice %}}

![sns.png](/images/5-Workshop/5.6-SNS/sns.png)

#### Tạo Subscription SNS

Sau khi tạo chủ đề, hãy tạo một hoặc nhiều đăng ký để cảnh báo được gửi đến người nhận hoặc điểm cuối (trong trường hợp này, **email**).

Các bước:
1. Chọn **Subscription** trong **SNS**
2. Chọn giao thức **email**, chọn **topic** bạn vừa tạo và ghi lại email bạn muốn kiểm tra.

![subcription.png](/images/5-Workshop/5.6-SNS/subcription.png)

Các điểm cuối email yêu cầu xác nhận trước khi nhận các tin nhắn. Kiểm tra hộp thư của bạn để tìm email xác nhận từ AWS SNS và xác nhận đăng ký.

![email.png](/images/5-Workshop/5.6-SNS/email.png)

---

#### Tạo một rule và gắn nó vào topic SNS

1. Đi tới Bảng điều khiển **Amazon EventBridge** 
2. Chọn **Rules** và tạo một **rule** mới

![rule_1.png](/images/5-Workshop/5.6-SNS/rule_1.png)

3. Ở bước 2, chúng tôi xác định mẫu sự kiện bằng cách chọn **Custom pattern**. Các mẫu sự kiện có thể khớp với `source`, `detail-type`.

4. Sử dụng Json sau:

```
{
  "source": ["com.smartoffice.iot"],
  "detail-type": ["sensor.anomaly"]
}
```

![rule_2.png](/images/5-Workshop/5.6-SNS/rule_2.png)

5. Ở bước 3, chọn mục tiêu cho quy tắc — chọn **topic SNS** bạn đã tạo trước đó.

![rule_3.png](/images/5-Workshop/5.6-SNS/rule_3.png)

Sau khi tạo, **EventBridge** sẽ chuyển tiếp các sự kiện phù hợp đến **topic SNS** sẽ chuyển đến các đăng ký của nó.

![rule_4.png](/images/5-Workshop/5.6-SNS/rule_4.png)

{{% notice warning %}}
Thay thế địa chỉ email và tên tài nguyên bằng các giá trị từ tài khoản của bạn trước khi chạy.
{{% /notice %}}
