---
title: "Blog 2"
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---


# Tối ưu hóa hiệu năng cold start của AWS Lambda sử dụng priming với SnapStart

Tác giả: Shan Kandaswamy và Gustavo Martim | Ngày đăng: 29 tháng 04 năm 2025 | Danh mục: [Advanced (300)](https://aws.amazon.com/blogs/compute/category/learning-levels/advanced-300/), [AWS Lambda](https://aws.amazon.com/blogs/compute/category/compute/aws-lambda/), [Best Practices](https://aws.amazon.com/blogs/compute/category/post-types/best-practices/), [Serverless](https://aws.amazon.com/blogs/compute/category/serverless/), [Technical How-to](https://aws.amazon.com/blogs/compute/category/post-types/technical-how-to/) | [Permalink](https://aws.amazon.com/blogs/compute/optimizing-cold-start-performance-of-aws-lambda-using-advanced-priming-strategies-with-snapstart/) | Share

Được giới thiệu tại re:Invent 2022, SnapStart là một phương pháp tối ưu hóa hiệu năng giúp việc xây dựng các ứng dụng có khả năng phản hồi cao và mở rộng tốt bằng AWS Lambda trở nên dễ dàng hơn. Yếu tố đóng góp lớn nhất vào độ trễ khởi động (thường được gọi là cold-start time) là thời gian dành cho việc khởi tạo một hàm. Quá trình này bao gồm việc tải mã nguồn của hàm và khởi tạo các dependency. Đối với các workload nhạy cảm về độ trễ như API và các ứng dụng xử lý dữ liệu thời gian thực, độ trễ khởi động cao có thể dẫn đến trải nghiệm người dùng cuối không tối ưu.

Lambda SnapStart có thể giảm thời gian khởi động từ vài giây xuống mức dưới một giây, với thay đổi code ở mức tối thiểu hoặc không cần thay đổi. Bài viết này thảo luận về 'Priming', một kỹ thuật để tối ưu hóa hơn nữa thời gian khởi động cho các hàm AWS Lambda được xây dựng bằng Java và Spring Boot.

Các ứng dụng Spring Boot thường gặp phải độ trễ cold start cao trong quá trình khởi tạo JVM và framework, nơi một lượng thời gian đáng kể được dành cho việc tải các class và thực hiện biên dịch Just-In-Time (JIT) mã Java bytecode. Bài đăng blog này sử dụng một ứng dụng Spring Boot làm ví dụ để truy xuất 10 bản ghi từ bảng UnicornEmployee trong cơ sở dữ liệu Amazon RDS for PostgreSQL, trong đó mỗi bản ghi nhân viên bao gồm tên, địa điểm và ngày tuyển dụng.

Ứng dụng mẫu sử dụng Amazon API Gateway để kích hoạt một hàm AWS Lambda kết nối đến cơ sở dữ liệu thông qua RDS Proxy để trả về dữ liệu nhân viên. Mặc dù ứng dụng mẫu này sử dụng dữ liệu nhân viên giả để minh họa, các mẫu và kỹ thuật tối ưu hóa được thảo luận trong bài viết này có thể áp dụng cho các kịch bản thực tế với các mẫu truy cập dữ liệu tương tự.

Mã nguồn mẫu cho việc triển khai này có thể được tìm thấy trong kho GitHub của chúng tôi tại [lambda-priming-crac-java-cdk](https://github.com/aws-samples/lambda-priming-crac-java-cdk).

## Cách SnapStart hoạt động

Bài viết này giả định rằng người đọc đã quen thuộc với SnapStart và cung cấp một nền tảng ngắn gọn. Để biết thêm chi tiết, hãy tham khảo [SnapStart documentation](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html).

Tóm tắt nhanh, pha INIT của một hàm Lambda bao gồm việc tải xuống mã nguồn của hàm, khởi động runtime và bất kỳ dependency bên ngoài nào, và chạy mã khởi tạo của hàm. Đối với các hàm không sử dụng SnapStart, pha này xảy ra mỗi khi ứng dụng của bạn mở rộng quy mô để tạo ra một execution environment mới. Khi SnapStart được kích hoạt, pha INIT xảy ra khi bạn publish một phiên bản của hàm.

Hình ảnh sau đây cho thấy sự so sánh vòng đời của một request Lambda khi có và không có SnapStart.

![Lambda Request Lifecycle Comparison](/images/blog-2/ComputeBlog-2165img1.png)

**Hình 1 – So sánh vòng đời của một request Lambda khi có và không có SnapStart**

Vào cuối pha INIT, Lambda thực thi runtime hooks before-checkpoint của bạn. Lambda sau đó tạo snapshot trạng thái bộ nhớ và đĩa của execution environment đã được khởi tạo, lưu trữ snapshot đã được mã hóa và cache nó để truy cập với độ trễ thấp. Khi hàm được gọi sau đó, các execution environment mới sẽ được khôi phục từ snapshot đã được cache (trong pha RESTORE), giúp tăng tốc độ khởi động của hàm.

![Execution Environments Resume from Snapshot](/images/blog-2/ComputeBlog-2165img2.png)

**Hình 2 – Các execution environment mới được khôi phục từ snapshot đã được cache**

Bạn có thể xác thực sự tăng tốc này bằng cách so sánh thời gian RESTORE với thời gian INIT được ghi lại trước khi có SnapStart trong Log Amazon CloudWatch của hàm Lambda. Như được minh họa trong bảng sau, việc bật SnapStart giúp giảm độ trễ khởi động của ứng dụng Spring Boot mẫu của chúng ta đi 4.3 lần, từ 6.1 giây xuống còn 1.4 giây. Độ trễ cold start 6.1 giây đối với ON_DEMAND chủ yếu là do sự kết hợp của (1) việc khởi tạo JVM và framework Spring Boot, (2) việc biên dịch JIT mã ứng dụng được tải lười (lazy loaded) trong lần gọi đầu tiên và (3) thời gian cần thiết để thiết lập kết nối cơ sở dữ liệu với RDS thông qua Amazon RDS Proxy. Bằng cách bật SnapStart, Lambda sẽ khởi tạo JVM và Spring Boot trước khi hàm được gọi – dẫn đến độ trễ giảm đáng kể còn 1.4 giây.

| Method | Cold Start Invocations | p50 | p90 | p99 | p99.9 |
| --- | --- | --- | --- | --- | --- |
| PrimingLogGroup-1_ON_DEMAND | 128 | 5047.94 ms | 5386.78 ms | 6158.80 ms | 6195.84 ms |
| PrimingLogGroup-2_SnapStart_NO_PRIMING | 111 | 1177.87 ms | 1288.73 ms | 1419.94 ms | 1425.63 ms |

Bạn có thể giảm cold start sâu hơn nữa cho các ứng dụng Spring Boot nhạy cảm về độ trễ của mình bằng cách sử dụng các kỹ thuật priming trên các hàm Lambda. Hãy cùng khám phá cách triển khai các kỹ thuật priming.

## Giải thích về Priming

Priming là quá trình tải trước các dependency và khởi tạo tài nguyên trong pha INIT, thay vì trong pha INVOKE, để tối ưu hóa hơn nữa hiệu năng khởi động với SnapStart. Điều này là cần thiết vì các framework Java sử dụng dependency injection sẽ tải các class vào bộ nhớ khi các class này được gọi một cách tường minh, điều này thường xảy ra trong pha INVOKE của Lambda. Bạn có thể chủ động tải các class bằng cách sử dụng Java runtime hooks, là một phần của dự án mã nguồn mở CRaC (Coordinated Restore at Checkpoint). Bài viết này minh họa cách sử dụng hook này, được gọi là beforeCheckpoint(), để "prime" các hàm Java đã bật SnapStart, theo hai cách:

1. **Invoke Priming**: Cách tiếp cận này bao gồm việc trực tiếp gọi các endpoint hoặc method của ứng dụng trong hook trước khi tạo snapshot (pre-snapshotting hook) để chúng được biên dịch JIT trong pha INIT và được bao gồm trong snapshot. Việc này có thể bao gồm các hoạt động như gọi các endpoint của API Gateway hoặc lấy dữ liệu từ một bucket S3 hoặc cơ sở dữ liệu RDS để chủ động thực thi các luồng mã, đảm bảo rằng các class nền tảng được bao gồm trong snapshot.

2. **Class Priming**: Cách tiếp cận này bao gồm việc khởi tạo chủ động các class trong pha INIT, đảm bảo rằng chúng được bao gồm trong snapshot của hàm mà không có nguy cơ gây ra những thay đổi không mong muốn cho trạng thái hoặc dữ liệu của ứng dụng. Điều này có thể đạt được bằng cách tận dụng method forName() của Java, method này sẽ tải, liên kết và khởi tạo class được chỉ định. "Khởi tạo" (Initialization) đề cập đến quá trình của JVM tải định nghĩa class vào bộ nhớ, xác minh bytecode, chuẩn bị các trường tĩnh với giá trị mặc định, và thực thi các bộ khởi tạo tĩnh. Điều này khác với "khởi tạo đối tượng" (instantiation), là quá trình tạo ra các đối tượng của class bằng cách sử dụng các hàm khởi tạo (constructor). Để tạo ra một danh sách các class cần thiết cho việc tải trước, bạn có thể sử dụng tùy chọn VM option sau, ghi danh sách ra một tệp có tên là classes-loaded.txt: 
```
-Xlog:class+load=info:classes-loaded.txt
```
Mặc dù invoke priming có thể mang lại hiệu năng tốt hơn, nó đòi hỏi nỗ lực bổ sung để đảm bảo rằng các hành động được thực hiện là idempotent (có thể thực hiện nhiều lần mà không thay đổi kết quả) và không có các tác dụng phụ không mong muốn, ví dụ như xử lý các giao dịch tài chính trong một ứng dụng ngân hàng. Vì lý do này, invoke priming chỉ nên được sử dụng khi mã được thực thi trong quá trình priming là idempotent hoặc không làm thay đổi trạng thái. Đối với các kịch bản không thể làm được điều này, class priming cung cấp một giải pháp thay thế an toàn hơn bằng cách chỉ khởi tạo các class mà không thực thi các method của chúng. Lưu ý rằng điều này giả định ứng dụng của bạn không thực thi mã thay đổi trạng thái trong quá trình khởi tạo class.

Với bối cảnh này, hãy xem cách triển khai Invoke priming và Class priming cho một ứng dụng Spring Boot mẫu.

## Ví dụ triển khai priming sử dụng CRaC runtime hook trước khi tạo Lambda snapshot

Bài viết này minh họa cả Invoke priming và Class priming bằng cách sử dụng ứng dụng Spring Boot mẫu. Việc lựa chọn giữa hai phương pháp phụ thuộc vào các yêu cầu và độ phức tạp cụ thể của ứng dụng của bạn.

### Bước 1: Thiết lập ứng dụng Spring Boot của bạn

Thiết lập ứng dụng Spring Boot của bạn bằng cách sử dụng aws-serverless-springboot3-archetype như đã giải thích trong hướng dẫn Quick Start Spring Boot3 của chúng tôi, thêm mã kết nối cơ sở dữ liệu, hoặc đơn giản là clone dự án mẫu từ GitHub repository.

**1. Tạo một ứng dụng Spring Boot.**

```java
package software.amazon.awscdk.examples.unicorn;

@Import({ UnicornConfig.class })
@SpringBootApplication
public class UnicornApplication {
    private static final Logger log = LoggerFactory.getLogger(UnicornApplication.class);
    
    public static void main(String[] arguments) {
        SpringApplication.run(UnicornApplication.class, arguments);
    }
}
```

**2. Thêm tất cả các Maven dependency cần thiết**

Thêm các dependency cho Spring Boot, AWS Lambda, và Kết nối Cơ sở dữ liệu vào tệp pom.xml của bạn. Dependency sau đây chứa các class cần thiết để sử dụng các CRaC runtime hook:

```xml
<dependency>
    <groupId>org.crac</groupId>
    <artifactId>crac</artifactId>
</dependency>
```

**3. Cấu hình kết nối cơ sở dữ liệu**

Thiết lập chi tiết kết nối cơ sở dữ liệu trong tệp application.properties:

```properties
spring.datasource.password=${SPRING_DATASOURCE_PASSWORD}
spring.datasource.url=${SPRING_DATASOURCE_URL}
spring.datasource.username=postgres
spring.datasource.hikari.maximumPoolSize=1
```

### Bước 2: Triển khai Lambda Function Handler với CRaC runtime hook và Phương pháp Invoke Priming

Tạo Lambda Function Handler và tích hợp các CRaC runtime hook để thực thi các method beforeCheckpoint() và afterRestore() trong ứng dụng của bạn trước khi tạo và sau khi khôi phục snapshot.

```java
package software.amazon.awscdk.examples.unicorn.handler;

import org.crac.Core;
import org.crac.Resource;

public class InvokePriming implements RequestHandler<APIGatewayV2HTTPEvent, APIGatewayV2HTTPResponse>, Resource {
    
    @Override
    public APIGatewayV2HTTPResponse handleRequest(APIGatewayV2HTTPEvent event, Context context) {
        var awsLambdaInitializationType = System.getenv("AWS_LAMBDA_INITIALIZATION_TYPE");
        var unicorns = getUnicorns();
        var body = gson.toJson(unicorns);
        return APIGatewayV2HTTPResponse.builder()
            .withStatusCode(200)
            .withBody(body)
            .build();
    }

    @Override
    public void beforeCheckpoint(org.crac.Context<? extends Resource> context) throws Exception {
        var event = APIGatewayV2HTTPEvent.builder().build();
        handleRequest(event, null);
    }
}
```

### Bước 3: Triển khai Phương pháp Class priming

Phương pháp class priming tập trung vào việc tải trước các class cần thiết để đạt được hiệu năng tối ưu. Để triển khai class priming, hãy tạo danh sách các class được tải trong quá trình khởi động ứng dụng và thực thi hàm bằng cách chạy ứng dụng cục bộ với JVM argument sau:

```
-Xlog:class+load=info:classes-loaded.txt
```

**1. Đảm bảo rằng các class ứng dụng của bạn không làm thay đổi trạng thái trong quá trình khởi tạo tĩnh.**

Tệp classes-loaded.txt được tạo ra chứa các mục class ở định dạng sau:

```
[0.068s][info][class,load]software.amazon.awscdk.examples.unicorn.handler.ClassPriming source: file:/var/task/
```

**2. Trích xuất danh sách các class từ tệp**

Chỉ trích xuất các tên class đủ điều kiện (fully qualified class names) từ mỗi dòng:

```java
software.amazon.awscdk.examples.unicorn.handler.ClassPriming
```

**3. Sử dụng method tiện ích để tải các class từ tệp**

```java
package software.amazon.awscdk.examples.unicorn.service;

public class ClassLoaderUtil {
    public static void loadClassesFromFile() {
        log.info("loadClassesFromFile->started");
        Path path = Paths.get("classes-loaded.txt");
        try (BufferedReader bufferedReader = Files.newBufferedReader(path)) {
            Stream<String> lines = bufferedReader.lines();
            lines.forEach(line -> {
                var index1 = line.indexOf("[class,load]");
                var index2 = line.indexOf(" source: ");
                if (index1 < 0 || index2 < 0) {
                    return;
                }
                var className = line.substring(index1 + 13, index2);
                try {
                    Class.forName(className, true, ClassPriming.class.getClassLoader());
                } catch (Throwable ignored) {
                }
            });
            log.info("loadClassesFromFile->finished");
        } catch (IOException exception) {
            log.error("Error on newBufferedReader", exception);
        }
    }
}
```

**4. Triển khai class priming trong handler**

```java
package software.amazon.awscdk.examples.unicorn.handler;

import org.crac.Core;
import org.crac.Resource;

public class ClassPriming implements RequestHandler<APIGatewayV2HTTPEvent, APIGatewayV2HTTPResponse>, Resource {
    
    public ClassPriming() {
        ConfigurableApplicationContext configurableApplicationContext = SpringApplication.run(UnicornApplication.class);
        this.unicornService = configurableApplicationContext.getBean(UnicornService.class);
        this.gson = configurableApplicationContext.getBean(Gson.class);
        Core.getGlobalContext().register(this);
    }

    @Override
    public APIGatewayV2HTTPResponse handleRequest(APIGatewayV2HTTPEvent event, Context context) {
        var unicorns = getUnicorns();
        var body = gson.toJson(unicorns);
        return APIGatewayV2HTTPResponse.builder()
            .withStatusCode(200)
            .withBody(body)
            .build();
    }

    @Override
    public void beforeCheckpoint(org.crac.Context<? extends Resource> context) throws Exception {
        ClassLoaderUtil.loadClassesFromFile();
    }
}
```

### Bước 4: Thiết lập Cơ sở hạ tầng AWS CDK

CDK stack sẽ triển khai một ứng dụng serverless và cơ sở hạ tầng cần thiết để kiểm thử các chiến lược tối ưu hóa Lambda khác nhau. Nó tạo ra một VPC với các private subnet, một instance RDS for PostgreSQL với một database proxy, và năm hàm Lambda triển khai các phương pháp tối ưu hóa khác nhau (ON_DEMAND không có SnapStart, SnapStart không có priming, SnapStart với invoke priming, và SnapStart với class priming).

Thực hiện theo các bước sau để triển khai cơ sở hạ tầng:

**1. Clone repository mẫu:**

```bash
git clone https://github.com/aws-samples/lambda-priming-crac-java-cdk.git
```

**2. Triển khai CDK stack:**

```bash
cd lambda-priming-crac-java-cdk/infrastructure
cdk synth
cdk deploy --require-approval never --all 2>&1 | tee cdk_output.txt
```

**3. Lưu các URL của API Gateway**

**4. Trích xuất các URL vào các biến để kiểm thử:**

```bash
ONDEMAND_URL=$(grep -oE 'https://[a-zA-Z0-9.-]+\.execute-api\.[a-zA-Z0-9-]+\.amazonaws\.com/prod/' "cdk_output.txt" | head -n 1)
NOPRIMING_URL=$(grep -oE 'https://[a-zA-Z0-9.-]+\.execute-api\.[a-zA-Z0-9-]+\.amazonaws\.com/prod/' "cdk_output.txt" | head -n 2 | tail -n 1)
INVOKEPRIMING_URL=$(grep -oE 'https://[a-zA-Z0-9.-]+\.execute-api\.[a-zA-Z0-9-]+\.amazonaws\.com/prod/' "cdk_output.txt" | head -n 3 | tail -n 1)
CLASSPRIMING_URL=$(grep -oE 'https://[a-zA-Z0-9.-]+\.execute-api\.[a-zA-Z0-9-]+\.amazonaws\.com/prod/' "cdk_output.txt" | head -n 4 | tail -n 1)
SETUP_URL=$(grep -oE 'https://[a-zA-Z0-9.-]+\.execute-api\.[a-zA-Z0-9-]+\.amazonaws\.com/prod/' "cdk_output.txt" | head -n 5 | tail -n 1)
```

### Bước 5: Tải dữ liệu cơ sở dữ liệu và chạy kiểm tra hiệu năng

**1. Khởi tạo cơ sở dữ liệu với dữ liệu mẫu:**

```bash
curl -X GET "$SETUP_URL"
# Kết quả mong đợi: {"message":"Database schema initialized and data loaded"}
```

**2. Chạy kiểm tra hiệu năng cho tất cả các endpoint:**

```bash
artillery run -t "$ONDEMAND_URL" -v '{ "url": "/unicorn" }' ./loadtest.yaml && \
artillery run -t "$NOPRIMING_URL" -v '{ "url": "/unicorn" }' ./loadtest.yaml && \
artillery run -t "$INVOKEPRIMING_URL" -v '{ "url": "/unicorn" }' ./loadtest.yaml && \
artillery run -t "$CLASSPRIMING_URL" -v '{ "url": "/unicorn" }' ./loadtest.yaml
```

### Bước 6: So sánh kết quả kiểm tra tải

Kết quả kiểm tra hiệu năng trong bảng dưới đây được sắp xếp từ độ trễ khởi động chậm nhất đến nhanh nhất. Hàm không có SnapStart hoạt động chậm nhất do việc khởi tạo JVM, tải class và biên dịch JIT xảy ra khi hàm được gọi. Chú ý đến sự cải thiện 4.3 lần với SnapStart, vốn khôi phục các lệnh gọi từ một snapshot đã được khởi tạo trước, do đó tránh được việc khởi tạo JVM và biên dịch JIT ban đầu.

SnapStart với class priming đạt được tốc độ nhanh hơn 1.4 lần so với SnapStart thông thường, bằng cách chủ động tải/khởi tạo các class trong pha INIT để chúng được bao gồm trong snapshot của hàm bạn. Cuối cùng, SnapStart với invoke priming đạt được hiệu năng nhanh nhất – với độ trễ cold-start p99.9 là 781.68ms, nhanh hơn 1.8 lần so với SnapStart. Điều này là do ngoài việc khởi tạo các class, nó còn thực thi các method trên các instance của những class đó, dẫn đến việc có nhiều thành phần hơn được đưa vào snapshot của hàm.

| Method | Cold Start Invocations | p50 | p90 | p99 | p99.9 |
| --- | --- | --- | --- | --- | --- |
| PrimingLogGroup-1_ON_DEMAND | 128 | 5047.94 ms | 5386.78 ms | 6158.80 ms | 6195.84 ms |
| PrimingLogGroup-2_SnapStart_NO_PRIMING | 111 | 1177.87 ms | 1288.73 ms | 1419.94 ms | 1425.63 ms |
| PrimingLogGroup-4_SnapStart_CLASS_PRIMING | 82 | 857.81 ms | 997.49 ms | 1085.94 ms | 1085.94 ms |
| PrimingLogGroup-3_SnapStart_INVOKE_PRIMING | 66 | 608.42 ms | 688.88 ms | 781.68 ms | 781.68 ms |

Lưu ý rằng với invoke priming, bất kỳ mã ứng dụng nào bạn thực thi phải là idempotent hoặc chỉ sửa đổi dữ liệu giả (stub data). Ví dụ, hãy xem xét mã ứng dụng kích hoạt một giao dịch tài chính. Nếu mã này được thực thi trong quá trình invoke priming với dữ liệu người dùng thật, nó có thể gây ra các hiệu ứng không mong muốn với những hậu quả tiềm tàng nghiêm trọng. Class priming tránh được điều này, vì các class ứng dụng được khởi tạo thay vì được tạo đối tượng (instantiated) và thực thi các method của chúng. Điều này giả định rằng mã ứng dụng không thực thi logic sửa đổi trạng thái trong quá trình khởi tạo class.

## Kết luận

Bài viết này đã chỉ ra cách AWS Lambda SnapStart, được tăng cường bởi các CRaC runtime hook, mở ra khả năng kiểm soát chi tiết việc tối ưu hóa cold-start cho các ứng dụng Java thông qua hai chiến lược priming riêng biệt:

- **Invoke Priming**: Cải thiện hiệu năng bằng cách thực thi các endpoint quan trọng trong quá trình tạo snapshot, lý tưởng cho các luồng công việc idempotent.
- **Class Priming**: Tải trước các class mà không kích hoạt business logic, giúp giảm thiểu rủi ro về tác dụng phụ.

Để triển khai các kỹ thuật tối ưu hóa này trong ứng dụng của bạn, hãy đánh giá trường hợp sử dụng của bạn và chọn phương pháp priming tối ưu. Theo dõi sự sụt giảm độ trễ và việc sử dụng tài nguyên của ứng dụng thông qua các metric của Amazon CloudWatch để định lượng các cải tiến về hiệu năng. Bằng cách tích hợp các chiến lược này, các nhà phát triển có thể đạt được cold start dưới một giây trong khi vẫn duy trì khả năng mở rộng và hiệu quả chi phí của kiến trúc serverless khi sử dụng Java.

Để tìm hiểu sâu hơn, hãy xem GitHub repository với mã nguồn ví dụ đầy đủ, bao gồm hướng dẫn thiết lập và các mẫu có thể tái sử dụng mà bạn có thể điều chỉnh cho các dự án của riêng mình. Để có thêm nhiều examples of Java applications running on AWS Lambda, hãy truy cập serverlessland.com và khám phá nhiều loại tài nguyên, hướng dẫn và các trường hợp sử dụng thực tế.
