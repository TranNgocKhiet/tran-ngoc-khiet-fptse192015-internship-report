import time
import json
import random
from awscrt import io, mqtt # pip install awscrt
from awsiot import mqtt_connection_builder # pip install awsiot

# --- 1. CẤU HÌNH KẾT NỐI (SỬA LẠI THEO CỦA BẠN) ---
ENDPOINT = "a18g0l0koofjed-ats.iot.ap-southeast-1.amazonaws.com"
CLIENT_ID = "HCM_test1"
OFFICE_ID = "6c92bc28-45d5-4475-af7e-e34590cc4d6c"
ROOM_ID = "test1"

# Đường dẫn chứng chỉ
PATH_TO_CERT = "certs/device-cert.pem.crt"
PATH_TO_KEY = "certs/private.pem.key"
PATH_TO_ROOT = "certs/AmazonRootCA1.pem"

# Topic
TOPIC_TELEMETRY = f"office/{OFFICE_ID}/room/{ROOM_ID}/telemetry"
TOPIC_CONFIG = f"office/{OFFICE_ID}/room/{ROOM_ID}/config"

# --- 2. TRẠNG THÁI THIẾT BỊ (GLOBAL STATE) ---
# Đây là các giá trị "Mục tiêu" mà bạn chỉnh từ Web
state = {
    "target_temp": 25.0,  # Độ C
    "target_hum": 60.0,   # %
    "target_light": 300   # Lux
}

# --- 3. HÀM XỬ LÝ KHI NHẬN CONFIG TỪ WEB ---
def on_config_received(topic, payload, dup, qos, retain, **kwargs):
    print(f"\n🔔 CÓ CONFIG MỚI TỪ SERVER!")
    try:
        msg = json.loads(payload)
        print(f"📥 Nội dung lệnh: {msg}")
        
        # Cập nhật trạng thái nếu có trong lệnh
        if 'temp' in msg:
            state['target_temp'] = float(msg['temp'])
            print(f"   👉 Set Nhiệt độ mục tiêu: {state['target_temp']}°C")
            
        if 'hum' in msg:
            state['target_hum'] = float(msg['hum'])
            print(f"   👉 Set Độ ẩm mục tiêu: {state['target_hum']}%")

        if 'light' in msg:
            state['target_light'] = int(msg['light'])
            print(f"   👉 Set Ánh sáng mục tiêu: {state['target_light']} Lux")
            
    except Exception as e:
        print(f"❌ Lỗi đọc config: {e}")

# --- 4. CHƯƠNG TRÌNH CHÍNH ---
def main():
    # Khởi tạo kết nối MQTT
    event_loop_group = io.EventLoopGroup(1)
    host_resolver = io.DefaultHostResolver(event_loop_group)
    client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
    
    mqtt_connection = mqtt_connection_builder.mtls_from_path(
        endpoint=ENDPOINT,
        cert_filepath=PATH_TO_CERT,
        pri_key_filepath=PATH_TO_KEY,
        client_bootstrap=client_bootstrap,
        ca_filepath=PATH_TO_ROOT,
        client_id=CLIENT_ID,
        clean_session=False,
        keep_alive_secs=30
    )
    
    print(f"Connecting to AWS IoT as {CLIENT_ID}...")
    mqtt_connection.connect().result()
    print("✅ Connected Successfully!")

    # Đăng ký nhận tin Config
    mqtt_connection.subscribe(
        topic=TOPIC_CONFIG,
        qos=mqtt.QoS.AT_LEAST_ONCE,
        callback=on_config_received
    )
    print(f"🎧 Đang lắng nghe Config tại: .../config")

    # Vòng lặp gửi data liên tục
    try:
        while True:
            # --- GIẢ LẬP SỐ LIỆU CẢM BIẾN ---
            # Tạo dao động ngẫu nhiên quanh mức target để biểu đồ trông thực tế hơn
            
            # Nhiệt độ: Dao động +/- 0.5 độ
            sim_temp = state['target_temp'] + random.uniform(-0.5, 0.5)
            
            # Độ ẩm: Dao động +/- 2%
            sim_hum = state['target_hum'] + random.uniform(-2.0, 2.0)
            
            # Ánh sáng: Dao động +/- 10 Lux (Ví dụ bóng đèn chớp tắt nhẹ hoặc bóng râm)
            sim_light = state['target_light'] + random.randint(-10, 10)
            # Đảm bảo ánh sáng không âm
            if sim_light < 0: sim_light = 0

            current_time = int(time.time())

            # Tạo gói tin JSON (Khớp với Lambda SaveSensorData)
            payload = {
                "roomId": ROOM_ID,
                "officeId": OFFICE_ID,
                "temperature": round(sim_temp, 1),
                "humidity": round(sim_hum, 1),
                "lighting": int(sim_light),     # <--- Đã thêm Ánh Sáng đầy đủ
                "timestamp": current_time,
                "expireAt": current_time + (3 * 24 * 60 * 60) # TTL 3 ngày
            }
            
            # Gửi lên AWS
            mqtt_connection.publish(
                topic=TOPIC_TELEMETRY,
                payload=json.dumps(payload),
                qos=mqtt.QoS.AT_LEAST_ONCE
            )
            
            # In log đẹp để dễ theo dõi
            print(f"📡 Gửi: Temp={payload['temperature']}°C | Hum={payload['humidity']}% | Light={payload['lighting']} Lux")
            
            time.sleep(5) # Gửi mỗi 5 giây

    except KeyboardInterrupt:
        print("\nStopping...")
        mqtt_connection.disconnect().result()

if __name__ == '__main__':
    main()