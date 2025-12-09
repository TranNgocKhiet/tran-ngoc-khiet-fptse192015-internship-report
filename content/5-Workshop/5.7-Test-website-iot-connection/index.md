---
title : "Test website and IoT connection"
weight : 7
chapter : false
pre : " <b> 5.7. </b> "
---

#### Download mock IoT device script

[main.py](/file/iot-test/main.py)

#### Add data from your mock device

```yaml
ENDPOINT = ""
CLIENT_ID = ""
OFFICE_ID = ""
ROOM_ID = ""

PATH_TO_CERT = ""
PATH_TO_KEY = ""
PATH_TO_ROOT = ""
```

| Attribute    | Value 													           |
|--------------|-------------------------------------------------------------------|
| ENDPOINT     | Website manager page                                              |
| CLIENT_ID    | ID of your office	                                               |
| OFFICE_ID    | Name of your office                                               |
| ROOM_ID      | ID of your room                                                   |
| PATH_TO_CERT | Path to your device certificate download when your create room    |
| PATH_TO_KEY  | Path to your device private key download when your create room    |
| PATH_TO_ROOT | Path to your Amazon root certifica	download when your create room |

## Link video demo

<https://www.youtube.com/watch?v=k45jHjkKhuc>