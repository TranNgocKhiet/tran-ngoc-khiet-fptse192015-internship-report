---
title : "Kiểm thử kết nối giữa website và thiết bị IoT"
weight : 7
chapter : false
pre : " <b> 5.7. </b> "
---

#### Tải kịch bản giả lập thiết bị IoT

[main.py](/file/iot-test/main.py)

#### Thêm dữ liệu cho thiết bị giả

```yaml
ENDPOINT = ""
CLIENT_ID = ""
OFFICE_ID = ""
ROOM_ID = ""

PATH_TO_CERT = ""
PATH_TO_KEY = ""
PATH_TO_ROOT = ""
```

| Thuộc tính   | Giá trị 												            |
|--------------|--------------------------------------------------------------------|
| ENDPOINT     | Trên trang manager                                                 |
| CLIENT_ID    | ID của office của bạn	                                            |
| OFFICE_ID    | Tên office của bạn	                                                |
| ROOM_ID      | ID phòng của bạn                                                   |
| PATH_TO_CERT | Đường dẫn tải xuống chứng chỉ thiết bị của bạn khi bạn tạo phòng   |
| PATH_TO_KEY  | Đường dẫn tải xuống khóa riêng của thiết bị khi bạn tạo phòng      |
| PATH_TO_ROOT | Đường dẫn tải xuống chứng chỉ gốc Amazon của bạn khi bạn tạo phòng |

## Link video demo
