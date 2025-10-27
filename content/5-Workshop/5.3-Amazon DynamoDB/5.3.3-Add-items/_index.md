---
title : "Add item to tables"
weight : 3
chapter : false
pre : " <b> 5.3.3 </b> "
---

1. In tab **Tables**, choose **SmartOffice_User_Prod**

![DynamoDB 5](/images/5-workshop/5.3-DynamoDB/DynamoDB-5.png)

2. Choose **Action**, **Create item**

![DynamoDB 10](/images/5-workshop/5.3-DynamoDB/DynamoDB-10.png)

3. Choose **JSON view**, turn off **View DynamoDB JSON**
4. Enter 
```
{
 "userId": "user-001",
 "companyId": "comp-abc",
 "name": "Nguyen Van A",
 "email": "a@abc.com",
 "role": "admin",
 "offices": [
  "office-hcm",
  "office-hn"
 ]
}
```

![DynamoDB 11](/images/5-workshop/5.3-DynamoDB/DynamoDB-11.png)

5. Click **Create item**

---

## Same for table:
### SmartOffice_Office_Prod
```
{
  "officeId": "office-hcm",
  "companyId": "comp-abc",
  "officeName": "Headquarters HCM",
  "location": "Ho Chi Minh City",
  "latitude": 10.762622,
  "longitude": 106.660172,
  "timezone": "Asia/Ho_Chi_Minh",
  "rooms": ["A101", "A102", "A103", "A104"]
}
```

### SmartOffice_RoomConfig_Prod
```
{
"roomId": "A101",
"officeId": "office-hcm",
"temperatureMode": "auto",
"humidityMode": "manual",
"lightMode": "off",
"targetTemperature": 26,
"targetHumidity": 60,
"targetLight": 300,
"lastUpdate": "2025-10-16T14:05:00Z",
"autoOnTime": "18:00",
"autoOffTime": "22:00"
}
```

### SmartOffice_RoomLog_Prod
```
{
  "roomId": "A101",
  "timestamp": "1734355200",
  "temperature": 30,
  "humidity": 70,
  "light": 400,
  "expireAt": 1734528000
}
```