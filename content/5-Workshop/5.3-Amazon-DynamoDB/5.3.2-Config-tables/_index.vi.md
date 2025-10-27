---
title : "Cấu hình các bảng"
weight : 2
chapter : false
pre : " <b> 5.3.2 </b> "
---

### Cấu hình Time to Live (TTL) cho bảng SmartOffice_RoomLog_Prod

1. Trong tab **Tables**, chọn **SmartOffice_RoomLog_Prod**

![DynamoDB 5](/images/5-workshop/5.3-DynamoDB/DynamoDB-5.png)

2. Điều hướng đến tab **Settings**, trong trường **Time to Live (TTL)** nhấn **Turn on**

![DynamoDB 6](/images/5-workshop/5.3-DynamoDB/DynamoDB-6.png)

3. Tại **TTL attribute name**, nhập ```expireAt```  
4. Tại **Simulated date and time**, chọn **Epoch time value**, nhập ```1770000000```
   
![DynamoDB 7](/images/5-workshop/5.3-DynamoDB/DynamoDB-7.png)

5. Nhấn **Turn on TTL**

---

### Cấu hình Point-in-time recovery (PITR) cho các bảng SmartOffice_User_Prod, SmartOffice_Office_Prod và SmartOffice_RoomConfig_Prod

1. Trong tab **Tables**, chọn **SmartOffice_User_Prod**
   
![DynamoDB 5](/images/5-workshop/5.3-DynamoDB/DynamoDB-5.png)

2. Điều hướng đến tab **Backups**, trong trường **Point-in-time recovery (PITR)**, nhấn **Edit**
   
![DynamoDB 8](/images/5-workshop/5.3-DynamoDB/DynamoDB-8.png)

3. Chọn **Turn on point-in-time recovery**  
4. Trong trường **Backup recovery period**, chọn **35** days

![DynamoDB 9](/images/5-workshop/5.3-DynamoDB/DynamoDB-9.png)

5. Nhấn **Save changes**  
6. Thực hiện tương tự cho bảng **SmartOffice_Office_Prod** và **SmartOffice_RoomConfig_Prod**

---

### Cấu hình DynamoDB stream cho bảng SmartOffice_RoomConfig_Prod

1. Trong tab **Tables**, chọn **SmartOffice_RoomConfig_Prod**

![DynamoDB 5](/images/5-workshop/5.3-DynamoDB/DynamoDB-5.png)

2. Điều hướng đến tab **Exports and streams**, trong trường **DynamoDB stream details**, nhấn **Turn on**

![DynamoDB 12](/images/5-workshop/5.3-DynamoDB/DynamoDB-12.png)

3. Trong trường **View type**, chọn **New and old images**

![DynamoDB 13](/images/5-workshop/5.3-DynamoDB/DynamoDB-13.png)

4. Nhấn **Turn on stream**
