import time
import json
import random
import sys
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient # pip install AWSIoTPythonSDK

# ======================================================
# CẤU HÌNH
# ======================================================
AWS_IOT_ENDPOINT = "a1w61tlrgpahml-ats.iot.ap-southeast-1.amazonaws.com" # <--- Thay Endpoint của bạn
THING_NAME = "dcb92f59-d2d3-4dcd-8816-926376f29a03_202"
ROOM_ID = "202"
OFFICE_ID = "dcb92f59-d2d3-4dcd-8816-926376f29a03"

ROOT_CA_PATH = "AmazonRootCA1.pem"
CERT_PATH = "certificate.pem.crt"
KEY_PATH = "private.pem.key"

TELEMETRY_TOPIC = f"smart-office/{OFFICE_ID}/{ROOM_ID}/telemetry"
SHADOW_UPDATE_TOPIC = f"$aws/things/{THING_NAME}/shadow/update"

# ======================================================
# KHỞI TẠO
# ======================================================
print(f"🔄 Đang khởi động thiết bị {THING_NAME}...")

myShadowClient = AWSIoTMQTTShadowClient(THING_NAME)
myShadowClient.configureEndpoint(AWS_IOT_ENDPOINT, 8883)
myShadowClient.configureCredentials(ROOT_CA_PATH, KEY_PATH, CERT_PATH)

# --- CẤU HÌNH LWT (LAST WILL) ---
# Nếu mất kết nối đột ngột, AWS sẽ tự động update Shadow thành OFFLINE
lwt_payload = json.dumps({
    "state": {
        "reported": {
            "connectionStatus": "OFFLINE"
        }
    }
})
# Cấu hình LWT phải làm TRƯỚC KHI connect
# Lưu ý: AWSIoTPythonSDK cũ cấu hình LWT qua MQTTClientCore, 
# nhưng để đơn giản ta sẽ handle việc Offline thủ công khi tắt script bằng Ctrl+C.
# LWT nâng cao cần truy cập vào _mqttCore, ở đây ta làm mức ứng dụng trước.

myShadowClient.configureAutoReconnectBackoffTime(1, 32, 20)
myShadowClient.configureConnectDisconnectTimeout(10)
myShadowClient.configureMQTTOperationTimeout(5)

try:
    myShadowClient.connect()
    print("✅ Kết nối mạng thành công (ONLINE)!")
except Exception as e:
    print(f"❌ Lỗi kết nối: {str(e)}")
    exit()

deviceShadowHandler = myShadowClient.createShadowHandlerWithName(THING_NAME, True)
mqtt_client_core = myShadowClient.getMQTTConnection()

# Hàm callback update Shadow
def shadowCallback(payload, responseStatus, token):
    if responseStatus == "accepted":
        print(f"   [Shadow] Update OK")
    else:
        print(f"   [Shadow] Update Failed: {responseStatus}")

# Hàm cập nhật Full trạng thái
def update_shadow_state(device_status, connection_status):
    payload = {
        "state": {
            "reported": {
                "deviceStatus": device_status,       # ON / OFF
                "connectionStatus": connection_status, # ONLINE / OFFLINE
                "timestamp": int(time.time())
            }
        }
    }
    deviceShadowHandler.shadowUpdate(json.dumps(payload), shadowCallback, 5)

# ======================================================
# CHƯƠNG TRÌNH CHÍNH
# ======================================================
try:
    # 1. Bắt đầu: MÁY BẬT - MẠNG ONLINE
    current_device_status = "ON"
    update_shadow_state("ON", "ONLINE")
    
    start_time = int(time.time())
    
    while True:
        current_time = int(time.time())
        
        # --- LOGIC GIẢ LẬP: SAU 60 GIÂY TỰ ĐỘNG TẮT MÁY (OFF) ---
        # (Nhưng vẫn giữ kết nối mạng)
        if current_device_status == "ON" and (current_time - start_time) > 15:
            print("\n⚠️ [USER REQUEST] Yêu cầu tắt thiết bị...")
            current_device_status = "OFF"
            # Cập nhật Shadow: Device OFF, Connection vẫn ONLINE
            update_shadow_state("OFF", "ONLINE") 
            print("💤 Thiết bị đã chuyển sang chế độ chờ (Standby).\n")

        # --- XỬ LÝ THEO TRẠNG THÁI ---
        if current_device_status == "ON":
            # [ON]: Gửi dữ liệu cảm biến bình thường
            temperature = int(round(random.uniform(25.0, 32.0)))
            humidity = int(round(random.uniform(60.0, 80.0)))
            
            telemetry_payload = {
                "roomId": ROOM_ID,
                "officeId": OFFICE_ID,
                "temperature": temperature,
                "humidity": humidity,
                "light": random.randint(300, 500),
                "timestamp": current_time,
                "expireAt": current_time + (48 * 3600)
            }
            mqtt_client_core.publish(TELEMETRY_TOPIC, json.dumps(telemetry_payload), 1)
            print(f"🟢 [ON - Sending Data] Temp={temperature}")
            
        else:
            # [OFF]: Không gửi data cảm biến, chỉ duy trì kết nối
            # Có thể gửi heartbeat nhẹ nếu muốn
            print(f"🔴 [OFF - Connected] Thiết bị đang tắt. Vẫn giữ kết nối...")

        time.sleep(5)

except KeyboardInterrupt:
    print("\n🛑 Đang ngắt kết nối hoàn toàn...")
    
    # Cập nhật lần cuối: Connection OFFLINE
    # (Lưu ý: Device Status giữ nguyên trạng thái cuối cùng của nó)
    update_shadow_state(current_device_status, "OFFLINE")
    
    time.sleep(2)
    myShadowClient.disconnect()
    print("Đã thoát.")