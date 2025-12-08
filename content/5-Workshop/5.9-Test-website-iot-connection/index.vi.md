---
title : "Kiểm thử kết nối giữa website và thiết bị IoT"
weight : 9
chapter : false
pre : " <b> 5.9. </b> "
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

| Thuộc tính   | Giá trị 												                     |
|--------------|-----------------------------------------------------------------------------|
| ENDPOINT     | **IoT Core** > **MQTT test client** > **Connection details** > **Endpoint** |
| CLIENT_ID    | ID of your office	                                                         |
| OFFICE_ID    | Name of your office                                                         |
| ROOM_ID      | ID of your room                                                             |
| PATH_TO_CERT | Path to your device certificate                                             |
| PATH_TO_KEY  | Path to your device private key 			                                 |
| PATH_TO_ROOT | Path to your Amazon root certifica			                                 |
