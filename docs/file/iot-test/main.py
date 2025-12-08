import time
import json
import random
from awscrt import io, mqtt 
from awsiot import mqtt_connection_builder, iotshadow

# ======================================================
# 1. CẤU HÌNH
# ======================================================
ENDPOINT = "a18g0l0koofjed-ats.iot.ap-southeast-1.amazonaws.com"
CLIENT_ID = "HoChiMinh_Room1"
OFFICE_ID = "37e90376-84a7-412a-95e0-0f3393bd9f22"
ROOM_ID = "Room1"
THING_NAME = CLIENT_ID 

PATH_TO_CERT = "certs/device-cert.pem.crt"
PATH_TO_KEY = "certs/private.pem.key"
PATH_TO_ROOT = "certs/AmazonRootCA1.pem"

TOPIC_TELEMETRY = f"office/{OFFICE_ID}/room/{ROOM_ID}/telemetry"
TOPIC_CONFIG = f"office/{OFFICE_ID}/room/{ROOM_ID}/config"

# ======================================================
# 2. TRẠNG THÁI THIẾT BỊ (GLOBAL STATE)
# ======================================================
state = {
    "target_temp": 26.0,
    "target_hum": 60.0,
    "target_light": 300,
    "temp_mode": "auto",
    "humid_mode": "auto",
    "light_mode": "auto",
    "auto_control": "ON", 
    "status": "OFF" 
}

shadow_client = None

# ======================================================
# 3. HÀM CẬP NHẬT SHADOW
# ======================================================
def update_shadow_reported(device_status, connection_status):
    """
    Cập nhật Shadow:
    - deviceStatus: Lấy từ biến state['status'] (ON/OFF)
    - connectionStatus: Truyền vào trực tiếp (ONLINE/OFFLINE)
    """
    if shadow_client is None: return

    try:
        # Payload chuẩn
        shadow_payload = {
            "state": {
                "reported": {
                    "deviceStatus": str(device_status),      
                    "connectionStatus": str(connection_status),
                    "timestamp": int(time.time())
                }
            }
        }
        
        # Gửi update (Non-blocking)
        future = shadow_client.publish_update_shadow(
            request=iotshadow.UpdateShadowRequest(
                thing_name=THING_NAME,
                state=iotshadow.ShadowState(
                    reported=shadow_payload["state"]["reported"]
                )
            ),
            qos=mqtt.QoS.AT_LEAST_ONCE
        )
        
        future.add_done_callback(lambda f: print("✅ [Shadow] Update OK") if not f.exception() else print(f"❌ [Shadow] Lỗi: {f.exception()}"))
        
    except Exception as e:
        print(f"❌ [Shadow] Lỗi code: {e}")

# ======================================================
# 4. HÀM XỬ LÝ CONFIG (Từ Web/Automation)
# ======================================================
def on_config_received(topic, payload, dup, qos, retain, **kwargs):
    try:
        msg = json.loads(payload)
        has_changed = False
        status_changed = False
        log_changes = []

        def update_if_changed(key, new_val, cast_func=None):
            if key not in state: return False
            val = cast_func(new_val) if cast_func else new_val
            if str(state[key]) != str(val):
                old_val = state[key]
                state[key] = val
                log_changes.append(f"   👉 {key}: {old_val} -> {val}")
                return True
            return False

        # Cập nhật thông số môi trường
        if 'temp' in msg: update_if_changed('target_temp', msg['temp'], float) 
        if 'hum' in msg: update_if_changed('target_hum', msg['hum'], float)
        if 'light' in msg: update_if_changed('target_light', msg['light'], int)
        
        # Cập nhật Auto Control
        if 'autoControl' in msg:
            update_if_changed('auto_control', msg['autoControl'], str)

        # Cập nhật Status (ON/OFF) từ lệnh
        if 'value' in msg:
            new_status = str(msg['value'])
            if state["status"] != new_status:
                state["status"] = new_status
                status_changed = True
                log_changes.append(f"   👉 STATUS: Đổi thành {new_status}")

        if has_changed or log_changes or status_changed:
            print(f"\n🔔 CÓ CONFIG MỚI:")
            for log in log_changes: print(log)

            # Nếu trạng thái ON/OFF thay đổi -> Cập nhật Shadow ngay
            if status_changed:
                update_shadow_reported(state["status"], "ONLINE")
            
    except Exception as e:
        print(f"❌ Lỗi đọc config: {e}")

