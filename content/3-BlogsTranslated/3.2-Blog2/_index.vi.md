---
title: "Blog 2"
weight: 1
chapter: false
pre: " <b> 3.2. </b> "
---

# Thiết lập cảnh báo tự động cho các AWS Savings Plans mới mua

Tác giả: Syed Muhammad Tawha và Dan Johns | ngày 26 tháng 6, 2025 | trong [Amazon Simple Notification Service (SNS)](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/messaging/amazon-simple-notification-service-sns/), [AWS Cloud Financial Management](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/aws-cloud-financial-management/), [AWS CloudFormation](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/management-tools/aws-cloudformation/), [Cloud Cost Optimization](https://aws.amazon.com/blogs/aws-cloud-financial-management/category/business-intelligence/cloud-cost-optimization/) | [Permalink](https://aws.amazon.com/blogs/aws-cloud-financial-management/how-to-set-up-automated-alerts-for-newly-purchased-aws-savings-plans/)

Khi các tổ chức phát triển, các nhóm FinOps cần có cái nhìn tổng quan toàn diện về cam kết [AWS Savings Plans](https://aws.amazon.com/savingsplans/) để tối đa hóa hiệu quả sử dụng. Giải pháp này liên quan đến việc triển khai hệ thống giám sát và cảnh báo tự động nhằm xác định các Savings Plans chưa được sử dụng hiệu quả trong thời gian còn có thể hoàn trả.

Khi bạn mua một Savings Plan, bạn cam kết trong vòng một hoặc ba năm. Các Savings Plans có cam kết hàng giờ từ 100 USD trở xuống có thể được hoàn trả nếu được mua trong vòng 7 ngày gần nhất và trong cùng tháng dương lịch, miễn là bạn chưa vượt quá giới hạn hoàn trả. Khi tháng dương lịch kết thúc (theo giờ UTC), các Savings Plans đã mua sẽ không thể hoàn trả.

Trong bài viết này, chúng tôi cung cấp mẫu [AWS CloudFormation](https://aws.amazon.com/cloudformation/) để tạo [AWS Step Functions](https://aws.amazon.com/step-functions/) state machine, [Amazon Simple Notification Service](https://aws.amazon.com/sns/) (SNS) topic, [Amazon EventBridge](https://aws.amazon.com/eventbridge/) scheduler, và các vai trò [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) cần thiết để tự động giám sát các Savings Plans mới mua và làm nổi bật những kế hoạch đang bị sử dụng dưới mức.

## Tổng quan về giải pháp

Giải pháp này tuân thủ các thực tiễn bảo mật tốt nhất của AWS bằng cách triển khai phân tách trên hai tài khoản khác nhau. Một CloudFormation stack sẽ được tạo trong [Management Account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#management-account) để thiết lập các vai trò IAM cần thiết nhằm truy xuất dữ liệu sử dụng Savings Plans. Một CloudFormation stack khác sẽ được triển khai trong [Member Account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#member-account) thuộc [AWS Organization](https://aws.amazon.com/organizations/) của bạn.

Stack CloudFormation trong member account tạo một state machine có khả năng assume role trong management account và phân tích tất cả các Savings Plans trong management account, bao gồm cả những kế hoạch được mua trên toàn tổ chức. Quy trình làm việc này lọc các Savings Plans đang hoạt động, dựa trên ngày mua, tập trung vào các kế hoạch được mua trong vòng 7 ngày gần nhất và trong tháng dương lịch hiện tại. Sau đó, nó đánh giá tỷ lệ sử dụng và xác định các kế hoạch dưới ngưỡng xác định.

State machine này sẽ chạy theo tần suất bạn chỉ định và sử dụng Amazon SNS để gửi cảnh báo qua email đến các địa chỉ bạn cung cấp trong quá trình tạo stack. Các cảnh báo này bao gồm thông tin chi tiết về các Savings Plans có mức sử dụng thấp và hướng dẫn quy trình hoàn trả.

![Sơ đồ kiến trúc AWS](/images/blog-2/AWS-architecture-diagram.png)

<div style="text-align:center;">Hình 1: Sơ đồ kiến trúc AWS – Member account giả định vai trò để đọc dữ liệu Savings Plans từ management account và kích hoạt Step Function, sau đó gửi cảnh báo qua email thông qua Amazon SNS.</div>

## Hướng dẫn triển khai giải pháp

### Yêu cầu tiên quyết

- Một tài khoản AWS
- Quyền IAM để tạo CloudFormation Stack và triển khai IAM role trong Management Account
- Quyền IAM để tạo CloudFormation Stack và triển khai Step Functions, IAM roles, SNS, và EventBridge scheduler trong Member Account bạn chọn
  
### Triển khai giải pháp

Trong phần này, bạn sẽ triển khai các tài nguyên của giải pháp trong các account của bạn.

#### Phần 1 – Triển khai trong Member Account

Trong phần này, bạn sẽ triển khai các tài nguyên của giải pháp trong member account đã chọn.

1. Đăng nhập vào AWS Management Console của member account nơi bạn muốn chạy giải pháp này.
2. Triển khai CloudFormation Stack.[![Launch Stack](/images/blog-2/SC-2_button.jpg)](https://us-west-2.console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://aws-well-architected-labs.s3.us-west-2.amazonaws.com/Cost/Blogs/sample-aws-new-savings-plan-utilization-alert/sample-aws-new-savings-plan-utilization-alert_member.yaml&stackName=new-savings-plan-utilization-alert-member)
3. Đặt Stack Name là new-sp-utilization-alert-member.
4. Trong tham số AlertEmails, nhập danh sách địa chỉ email (ngăn cách bằng dấu phẩy) để nhận thông báo về các Savings Plans sử dụng thấp.
5. Trong tham số ManagementAccountId, nhập 12 chữ số ID tài khoản AWS quản lý của bạn.
6. Trong tham số ScheduleExpression, chỉ định tần suất thực thi của Step Functions state machine bằng định dạng cron (mặc định là hàng ngày lúc 9 AM UTC).
7. Trong tham số UtilizationThreshold, chỉ định tỷ lệ sử dụng tối thiểu cho Savings Plans của bạn. Bạn sẽ nhận cảnh báo khi tỷ lệ sử dụng thấp hơn ngưỡng này.
8. Nhấp Next, chọn hộp xác nhận, và tạo stack.
9. Chờ cho đến khi stack hiển thị trạng thái CREATE-COMPLETE.
10. Bạn sẽ nhận được email để xác nhận đăng ký SNS topic được tạo bởi stack này — hãy xác nhận để bắt đầu nhận thông báo.
11. Truy cập tab Outputs của stack vừa tạo và ghi chú lại giá trị của ExecutionRoleArn và StateMachineArn — bạn sẽ cần chúng ở phần tiếp theo.
    
#### Phần 2 – Triển khai trong Management Account

1. Đăng nhập vào AWS Management Console của management account (phải là tài khoản được nhập trong tham số ManagementAccountId ở phần 1).
2. Triển khai CloudFormation stack.[![Launch Stack](/images/blog-2/SC-2_button.jpg)](https://us-west-2.console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://aws-well-architected-labs.s3.us-west-2.amazonaws.com/Cost/Blogs/sample-aws-new-savings-plan-utilization-alert/sample-aws-new-savings-plan-utilization-alert_management.yaml&stackName=aws-new-savings-plan-utilization-alert-management)
3. Đặt Stack Name là new-sp-utilization-alert-management.
4. Trong tham số ExecutionRoleArn, nhập giá trị sao chép từ phần Outputs của stack đã triển khai trong member account.
5. Trong tham số StateMachineArn, nhập giá trị tương ứng từ phần Outputs.
6. Nhấp Next, chọn hộp xác nhận, và tạo stack.
7. Chờ cho đến khi stack hiển thị trạng thái **CREATE-COMPLETE**.

#### Kiểm thử giải pháp

Khi Step Functions state machine và các tài nguyên liên quan đã được triển khai trong member account, bạn có thể kiểm thử:

- Đăng nhập lại vào AWS Management Console của member account.
- Truy cập tab Resources trong CloudFormation stack và tìm SavingsPlansAlerts Step Functions state machine. Nhấp vào liên kết màu xanh để mở Step Functions Console.
- Nhấn nút Start execution ở bên phải để bắt đầu chạy.
- Theo dõi chi tiết quá trình thực thi trong phần Events để xem tiến trình. Nếu có bất kỳ Savings Plans nào được mua trong 7 ngày gần nhất và trong tháng dương lịch hiện tại, bạn sẽ nhận email thông báo.
- Một lần chạy thành công được thể hiện bằng hộp màu xanh lá cây trong Graph view. Nếu có Savings Plans dưới ngưỡng sử dụng, bạn sẽ nhận được email cảnh báo.

## Dọn dẹp

Tất cả tài nguyên được triển khai có thể được xóa bằng cách xóa các CloudFormation stacks, thông qua AWS Management Console hoặc AWS CLI.

Xóa stack trong management account (CLI):

```
aws cloudformation delete-stack –stack-name new-sp-utilization-alert_management
```

Xóa stack trong member account (CLI):

```
aws cloudformation delete-stack –stack-name new-sp-utilization-alert_member
```

## Hiểu và xử lý cảnh báo

Khi bạn nhận được cảnh báo về Savings Plans sử dụng thấp, hãy xem xét chi tiết mức sử dụng được cung cấp trong email. Phân tích các chỉ số sử dụng so với cam kết ban đầu, và xác định xem mức sử dụng thấp có dự kiến hay do các yếu tố khác như di chuyển khối lượng công việc, thay đổi kiến trúc, hoặc ước lượng sai nhu cầu dung lượng. Nếu mức sử dụng vẫn liên tục dưới ngưỡng, Savings Plan được mua trong vòng 7 ngày, trong tháng hiện tại, và có cam kết hàng giờ ≤ 100 USD, hãy xem xét hoàn trả kế hoạch. Ghi lại lý do hoàn trả để tham khảo và lập kế hoạch trong tương lai.

## Kết luận

Trong bài viết này, chúng tôi đã trình bày cách sử dụng Savings Plan API và Cost Explorer API để xác định các Savings Plans có mức sử dụng thấp trong tổ chức của bạn. Chúng tôi cũng minh họa cách sử dụng Step Functions State Machine để lọc các Savings Plans được mua trong 7 ngày gần nhất và trong tháng hiện tại. Khung thời gian này rất quan trọng vì bạn có thể hoàn trả Savings Plans trong cửa sổ hoàn trả nếu chúng được mua nhầm hoặc không được sử dụng hiệu quả. Để biết hướng dẫn chi tiết về quy trình hoàn trả, vui lòng tham khảo tài liệu [Returning a Purchased Savings Plan](https://docs.aws.amazon.com/savingsplans/latest/userguide/return-sp.html)

<div style="display: flex; align-items: center;">
  <img src="/images/blog-2/syed.png" alt="Syed Muhammad Tawha" style="width:120px; border-radius:8px; margin-right:16px;">
  <p>
    <strong>Syed Muhammad Tawha</strong><br>
    Syed Muhammad Tawha là Quản lý Tài khoản Kỹ thuật Cấp cao (Principal Technical Account Manager) tại AWS, làm việc tại Dublin, Ireland. Tawha chuyên về Lưu trữ (Storage), Khả năng phục hồi (Resilience) và Tối ưu hóa chi phí đám mây (Cloud Cost Optimization). Anh đam mê việc hỗ trợ các khách hàng của AWS. Ngoài ra, Tawha cũng rất thích dành thời gian bên bạn bè và gia đình.
  </p>
</div>

<div style="display: flex; align-items: center;">
  <img src="/images/blog-2/Dan-Johns.jpg" alt="Dan Johns" style="width:120px; border-radius:8px; margin-right:16px;">
  <p>
    <strong>Dan Johns</strong><br>
    Dan Johns là Kỹ sư Kiến trúc Giải pháp Cấp cao (Senior Solutions Architect Engineer), hỗ trợ khách hàng của mình trong việc xây dựng trên AWS và đáp ứng các yêu cầu kinh doanh. Ngoài công việc chuyên môn, anh thích đọc sách, dành thời gian bên gia đình, và tự động hóa các công việc trong ngôi nhà của mình.
  </p>
</div>

