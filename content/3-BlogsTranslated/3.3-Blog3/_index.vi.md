---
title: "Blog 3"
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---

# Giới thiệu just-in-time node access, một tính năng của AWS Systems Manager

Tác giả: Chetan Makvana, Anthony Verleysen, và Mark Brealey | Ngày đăng: 29 tháng 4 năm 2025 | Danh mục: [Announcements](https://aws.amazon.com/blogs/mt/category/post-types/announcements/), [AWS Systems Manager](https://aws.amazon.com/blogs/mt/category/management-tools/aws-systems-manager/), [Management Tools](https://aws.amazon.com/blogs/mt/category/management-tools/), [Security](https://aws.amazon.com/blogs/mt/category/security-identity-compliance/security/) | [Permalink](https://aws.amazon.com/blogs/mt/introducing-just-in-time-node-access-using-aws-systems-manager/) | Share

Hôm nay, chúng tôi vui mừng thông báo về việc phát hành rộng rãi [just-in-time node access](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access.html), một tính năng (capability) trong [AWS Systems Manager](https://aws.amazon.com/systems-manager/). Just-in-time node access cho phép truy cập một cách linh hoạt (dynamic) và có giới hạn thời gian (time-bound) đến các node [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/), hạ tầng tại chỗ (on-premises), và đa đám mây (multicloud) được quản lý bởi AWS Systems Manager. Tính năng này sử dụng một quy trình phê duyệt dựa trên chính sách (policy), cho phép bạn loại bỏ các quyền truy cập dài hạn trong khi vẫn duy trì hiệu quả vận hành và nâng cao bảo mật.

Các tổ chức mở rộng hoạt động lên đến hàng nghìn node đòi hỏi các quyền (permissions) chi tiết dựa trên danh tính (identity) để hỗ trợ các mục tiêu về kiểm toán (audit) và tuân thủ (compliance). Họ muốn loại bỏ hoàn toàn các thông tin xác thực dài hạn (long-term credentials). Việc sử dụng thông tin xác thực dài hạn để truy cập node tạo ra các lỗ hổng bảo mật, làm tăng nguy cơ bị truy cập trái phép và các sự cố xâm nhập tiềm tàng.

Trước đây, khách hàng phải đối mặt với sự đánh đổi khó khăn giữa bảo mật và hiệu quả vận hành. Thay vì xác định cẩn thận ai cần truy cập vào tài nguyên nào, các đội ngũ IT thường cấp các quyền (permissions) vượt mức cần thiết cho các nhóm người dùng lớn. Thực trạng này làm gia tăng nguy cơ xảy ra lỗi vận hành vô ý và tạo cơ hội cho các tác nhân xấu (bad actors), xuất phát từ nhu cầu tiện lợi trong vận hành. Họ phải lựa chọn giữa việc duy trì thông tin xác thực dài hạn (long-term credentials), làm tăng nguy cơ bị xâm phạm bảo mật, hoặc triển khai các biện pháp kiểm soát truy cập nghiêm ngặt làm chậm quá trình ứng phó sự cố. Các giải pháp tự xây dựng (custom-built) thì phức tạp để bảo trì và mở rộng; trong khi đó, các công cụ không phải của AWS sử dụng tác nhân (agent) lại yêu cầu danh tính (identity) và quyền (permissions) để truy cập vào các node.

## Tổng Quan

Just-in-time node access giúp bạn triển khai nguyên tắc truy cập đặc quyền tối thiểu (least-privilege access) trong khi vẫn đảm bảo các đội ngũ vận hành có thể phản ứng nhanh chóng với các sự cố. Nó hoạt động liền mạch trên toàn bộ [AWS Organization](https://aws.amazon.com/organizations/) của bạn, cho phép bạn thiết lập các cơ chế kiểm soát truy cập nhất quán dù bạn đang quản lý một tài khoản (account) hay nhiều tài khoản. Tính năng mới này cho phép quản trị viên (administrator) định nghĩa các quyền kiểm soát truy cập chính xác thông qua các chính sách phê duyệt (approval policies) chỉ định rõ ai có thể truy cập node nào và trong điều kiện nào. Các tổ chức có thể lựa chọn giữa quy trình phê duyệt thủ công (manual approval) với nhiều người phê duyệt (approver) hoặc các chính sách tự động phê duyệt (auto-approval policies) dựa trên điều kiện (condition-based), mang lại sự linh hoạt để đáp ứng các yêu cầu bảo mật của họ.

Ví dụ, các quản trị viên (administrator) có thể thiết lập chính sách tự động phê duyệt (auto-approval policy) để nhanh chóng cấp quyền truy cập cho các kỹ sư trực (on-call engineer) trong các sự cố, chỉ cấp quyền cho những người vận hành (operator) thuộc một nhóm (group) on-call trong [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/). Thông qua just-in-time node access, những người vận hành (operator) có thể yêu cầu quyền truy cập vào các node khi họ cần. Dựa trên các chính sách phê duyệt (approval policy) được cấu hình sẵn, họ sẽ nhận được quyền truy cập tạm thời và sẽ tự động hết hạn sau một khoảng thời gian xác định. Sau khi được phê duyệt, họ có thể truy cập trực tiếp vào các node này thông qua shell trên trình duyệt bằng một cú nhấp chuột (one-click browser-based shell), [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/) hoặc Remote Desktop Protocol (RDP) được Systems Manager hỗ trợ, mà không cần phải mở cổng inbound (inbound port) hay quản lý khóa SSH (SSH key).

Để đơn giản hóa quy trình phê duyệt, just-in-time node access tích hợp với các công cụ như Slack và Microsoft Teams thông qua [Amazon Q Developer](https://aws.amazon.com/q/developer/), và email để thông báo cho những người phê duyệt (approver) về các yêu cầu đang chờ xử lý. Systems Manager cũng phát ra các sự kiện (event) tới [Amazon EventBridge](https://aws.amazon.com/eventbridge/) để cập nhật trạng thái của các yêu cầu truy cập phiên (session) just-in-time. Các sự kiện này có thể được chuyển đến [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/) để gửi thông báo hoặc tích hợp với các hệ thống nội bộ của bạn, cho phép các nhóm của bạn theo dõi và phản hồi các yêu cầu truy cập thông qua các luồng công việc (workflow) hiện có. Điều này cho phép bạn giám sát các yêu cầu truy cập và duy trì dấu vết kiểm toán (audit trail) trên toàn tổ chức. Hơn nữa, just-in-time node access có thể cung cấp khả năng quan sát sâu hơn vào các hoạt động của người vận hành (operator) bằng cách ghi lại (logging) các lệnh được chạy trong các phiên (session) và ghi lại hành động của họ trong các phiên RDP (RDP session).

Systems Manager cung cấp một bản dùng thử miễn phí (free trial) cho just-in-time node access trên mỗi tài khoản (account) mỗi Khu vực (Region), cho phép bạn khám phá và đánh giá đầy đủ tính năng này cho tổ chức của mình. Giai đoạn dùng thử này bao gồm phần còn lại của kỳ thanh toán (billing period) mà bạn bật tính năng, cộng với toàn bộ kỳ thanh toán (billing period) tiếp theo. Trong thời gian dùng thử này, bạn sẽ có quyền truy cập vào tất cả các chức năng, cho phép bạn kiểm tra các cấu hình và chính sách truy cập (access policies) mà không phải trả thêm bất kỳ khoản phí nào. Sau khi kết thúc dùng thử, just-in-time node access sẽ trở thành một dịch vụ trả phí, với chi phí dựa trên mô hình sử dụng của bạn. Để biết thông tin chi tiết về giá cả và phân tích chi phí, vui lòng tham khảo trang [AWS Systems Manager Pricing](https://aws.amazon.com/systems-manager/pricing/).

## Sử dụng Just-in-Time Node Access

Khi bạn triển khai just-in-time node access, bạn sẽ làm việc với ba vai trò riêng biệt: Quản trị viên (Administrator), Người vận hành (Operator), và Người phê duyệt (Approver). Quản trị viên thiết lập và duy trì các chính sách phê duyệt (approval policy). Người vận hành khởi tạo các yêu cầu truy cập đến các node cụ thể. Và người phê duyệt xem xét và cấp phép cho các yêu cầu truy cập.

Hãy cùng xem qua cách bạn có thể thiết lập và sử dụng tính năng này, thông qua một kịch bản nơi một kỹ sư trực (on-call engineer) của bạn cần truy cập vào một hệ thống sản phẩm (production), cụ thể là một phiên bản (instance) có tên là 'r2d2-app-01' từ nhóm các instance bên dưới như trong hình 1.

![Amazon EC2 console showing list of EC2 instances](/images/blog-3/ec2-instances.png)

*Hình 1: Giao diện console của Amazon EC2 hiển thị danh sách các EC2 instance*

Chúng ta sẽ khám phá cách một kỹ sư trực (on-call engineer) (vai trò Người vận hành – Operator) có thể yêu cầu quyền truy cập vào hệ thống sản phẩm (production), với trưởng nhóm DevOps (DevOps lead) (vai trò Người phê duyệt – Approver) quản lý việc phê duyệt, tất cả đều nằm trong khuôn khổ chính sách phê duyệt (approval policy) được định nghĩa bởi Quản trị viên (Administrator).

## Thiết lập Just-in-time node access với vai trò Quản trị viên (Administrator)

### Bước 1 – Bật Just-in-Time Node Access

Trong hướng dẫn này, chúng ta sẽ bật just-in-time node access cho AWS Organization. Để bắt đầu, trước tiên bạn phải thiết lập [Systems Manager unified console](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-organizations.html). Sau khi unified console được thiết lập, bạn có thể bật just-in-time node access trong Systems Manager.

Sau đó, bạn có thể chọn các Đơn vị Tổ chức (Organization Units – OUs) và Khu vực (Region) AWS nào để triển khai. Điều này cho phép bạn kiểm soát chính xác nơi giải pháp được thực thi, dù là trên toàn bộ tổ chức của bạn hay trong các khu vực cụ thể như trong hình 2.

![AWS System Manager console to enable just-in-time node access for Organizational Units and Regions](/images/blog-3/onboarding.png)

*Hình 2: Bật just-in-time node access*

### Bước 2 – Tạo approval policy

Sau khi bật tính năng, bước quan trọng tiếp theo là tạo các chính sách phê duyệt (approval policies). Các chính sách phê duyệt (approval policy) quyết định cách người dùng có được quyền truy cập vào các node. Các chính sách này có ba loại: tự động phê duyệt (auto-approval), phê duyệt thủ công (manual approval), và từ chối truy cập (deny-access). Chính sách tự động phê duyệt (Auto-approval policy) định nghĩa node nào người dùng có thể kết nối tự động. Chính sách phê duyệt thủ công (Manual approval policy) định nghĩa số lượng và các cấp phê duyệt thủ công phải được cung cấp để truy cập vào các node bạn chỉ định. Chính sách từ chối truy cập (Deny-access policy) ngăn chặn một cách tường minh việc tự động phê duyệt các yêu cầu truy cập đến các node bạn chỉ định.

Trong ví dụ của chúng ta, chúng ta sẽ tập trung vào việc tạo một chính sách phê duyệt thủ công (manual approval policy) cho các node được gắn thẻ (tag) Workload:Application01, bao gồm cả node 'r2d2-app-01' của chúng ta.

Để tạo policy, hãy điều hướng đến [AWS Systems Manager console](https://console.aws.amazon.com/systems-manager/home), chọn just-in-time node access trong thanh điều hướng (navigation pane), chọn tab Approval policies, và chọn Create manual policy. Việc cấu hình policy đòi hỏi một số thành phần chính.

Đầu tiên, trong mục Approval policy details, hãy cung cấp tên và mô tả cho chính sách phê duyệt (approval policy), cùng với việc thiết lập thời lượng truy cập tối đa (maximum access duration) như trong hình 3. Thời hạn này quyết định quyền truy cập đã được phê duyệt sẽ có hiệu lực trong bao lâu trước khi tự động hết hạn.

![Create manual approval policy page to enter Approval policy details](/images/blog-3/approval-policy-details-section.png)

*Hình 3: Trang manual approval policy*

Trong mục Targets, sử dụng các cặp khóa-giá trị (key-value) của thẻ (tag) để định nghĩa policy này sẽ áp dụng cho những node nào. Trong ví dụ này, chúng ta sẽ nhắm mục tiêu các node được gắn thẻ (tag) Workload:Application01, bao gồm cả node 'r2d2-app-01' của chúng ta. Cách tiếp cận này đảm bảo policy được áp dụng cho tất cả các node liên quan đến Application01 như trong hình 4.

![Specifying targets for a manual approval policy](/images/blog-3/manual-policy-targets.png)

*Hình 4: Mục tiêu của manual approval policy*

Trong mục Access request approvers, bạn sẽ chỉ định các cá nhân hoặc nhóm được ủy quyền để phê duyệt các yêu cầu truy cập. Trong kịch bản của chúng ta, chúng ta sẽ gán vai trò DevOps lead làm người phê duyệt. Người phê duyệt yêu cầu truy cập có thể là người dùng (user) và nhóm (group) của IAM Identity Center hoặc người dùng (user), nhóm (group), và vai trò (role) của IAM như trong hình 5.

![Create manual approval policy page to enter Access request approvals](/images/blog-3/access-requests-approvals.png)

*Hình 5: Phê duyệt yêu cầu truy cập*

Bạn cũng có thể định nghĩa các quy tắc truy cập tự động bằng [Cedar policy language](https://www.cedarpolicy.com/en), loại bỏ nhu cầu phê duyệt thủ công trong các kịch bản đáng tin cậy. Hãy xem các chính sách tự động phê duyệt (auto-approval policy) như là một bộ quy tắc truy cập đã được phê duyệt trước của tổ chức bạn. Các chính sách này chỉ định node nào người dùng có thể truy cập tự động, dựa trên các điều kiện và mức độ tin cậy được định sẵn. Để biết thêm thông tin, hãy xem [Create an auto-approval policy for just-in-time node access](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-create-auto-approval-policies.html) và [Statement structure and built-in operators for auto-approval and deny-access policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/auto-approval-deny-access-policy-statement-structure.html).

Ví dụ, bạn có thể tạo một chính sách tự động phê duyệt (auto-approval policy) mà tự động cho phép các thành viên của nhóm (group) "DevOpsTeam" truy cập vào các node được gắn thẻ (tag) Environment: Development bằng cách sử dụng Cedar policy sau:

```cedar
// Policy to permit access to Development nodes for members of the DevOpsTeam IDC group
permit (
    principal in AWS::IdentityStore::Group::"911b8590-7041-70fa-d20b-12345EXAMPLE",
    action == AWS::SSM::Action::"getTokenForInstanceAccess", 
    resource)
  when {
    resource.hasTag("Environment") && 
    resource.getTag("Environment") == "Development"
  };
```

## Yêu cầu quyền truy cập với vai trò Operator

Khi bạn cần truy cập một node được bảo vệ (protected node) với vai trò là người vận hành (operator), bạn sẽ thấy một quy trình yêu cầu được tinh gọn. Thay vì được truy cập ngay lập tức, bạn sẽ được yêu cầu gửi một yêu cầu truy cập (access request) khi cố gắng kết nối thông qua Session Manager. Bạn sẽ cần cung cấp lý do (justification) cho việc truy cập như trong hình 6.

![Operator raising a request to access the node](/images/blog-3/access-request-1.gif)

*Hình 6: Operator tạo một yêu cầu để truy cập node*

Sau khi gửi yêu cầu, bạn có thể theo dõi trạng thái của nó thông qua tab Access Requests như trong hình 7. Bạn sẽ có thể theo dõi yêu cầu của mình qua suốt quy trình phê duyệt và biết chính xác khi nào bạn có quyền truy cập. Bạn sẽ nhận được thông báo qua kênh liên lạc ưa thích của mình, có thể là email, Slack, Microsoft Teams hoặc một nền tảng tích hợp (integrated platform) khác. Để biết thêm thông tin, hãy xem [Configure notifications for just-in-time access requests](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-notifications.html).

![Just-in-time node access page showing list of access requests raised by operator](/images/blog-3/requests-for-me-page.png)

*Hình 7: Trang danh sách các yêu cầu truy cập*

## Quản lý các phê duyệt

Với vai trò là người phê duyệt (approver), bạn sẽ nhận được thông báo về các yêu cầu truy cập đang chờ xử lý thông qua kênh thông báo (notification channel) đã cấu hình của mình. Bạn có thể phê duyệt các yêu cầu một cách có lập trình bằng cách sử dụng [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI), hoặc [SDK](https://aws.amazon.com/developer/tools/) ưa thích của bạn. Hoặc bạn có thể xem xét các yêu cầu này trong Systems Manager console dưới tab Requests for me như trong hình 8.

![Just-in-time node access page showing list of access requests pending for approval by the approver](/images/blog-3/requests-approval.png)

*Hình 8: Danh sách các yêu cầu truy cập đang chờ phê duyệt*

Sau khi xem xét yêu cầu, bạn có thể phê duyệt hoặc từ chối yêu cầu và tùy chọn thêm một bình luận liên quan đến quyết định của mình.

## Hoàn thành chu trình truy cập

Một khi yêu cầu được phê duyệt, với vai trò là người vận hành (operator), bạn sẽ nhận được thông báo rằng quyền truy cập của bạn đã được cấp. Sau đó, bạn có thể kết nối với node bằng AWS Management console hoặc AWS CLI trong khoảng thời gian được quy định trong chính sách phê duyệt (approval policy) như trong hình 9.

![Operator accessing the managed node](/images/blog-3/access-approval.gif)

*Hình 9: Operator truy cập vào managed node*

## Kết luận

Trong blog này, chúng tôi đã giới thiệu [just-in-time node access](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access.html), một tính năng mới trong AWS Systems Manager. Just-in-time node access giải quyết thách thức trong việc cân bằng giữa hiệu quả vận hành và các yêu cầu bảo mật bằng cách loại bỏ các đặc quyền thường trực (standing privileges), đồng thời đảm bảo quyền truy cập nhanh chóng đến các node Amazon EC2, tại chỗ (on-premises), và đa đám mây (multicloud). Thông qua phương pháp tiếp cận linh hoạt dựa trên chính sách (policy), và hỗ trợ cả phê duyệt thủ công (manual approval) lẫn tự động (automatic approval), giờ đây bạn có thể triển khai nguyên tắc không có đặc quyền thường trực (zero standing privileges) mà không ảnh hưởng đến khả năng vận hành.

Systems Manager cung cấp một bản dùng thử miễn phí (free trial) cho just-in-time node access, cho phép bạn khám phá và đánh giá đầy đủ tính năng này cho tổ chức của mình.

Để tìm hiểu thêm, hãy xem [Just-in-time node access using Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access.html) để biết thêm chi tiết.

Hãy xem [bản demo tương tác (interactive demo)](https://aws-cloudops.storylane.io/share/qazsu1mgqiho) này để có một chuyến tham quan trực quan đầy đủ về trải nghiệm just-in-time node access.

TAGS: [AWS Systems Manager](https://aws.amazon.com/blogs/mt/tag/aws-system-manager/), [Security](https://aws.amazon.com/blogs/mt/tag/security/)

## Về tác giả:

**Chetan Makvana**

Chetan Makvana là Kiến trúc sư Giải pháp Doanh nghiệp (Enterprise Solutions Architect) tại Amazon Web Services. Anh hỗ trợ các khách hàng doanh nghiệp thiết kế những giải pháp cấp doanh nghiệp (enterprise grade) có khả năng mở rộng (scalable), ổn định (resilient), bảo mật (secured) và hiệu quả về chi phí (cost effective) bằng cách sử dụng các dịch vụ của AWS. Anh là người đam mê công nghệ và là một "builder" (người kiến tạo), với các lĩnh vực quan tâm chính bao gồm AI tạo sinh (generative AI), serverless, hiện đại hóa ứng dụng (app modernization) và DevOps. Ngoài công việc, anh thích "cày phim" (binge-watching), du lịch và âm nhạc.

**Anthony Verleysen**

Anthony Verleysen là Giám đốc Sản phẩm Kỹ thuật Cấp cao (Senior Product Manager – Technical) thuộc nhóm AWS Systems Manager. Anh chịu trách nhiệm quản lý sản phẩm cho Patch Manager và Distributor. Ngoài công việc, Anthony là một người đam mê chơi bóng đá và tennis.

**Mark Brealey**

Mark Brealey là Kiến trúc sư Giải pháp Di chuyển Cấp cao (Senior Migration Solutions Architect). Anh hỗ trợ các đối tác xây dựng các kiến trúc đám mây (cloud architectures) vững chắc (robust), bảo mật và hiệu quả. Anh chuyên thiết kế các giải pháp có khả năng mở rộng (scalable) nhằm giúp các tổ chức tối ưu hóa (maximize) cơ sở hạ tầng AWS của họ, đồng thời đảm bảo vận hành xuất sắc (operational excellence).