# ======================================================
# 5. CHƯƠNG TRÌNH CHÍNH
# ======================================================
def main():
    global shadow_client

    event_loop_group = io.EventLoopGroup(1)
    host_resolver = io.DefaultHostResolver(event_loop_group)
    client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
    
    # --- CẤU HÌNH LAST WILL (LWT) ---
    lwt_message = {
        "state": {
            "reported": {
                "connectionStatus": "OFFLINE"
            }
        }
    }
    
    mqtt_connection = mqtt_connection_builder.mtls_from_path(
        endpoint=ENDPOINT,
        cert_filepath=PATH_TO_CERT,
        pri_key_filepath=PATH_TO_KEY,
        client_bootstrap=client_bootstrap,
        ca_filepath=PATH_TO_ROOT,
        client_id=CLIENT_ID,
        clean_session=False,
        keep_alive_secs=30,
        will=mqtt.Will(
            topic=f"$aws/things/{THING_NAME}/shadow/update",
            qos=mqtt.QoS.AT_LEAST_ONCE,
            payload=json.dumps(lwt_message).encode('utf-8'), 
            retain=False 
        )
    )
    
    print(f"Connecting to AWS IoT as {CLIENT_ID}...")
    mqtt_connection.connect().result()
    print("✅ Connected Successfully!")

    # Khởi tạo Shadow Client
    shadow_client = iotshadow.IotShadowClient(mqtt_connection)
    
    # [STARTUP] Báo cáo trạng thái ban đầu: OFF, ONLINE
    update_shadow_reported(state["status"], "ONLINE")

    # Subscribe Config
    mqtt_connection.subscribe(
        topic=TOPIC_CONFIG,
        qos=mqtt.QoS.AT_LEAST_ONCE,
        callback=on_config_received
    )
    print(f"🎧 Đang lắng nghe Config tại: .../config")

    try:
        while True:
            current_time = int(time.time())
            payload = {}

            if state['status'] == 'OFF':
                # [OFF]: Gửi data rác (0) + status OFF
                payload = {
                    "roomId": ROOM_ID,
                    "officeId": OFFICE_ID,
                    "temperature": 0, 
                    "humidity": 0,
                    "light": 0,
                    "status": "OFF", 
                    "timestamp": current_time,
                    "expireAt": current_time + (3 * 24 * 60 * 60)
                }
                print(f"💤 Thiết bị đang OFF. Gửi data 0.")
            else:
                # [ON]: Gửi data giả lập + status ON
                sim_temp = state['target_temp'] + random.uniform(-0.5, 0.5)
                sim_hum = state['target_hum'] + random.uniform(-2.0, 2.0)
                sim_light = state['target_light'] 
                if sim_light < 0: sim_light = 0

                payload = {
                    "roomId": ROOM_ID,
                    "officeId": OFFICE_ID,
                    "temperature": round(sim_temp, 1),
                    "humidity": round(sim_hum, 1),
                    "light": int(sim_light), 
                    "status": "ON", 
                    "timestamp": current_time,
                    "expireAt": current_time + (3 * 24 * 60 * 60)
                }
                print(f"📡 Gửi: Temp={payload['temperature']} | Hum={payload['humidity']} | Light={payload['light']}")

            # Gửi Telemetry
            mqtt_connection.publish(
                topic=TOPIC_TELEMETRY,
                payload=json.dumps(payload),
                qos=mqtt.QoS.AT_LEAST_ONCE
            )
            
            time.sleep(5) 

    except KeyboardInterrupt:
        print("\nStopping...")
        # [SHUTDOWN] Báo connectionStatus = OFFLINE
        try:
            update_shadow_reported(state["status"], "OFFLINE")
            time.sleep(1)
        except:
            pass
        mqtt_connection.disconnect().result()

if __name__ == '__main__':
    main()