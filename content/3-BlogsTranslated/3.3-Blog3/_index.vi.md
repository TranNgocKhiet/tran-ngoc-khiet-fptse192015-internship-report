---
title: "Blog 3"
weight: 1
chapter: false
pre: " <b> 3.3. </b> "
---

# Vận hành hiệu quả khối lượng công việc Windows Server BYOL trên AWS

Tác giả: Ali Alzand, Jon Madison, và Mike Gupta | ngày 01 tháng 7, 2025 | trong [Amazon EC2](https://aws.amazon.com/blogs/modernizing-with-aws/category/compute/amazon-ec2/), [AWS Config](https://aws.amazon.com/blogs/modernizing-with-aws/category/management-tools/aws-config/), [AWS Cost and Usage Report](https://aws.amazon.com/blogs/modernizing-with-aws/category/aws-cloud-financial-management/aws-cost-and-usage-report/), [AWS License Manager](https://aws.amazon.com/blogs/modernizing-with-aws/category/management-tools/aws-license-manager/), [AWS Migration Hub](https://aws.amazon.com/blogs/modernizing-with-aws/category/migration/aws-migration-hub/), [Technical How-to](https://aws.amazon.com/blogs/modernizing-with-aws/category/post-types/technical-how-to/), [Windows on AWS](https://aws.amazon.com/blogs/modernizing-with-aws/category/aws-on-windows/) | [Permalink](https://aws.amazon.com/blogs/modernizing-with-aws/operating-byol-windows-server-workloads-effectively-on-aws/)

Một trong những cách mà khách hàng chạy [khối lượng công việc Microsoft trên Amazon Web Services (AWS)](https://aws.amazon.com/microsoft/) có thể giảm chi phí là tận dụng mô hình Bring Your Own License (BYOL) cho các giấy phép đủ điều kiện mà họ sở hữu. Trong bài viết này, chúng tôi sẽ chia sẻ một số thực hành tốt nhất giúp bạn tối ưu hóa việc vận hành các khối lượng công việc Windows Server BYOL trên AWS.

## Giới thiệu

Một cách phổ biến để chạy khối lượng công việc Windows Server của bạn trên [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) là sử dụng tùy chọn “license included” (bao gồm giấy phép). Tùy chọn này có lợi vì bạn không cần phải mua hoặc quản lý giấy phép riêng, đồng thời tận hưởng tính linh hoạt trong việc tính phí theo giây. Tuy nhiên, nếu bạn đã sở hữu giấy phép đủ điều kiện sử dụng trên AWS, việc mang chúng lên sẽ giúp giảm chi phí vận hành đáng kể.

Chúng tôi sẽ xem xét một số kỹ thuật cụ thể để giúp bạn trong quá trình chạy Windows Server BYOL trên AWS, bao gồm:

- Chuẩn bị máy chủ on-premises để nhập vào AWS dưới dạng [Amazon Machine Image (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html).
- Chuyển đổi và quản lý giấy phép Windows giữa BYOL và license included khi cần thiết.
- Phát hiện lỗi cấu hình bằng [AWS Config](https://aws.amazon.com/config/) custom rule.
- Hiểu dữ liệu liên quan đến các phiên bản BYOL trong [AWS Cost and Usage Report](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/) (AWS CUR).

## BYOL cho Windows trên AWS

Để tận dụng BYOL, bạn cần xác nhận rằng giấy phép của mình đủ điều kiện. AWS cung cấp [hướng dẫn Microsoft Licensing trong AWS](https://aws.amazon.com/windows/resources/licensing/). Khi xác định tính đủ điều kiện, hãy lưu ý:

- Giấy phép phải là vĩnh viễn (perpetual) và được mua trước ngày 1 tháng 10 năm 2019, hoặc là một phần true-up trong Enterprise Agreement (EA) còn hiệu lực tại thời điểm đó.
- Phiên bản Windows phải là Windows Server 2019 hoặc cũ hơn.

Nếu đáp ứng điều kiện này, bạn có thể sử dụng giấy phép trên AWS. Dù có hay không có Software Assurance, Windows Server không đủ điều kiện cho [License Mobility](https://aws.amazon.com/windows/resources/licensemobility/). Điều này có nghĩa là các giấy phép phải được áp dụng trên phần cứng chuyên dụng dành riêng cho bạn. [Amazon EC2 Dedicated Hosts](https://aws.amazon.com/ec2/dedicated-hosts/) là giải pháp đáp ứng yêu cầu này — cung cấp cho bạn trải nghiệm quen thuộc khi chạy các phiên bản EC2 mà không cần quản lý phần cứng hoặc hypervisor. [AWS License Manager](https://aws.amazon.com/license-manager/) là dịch vụ giúp quản lý giấy phép trong AWS và là trọng tâm của chiến lược BYOL hiệu quả. 

Việc tính phí cho các phiên bản Amazon EC2 Windows của bạn được xác định dựa trên trường [usage operation](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/billing-info-fields.html#billing-info) mà phiên bản đó kế thừa từ AMI nguồn. Các phiên bản Windows chạy với giấy phép bao gồm sẵn (license included) — bất kể loại tenancy nào — sẽ sử dụng usage operation: **RunInstances:0002**. Tuy nhiên, khi bạn sử dụng giấy phép riêng (BYOL) cho một phiên bản Windows chạy trên Dedicated Hosts, thì cần sử dụng usage operation: **RunInstances:0800**. Bài viết [how to create an Amazon EC2 AMI usage and billing information report](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-create-an-amazon-ec2-ami-usage-and-billing-information-report/) sẽ giúp bạn tạo báo cáo về usage operation cho các phiên bản trong tổ chức của mình.

## Chuẩn bị images của bạn cho BYOL

Một yêu cầu để sử dụng giấy phép Windows riêng của bạn trên AWS là bạn phải cung cấp AMI riêng của bạn, thay vì sử dụng AMI được tạo bởi AWS. Khi mang image riêng của bạn lên AWS, bạn có nhiều lựa chọn để tạo chúng. Nếu đích đến cho server Windows của bạn là BYOL trên dedicated hosts, các công cụ sau sẽ giúp bạn đảm bảo AMI sẵn sàng để sử dụng.

[VM Import/Export](https://aws.amazon.com/ec2/vm-import/) (VMIE) là công cụ giúp bạn nhập các image máy ảo từ nền tảng ảo hóa hiện có của bạn thành Amazon Machine Images. Bước đầu tiên là xuất máy ảo của bạn sử dụng [định dạng](https://docs.aws.amazon.com/vm-import/latest/userguide/prerequisites.html#vmimport-image-formats) tiêu chuẩn như Open Virtual Appliance (OVA), ESX Virtual Machine Disk (VMDK), hoặc Virtual Hard Disk (VHD/VHDX). Sau đó, tải image lên một bucket [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (S3) để chuẩn bị cho quá trình chuyển đổi.

Để sử dụng VMIE, bạn dùng [các hướng dẫn](https://docs.aws.amazon.com/vm-import/latest/userguide/required-permissions.html#vmimport-role) này để tạo một [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) role tên “vmimport” mà dịch vụ sẽ sử dụng để thực hiện các thao tác thay bạn.

Khi sử dụng [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI) để [nhập một Windows image](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportImage.html) mà bạn dự định sử dụng cho BYOL trên dedicated hosts, bạn cần chỉ định license type để thiết lập usage operation đúng cho AMI kết quả. Ví dụ, để nhập một image OVA từ bucket S3, bạn có thể dùng lệnh:

```
aws ec2 import-image –usage-operation RunInstances:0800 –disk-containers Format=OVA,Url=s3://<<my-bucket>>/<<my-image-name>>.ova
```

Lệnh này sẽ khởi tạo một job nhập mà khi hoàn tất, sẽ tạo ra một AMI với mã usage đúng cho Windows BYOL.

[Migration Hub Orchestrator](https://docs.aws.amazon.com/migrationhub/latest/ug/gs-orchestrator.html) là một công cụ cho phép bạn tạo workflow để tự động hóa các tác vụ và đơn giản hóa quy trình di chuyển. Một trong các mẫu workflow mà Orchestrator cung cấp là “Import virtual machine images to AWS”. Sử dụng mẫu workflow này để nhập image cho Windows BYOL.

1. Mở console AWS và điều hướng đến [Migration Hub Console](https://console.aws.amazon.com/migrationhub/home).
2. Chọn **Workflows** trong menu **Orchestrate**.
3. Chọn **Create Workflow**. (Hình 1)

![A screenshot to create a workflow for the Migration hub console](/images/blog-3/Picture1v2.png)

<div style="text-align:center;">Hình 1: Tạo Workflow</div>

4. Chọn mẫu **Import virtual machine images to AWS** (Hình 2) và nhấn **Next**.

![A screenshot to select the template that import a virtual machine image to AWS](/images/blog-3/Picture2-18.png)

<div style="text-align:center;">Hình 2: Chọn mẫu import virtual machine</div>

5. Trên trang **Configure your workflow**, nhập **Tên** cho workflow và (tuỳ chọn) **Mô tả**.
6. Trong phần **Source environment configuration**, điền trường **Disk container**, đó là bucket S3 nơi bạn đã lưu image từ on-premises. Tên phải tuân theo yêu cầu của tài liệu [Migration Hub Orchestrator](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/import-vm-images.html#source-env-config-import-vm-images).

![A screenshot to populate the Disk container field](/images/blog-3/Picture3v2.png)

<div style="text-align:center;">Hình 3: Cấu hình môi trường nguồn</div>

7. Trong phần **Target environment configuration**, chọn hệ điều hành và giấy phép cho các máy ảo được tạo với AMI kết quả. Chọn **Windows Server BYOL without SQL Server**.

![A screenshot to select the target Operating system and application license](/images/blog-3/Picture4-14.png)

<div style="text-align:center;">Hình 4: Chọn mô hình giấy phép</div>

8. Sử dụng các trường còn lại để tuỳ chỉnh AMI của bạn theo yêu cầu — bao gồm boot mode, [AWS Key Management Service](https://aws.amazon.com/kms/) (KMS), thẻ và license specification (để phân tích trường hợp kinh doanh). Bạn cũng có thể để mặc định.
9. Trên trang **Review and submit**, chọn Run workflow để khởi chạy workflow.
    
Sau khi tải image lên và tạo workflow, nó đã sẵn sàng để chạy bằng cách chọn **Run workflow**

![A screenshot to run the  workflow for the Migration hub console](/images/blog-3/Picture5-15.png)

<div style="text-align:center;">Hình 5: Chạy Workflow</div>

## Quản lý chuyển đổi giấy phép hợp lý

Có các tình huống mà bạn cần chuyển đổi các instance Amazon EC2 từ mô hình giấy phép BYOL sang license included và ngược lại. Những tình huống này bao gồm (nhưng không giới hạn):

- Nâng cấp hệ điều hành của instance Amazon EC2 lên Windows Server 2022, phiên bản không đủ điều kiện BYOL, bất kể tenancy.
- Di chuyển một instance Amazon EC2 ra khỏi dedicated host để chạy nó trên shared tenancy EC2, điều này không đủ điều kiện BYOL.
- Di chuyển một instance Amazon EC2 đủ điều kiện BYOL từ shared tenancy sang dedicated host.

Khi bạn cần chuyển đổi mô hình giấy phép của một instance Amazon EC2, hãy sử dụng tính năng [License type conversion](https://docs.aws.amazon.com/license-manager/latest/userguide/license-conversion.html) trong AWS License Manager. License type conversion cho phép bạn thay đổi usage operation. Xem hướng dẫn về [các loại giấy phép đủ điều kiện cho Windows và SQL Server trong License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-types-windows.html).

## Phát hiện vấn đề cấu hình với AWS Config

[AWS Config](https://aws.amazon.com/config/) là một dịch vụ giúp bạn đánh giá, kiểm toán và đánh giá cấu hình của các tài nguyên AWS. Bằng cách tận dụng một quy tắc tùy chỉnh của AWS Config, bạn có thể phát hiện cấu hình giấy phép tiềm ẩn sai cho các instance chạy trên dedicated hosts, từ đó tránh chi phí giấy phép không cần thiết.

[Kho aws-config-rules](https://github.com/awslabs/aws-config-rules) chứa các quy tắc AWS Config tùy chỉnh để triển khai vào tài khoản AWS của bạn bằng [AWS Config Rules Development Kit (RDK)](https://github.com/awslabs/aws-config-rdk). Sử dụng quy tắc tùy chỉnh [EC2_INSTANCE_LICENSE_INCLUDED_DEDICATED_HOST](https://github.com/awslabs/aws-config-rules/tree/master/python/EC2_INSTANCE_LICENSE_INCLUDED_DEDICATED_HOST) để phát hiện các instance chạy Windows Server “license included” (usage operation RunInstances:0002) trên Dedicated Hosts.

Sử dụng [AWS CloudShell](https://aws.amazon.com/cloudshell/) để chạy RDK và thử triển khai các quy tắc AWS Config. Để cài đặt quy tắc tùy chỉnh, mở CloudShell trong [AWS Console](https://aws.amazon.com/console/) ở vùng mong muốn, và thực hiện các lệnh sau:

```Bash                                                   
pip install rdk  
rdk init  
git clone https://github.com/awslabs/aws-config-rules  
cd aws-config-rules/python  
rdk deploy EC2_INSTANCE_LICENSE_INCLUDED_DEDICATED_HOST
```

Khi quy tắc đã được triển khai, bạn có thể xem nó trong [AWS Config console](https://console.aws.amazon.com/config/home). Với các instance có giấy phép cấu hình sai, bạn hoặc di chuyển chúng sang Shared tenancy, hoặc làm theo [quy trình License Conversion](https://aws.amazon.com/vi/blogs/modernizing-with-aws/operating-byol-windows-server-workloads-effectively-on-aws/#manage-license) tương ứng.

![A screenshot for the custom AWS config rule](/images/blog-3/Picture6-10.png)

<div style="text-align:center;">Hình 6: Quy tắc tùy chỉnh AWS Config</div>

## Hiểu dữ liệu CUR cho các instance BYOL

[AWS Cost and Usage Reports (CUR)](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) chứa bộ dữ liệu chi phí và sử dụng toàn diện nhất. Sử dụng [Amazon Athena](https://aws.amazon.com/athena/) để [truy vấn dữ liệu CUR](https://docs.aws.amazon.com/cur/latest/userguide/cur-query-athena.html) của bạn. Truy vấn sau đây hiển thị các giấy phép mà các instance của bạn đang bị tính phí:

```SQL
select  
    line_item_resource_id,  
    line_item_operation,  
    line_item_line_item_type,  
    month,  
    year,  
    line_item_unblended_cost,  
    line_item_blended_cost,  
    line_item_usage_type,  
    line_item_usage_account_id,  
    line_item_line_item_description  
from  
    customer_all  
where  
    line_item_usage_account_id = '[ACCOUNT NUMBER]'  
    and line_item_line_item_type = 'Usage'  
    and line_item_operation like '%RunInstances:%'
```

Dựa trên kết quả truy vấn trên, trường line_item_operation cho bạn biết bạn đang bị [tính phí](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-info-fields.html#billing-info) cho gì.

![A screenshot for the output of the AWS CUR query](/images/blog-3/Image-from-iOS.jpg)

<div style="text-align:center;">Hình 7: Kết quả AWS CUR</div>

## Kết luận

Việc triển khai BYOL cho các khối lượng công việc Windows Server thành công trên AWS đòi hỏi chú ý cẩn trọng tới tính đủ điều kiện giấy phép, cấu hình và quản lý liên tục. Bằng cách hiểu các yêu cầu then chốt — từ ngày mua giấy phép và phiên bản Windows Server, đến mã usage operation đúng trên dedicated hosts — các tổ chức có thể hiệu quả giảm chi phí hạ tầng đám mây trong khi vẫn đảm bảo tuân thủ giấy phép. Thành công phụ thuộc vào ba yếu tố chính:

1. Đánh giá giấy phép đúng — xác định giấy phép đủ điều kiện dựa vào ngày mua và phiên bản Windows Server
2. Cấu hình chính xác — đảm bảo mã usage operation đúng để tránh tính phí trùng lặp trên dedicated hosts
3. Giám sát liên tục — duy trì đánh giá thường xuyên về sử dụng và chi phí

Bằng cách tuân theo các thực hành này, các tổ chức có thể tối ưu chi phí triển khai Windows Server của họ đồng thời đảm bảo tuân thủ giấy phép trên AWS.

Sẵn sàng bắt đầu tối ưu chi phí Windows Server trên AWS? Hãy yêu cầu một [AWS Optimization and Licensing Assessment](https://aws.amazon.com/optimization-and-licensing-assessment/) để bắt đầu đánh giá các cơ hội giấy phép và tiềm năng tiết kiệm chi phí.

---

AWS có nhiều dịch vụ và tính năng hơn bất kỳ nhà cung cấp đám mây nào khác, giúp bạn dễ dàng, nhanh chóng và tiết kiệm chi phí hơn trong việc di chuyển các ứng dụng hiện có lên đám mây và xây dựng hầu như bất cứ thứ gì bạn có thể tưởng tượng. Hãy cung cấp cho các ứng dụng Microsoft của bạn cơ sở hạ tầng cần thiết để thúc đẩy kết quả kinh doanh mong muốn. Truy cập các blog [.NET on AWS](https://aws.amazon.com/blogs/dotnet/) và [AWS Database](https://aws.amazon.com/blogs/database/) để biết thêm hướng dẫn và tùy chọn cho khối lượng công việc Microsoft của bạn. [Liên hệ với chúng tôi](https://pages.awscloud.com/MAP-windows-contact-us.html) để bắt đầu hành trình di chuyển và hiện đại hóa ngay hôm nay.

TAGS: [Amazon EC2](https://aws.amazon.com/blogs/modernizing-with-aws/tag/amazon-ec2/), [AWS License Manager](https://aws.amazon.com/blogs/modernizing-with-aws/tag/aws-license-manager/), [Cost Savings](https://aws.amazon.com/blogs/modernizing-with-aws/tag/cost-savings/), [Microsoft](https://aws.amazon.com/blogs/modernizing-with-aws/tag/microsoft/), [Windows On AWS](https://aws.amazon.com/blogs/modernizing-with-aws/tag/windows-on-aws/), [Windows Server](https://aws.amazon.com/blogs/modernizing-with-aws/tag/windows-server/)

<div style="display: flex; align-items: center;">
  <img src="/images/blog-3/aaalzand-400.jpg" alt="Ali Alzand" style="width:120px; border-radius:8px; margin-right:16px;">
  <p>
    <strong>Ali Alzand</strong><br>
    Ali là Kiến trúc sư Giải pháp Chuyên biệt về Microsoft (Microsoft Specialist Solutions Architect) tại Amazon Web Services (AWS), người giúp các khách hàng toàn cầu khai mở sức mạnh của đám mây thông qua việc di chuyển (migrating), hiện đại hóa (modernizing) và tối ưu hóa (optimizing) các khối lượng công việc Microsoft của họ.
    Anh chuyên về vận hành đám mây (cloud operations) — tận dụng các dịch vụ AWS như Systems Manager, Amazon EC2 Windows, và EC2 Image Builder để thúc đẩy quá trình chuyển đổi đám mây. Ngoài công việc, Ali thích khám phá thiên nhiên, nướng thịt barbecue cùng bạn bè vào cuối tuần, và thưởng thức những món ăn đa dạng, độc đáo mà ẩm thực mang lại.
  </p>
</div>

<div style="display: flex; align-items: center; margin-bottom: 24px;">
  <img src="/images/blog-3/Screenshot-2025-06-30-at-8.26.18-AM.png" alt="Jon Madison" style="width:120px; border-radius:8px; margin-right:16px;">
  <p>
    <strong>Jon Madison</strong><br>
    Jon Madison là Chuyên gia Tư vấn Triển khai Cấp cao (Principal Delivery Consultant) trong Nhóm Năng lượng (Energy Team) thuộc AWS Professional Services (ProServe). Anh có nền tảng về Hạ tầng đám mây (Cloud Infrastructure), Bảo mật (Security) và DevOps, đồng thời đam mê hỗ trợ khách hàng trong việc chuyển đổi sang điện toán đám mây và xây dựng các giải pháp, quy trình có khả năng mở rộng. Trong thời gian rảnh, Jon thích nấu ăn, chơi game, và dành thời gian bên gia đình cùng bạn bè.
  </p>
</div>

<div style="display: flex; align-items: center;">
  <img src="/images/blog-3/MikeGupta.jpg" alt="Mike Gupta" style="width:120px; border-radius:8px; margin-right:16px;">
  <p>
    <strong>Mike Gupta</strong><br>
    Mike Gupta là Quản lý Tài khoản Kỹ thuật Cấp cao (Senior Technical Account Manager) tại AWS, làm việc tại Thành phố New York. Trong vai trò của mình, anh cung cấp hướng dẫn kỹ thuật mang tính chiến lược, giúp khách hàng áp dụng các thực hành tốt nhất của AWS để lập kế hoạch và xây dựng các giải pháp. Anh tận tâm hỗ trợ khách hàng phát triển kiến trúc có khả năng mở rộng, khả năng phục hồi cao và tiết kiệm chi phí. Trong thời gian rảnh, Mike thích dành thời gian bên vợ và gia đình, khám phá lịch sử địa phương, và thử các nhà hàng mới.
  </p>
</div>


