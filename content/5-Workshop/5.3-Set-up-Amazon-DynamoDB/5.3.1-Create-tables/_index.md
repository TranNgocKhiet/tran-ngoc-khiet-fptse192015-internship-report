---
title : "Create tables"
weight : 1
chapter : false
pre : " <b> 5.3.1 </b> "
---

1. Open **Management Console**, search and choose ```DynamoDB```.

![DynamoDB 1](/images/5-Workshop/5.3-DynamoDB/DynamoDB-1.png)

2. Navigate to tab **Tables**, click **Create table**

![DynamoDB 2](/images/5-Workshop/5.3-DynamoDB/DynamoDB-2.png)

3. For **Table name**, enter ```SmartOffice_RoomLog_Prod```
4. For **Partition key**, enter ```roomId```
5. For **Sort Key**, enter ```timestamp```
6. For **Table settings**, choose **Customize settings**

![DynamoDB 3](/images/5-Workshop/5.3-DynamoDB/DynamoDB-3.png)

7. For **Table class**, choose **DynamoDB Standard-IA**
   
{{% notice info %}}
Log sensor with less access, need to optimize storage pricing.
{{% /notice %}}

![DynamoDB 3](/images/5-Workshop/5.3-DynamoDB/DynamoDB-4.png)   

8. Leave other setting at default
9. Add **Tag** for management (**Key**: ```Project```, **Value**: ```SmartOffice```; **Key**: ```Environment```, **Value**: ```Dev```)
10. Click **Create table**   
 
---
 
## Do the same for table:
### SmartOffice_User_Prod
- **Name**: ```SmartOffice_User_Prod```
- **Partition key**: ```userId```
- **Table settings**: **Customize settings**
- **Deletion protection**: Check **Turn on deletion protection**
- **Tag** : **Key**: ```Project```, **Value**: ```SmartOffice```; **Key**: ```Environment```, **Value**: ```Dev```

### SmartOffice_Office_Prod
- **Name**: ```SmartOffice_Office_Prod```
- **Partition key**: ```officeId```
- **Table settings**: **Customize settings**
- **Deletion protection**: Check **Turn on deletion protection**
- **Tag** : **Key**: ```Project```, **Value**: ```SmartOffice```; **Key**: ```Environment```, **Value**: ```Dev```

### SmartOffice_RoomConfig_Prod
- **Name**: ```SmartOffice_RoomConfig_Prod```
- **Partition key**: ```roomId```
- **Table settings**: **Customize settings**
- **Deletion protection**: Check **Turn on deletion protection**
- **Tag** : **Key**: ```Project```, **Value**: ```SmartOffice```; **Key**: ```Environment```, **Value**: ```Dev```