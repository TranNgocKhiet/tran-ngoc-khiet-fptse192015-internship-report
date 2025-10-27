---
title : "Tạo các bảng"
weight : 1
chapter : false
pre : " <b> 5.3.1 </b> "
---

1. Mở **Management Console**, tìm và chọn ```DynamoDB```

![DynamoDB 1](/images/5-workshop/5.3-DynamoDB/DynamoDB-1.png)

2. Điều hướng đến tab **Tables**, nhấn **Create table**

![DynamoDB 2](/images/5-workshop/5.3-DynamoDB/DynamoDB-2.png)

3. Tại **Table name**, nhập ```SmartOffice_RoomLog_Prod```  
4. Tại **Partition key**, nhập ```roomId```  
5. Tại **Sort Key**, nhập ```timestamp```  
6. Trong **Table settings**, chọn **Customize settings**

![DynamoDB 3](/images/5-workshop/5.3-DynamoDB/DynamoDB-3.png)

7. Trong trường **Table class**, chọn **DynamoDB Standard-IA**
   
{{% notice info %}}
Log sensor có tần suất truy cập thấp, cần tối ưu chi phí lưu trữ.
{{% /notice %}}

![DynamoDB 3](/images/5-workshop/5.3-DynamoDB/DynamoDB-4.png)   

8. Giữ nguyên các thiết lập khác ở mặc định  
9. Thêm **Tag** để quản lý (**Key**: ```Project```, **Value**: ```SmartOffice```; **Key**: ```Environment```, **Value**: ```Dev```)  
10. Nhấn **Create table**   

---

## Tương tự cho bảng:
### SmartOffice_User_Prod
- **Name**: ```SmartOffice_User_Prod```
- **Partition key**: ```userId```
- **Table settings**: **Customize settings**
- **Deletion protection**: chọn **Turn on deletion protection**
- **Tag** : **Key**: ```Project```, **Value**: ```SmartOffice```; **Key**: ```Environment```, **Value**: ```Dev```

### SmartOffice_Office_Prod
- **Name**: ```SmartOffice_Office_Prod```
- **Partition key**: ```officeId```
- **Table settings**: **Customize settings**
- **Deletion protection**: chọn **Turn on deletion protection**
- **Tag** : **Key**: ```Project```, **Value**: ```SmartOffice```; **Key**: ```Environment```, **Value**: ```Dev```

### SmartOffice_RoomConfig_Prod
- **Name**: ```SmartOffice_RoomConfig_Prod```
- **Partition key**: ```roomId```
- **Table settings**: **Customize settings**
- **Deletion protection**: chọn **Turn on deletion protection**
- **Tag** : **Key**: ```Project```, **Value**: ```SmartOffice```; **Key**: ```Environment```, **Value**: ```Dev```