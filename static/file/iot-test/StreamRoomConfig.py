import json
import boto3
from boto3.dynamodb.types import TypeDeserializer

iot = boto3.client('iot-data', region_name='ap-southeast-1')
deserializer = TypeDeserializer()

def deserialize(image):
    d = {}
    for key in image:
        d[key] = deserializer.deserialize(image[key])
    return d

def lambda_handler(event, context):
    try:
        for record in event['Records']:
            if record['eventName'] in ['MODIFY', 'INSERT']:
                
                print(f"EventID: {record['eventID']}")
                
                if 'NewImage' not in record['dynamodb']:
                    continue
                    
                new_image = record['dynamodb']['NewImage']
                data = deserialize(new_image)
                
                # Lấy ID
                room_id = data.get('roomId')
                office_id = data.get('officeId')
                
                if not room_id or not office_id:
                    continue

                # --- CHUẨN BỊ PAYLOAD GỬI XUỐNG THIẾT BỊ ---
                payload = {}
                
                # 1. Nhiệt độ
                if 'targetTemperature' in data:
                    payload['temp'] = float(data['targetTemperature'])
                
                # 2. Ánh sáng
                if 'targetLight' in data:
                    payload['light'] = int(data['targetLight'])
                    
                # 3. [MỚI] Độ ẩm (Giả sử trong DB cột tên là 'targetHum')
                if 'targetHumidity' in data:
                    payload['hum'] = float(data['targetHumidity'])
                
                # Nếu không có gì thay đổi thì bỏ qua
                if not payload:
                    print("Không có dữ liệu config (Temp/Light/Hum)")
                    continue

                # Bắn xuống MQTT
                topic = f"office/{office_id}/room/{room_id}/config"
                print(f"📡 Sending to {topic}: {payload}")
                
                iot.publish(
                    topic=topic,
                    qos=1,
                    payload=json.dumps(payload)
                )

        return {'statusCode': 200, 'body': 'Processed'}

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return {'statusCode': 200, 'body': str(e)}