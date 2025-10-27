---
title : "Config tables"
weight : 2
chapter : false
pre : " <b> 5.3.2 </b> "
---

### Config TTL for table SmartOffice_RoomLog_Prod

1. In tab **Tables**, choose **SmartOffice_RoomLog_Prod**

![DynamoDB 5](/images/5-workshop/5.3-DynamoDB/DynamoDB-5.png)

2. Navigate to tab **Settings**, in the field **Time to Live (TTL)** click **Turn on**

![DynamoDB 6](/images/5-workshop/5.3-DynamoDB/DynamoDB-6.png)

3. For **TTL attribute name**, enter ```expireAt```
4. For **Simulated date and time**, choose **Epoch time value**, enter ```1770000000```
   
![DynamoDB 7](/images/5-workshop/5.3-DynamoDB/DynamoDB-7.png)

5. Click turn on TTL

---

### Config Point-in-time recovery (PITR) for table SmartOffice_User_Prod, SmartOffice_Office_Prod and SmartOffice_RoomConfig_Prod

1. In tab **Tables**, choose **SmartOffice_User_Prod**
   
![DynamoDB 5](/images/5-workshop/5.3-DynamoDB/DynamoDB-5.png)

2. Navigate to tab **Backups**, in the field **Point-in-time recovery (PITR)**, click **Edit**
   
![DynamoDB 8](/images/5-workshop/5.3-DynamoDB/DynamoDB-8.png)

3. Check **Turn on point-in-time recovery**
4. For **Backup recovery period** choose **35** days

![DynamoDB 9](/images/5-workshop/5.3-DynamoDB/DynamoDB-9.png)

5. Click **Save changes**
6. Do the same for table **SmartOffice_Office_Prod** and **SmartOffice_RoomConfig_Prod**

---

### Config DynamoDB stream for table SmartOffice_RoomConfig_Prod

1. In tab **Tables**, choose **SmartOffice_RoomConfig_Prod**

![DynamoDB 5](/images/5-workshop/5.3-DynamoDB/DynamoDB-5.png)

2. Navigate to tab **Exports and streams**, in the field **DynamoDB stream details**, click **Turn on**

![DynamoDB 12](/images/5-workshop/5.3-DynamoDB/DynamoDB-12.png)

3. For **View type**, choose **New and old images**

![DynamoDB 13](/images/5-workshop/5.3-DynamoDB/DynamoDB-13.png)

4. Click **Turn on stream**
