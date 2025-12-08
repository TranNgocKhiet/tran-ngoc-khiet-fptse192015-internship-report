---
title: "Blog 2"
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---

# Optimizing cold start performance of AWS Lambda using advanced priming strategies with SnapStart

by Shan Kandaswamy and Gustavo Martim | on 29 APR 2025 | in [Advanced (300)](https://aws.amazon.com/blogs/compute/category/learning-levels/advanced-300/), [AWS Lambda](https://aws.amazon.com/blogs/compute/category/compute/aws-lambda/), [Best Practices](https://aws.amazon.com/blogs/compute/category/post-types/best-practices/), [Serverless](https://aws.amazon.com/blogs/compute/category/serverless/), [Technical How-to](https://aws.amazon.com/blogs/compute/category/post-types/technical-how-to/) | [Permalink](https://aws.amazon.com/blogs/compute/optimizing-cold-start-performance-of-aws-lambda-using-advanced-priming-strategies-with-snapstart/) | Share

Introduced at re:Invent 2022, [SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) is a performance optimization that makes it easier to build highly responsive and scalable applications using [AWS Lambda](https://aws.amazon.com/lambda/). The largest contributor to startup latency (often referred to as cold-start time) is the time spent initializing a function. This includes loading the function's code and initializing dependencies. For latency-sensitive workloads such as APIs and real-time data processing applications, high startup latency can result in a suboptimal end user experience. Lambda SnapStart can reduce startup duration from several seconds to as low as sub-second, with minimal or no code changes. This post discusses 'Priming', a technique to further optimize startup times for AWS Lambda functions built using Java and Spring Boot.

Spring Boot applications typically experience high cold start latency during JVM and framework initialization, where significant time is spent loading classes and performing Just-In-Time (JIT) compilation of Java bytecode. This blog post uses a Spring Boot application as an example that retrieves 10 records from a 'UnicornEmployee' table in an [Amazon RDS](https://aws.amazon.com/rds/) for PostgreSQL database, where each employee record includes employee name, location, and hire date.

The sample application uses [Amazon API Gateway](https://aws.amazon.com/api-gateway/) which triggers an AWS Lambda function that connects to the database through RDS Proxy to return the employee data. While this sample application uses dummy employee data for demonstration, the patterns and optimization techniques discussed in this post are applicable to real-world scenarios with similar data access patterns. Sample code for this implementation can be found in our GitHub repository at [lambda-priming-crac-java-cdk](https://github.com/aws-samples/lambda-priming-crac-java-cdk).

## Background: How SnapStart works

The post assumes familiarity with SnapStart and provides a short background. For additional details, refer to the [SnapStart documentation](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html).

To quickly recap, the [INIT](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html) phase for a Lambda function involves downloading the function's code, starting the runtime and any external dependencies, and running the function's initialization code. For functions that don't use SnapStart, this phase occurs each time your application scales up to create a new execution environment. When SnapStart is activated, the INIT phase happens when you publish a function version.

The following image shows a comparison of a Lambda request lifecycle with and without SnapStart.

![Lambda Request Lifecycle Comparison](/images/blog-2/ComputeBlog-2165img1.png)

*Figure 1 – comparison of a Lambda request lifecycle with and without SnapStart*

At the end of the INIT phase, Lambda executes your before-checkpoint [runtime hooks](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks.html). Lambda then snapshots the memory and disk state of the initialized execution environment, persists the encrypted snapshot, and caches it for low-latency access. When the function is subsequently invoked, new execution environments are resumed from the cached snapshot (during the [RESTORE](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html#runtimes-lifecycle-restore) phase), speeding up function startup.

![Execution Environments Resume from Snapshot](/images/blog-2/ComputeBlog-2165img2.png)

*Figure 2 – new execution environments are resumed from the cached snapshot*

You can validate this speedup by comparing the RESTORE duration with the INIT duration recorded before SnapStart in your Lambda function's [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) Logs. As demonstrated in the following table, enabling SnapStart reduces the startup latency of our sample Spring Boot application by 4.3x from 6.1s to 1.4s. The 6.1s cold start latency for `ON_DEMAND` is primarily due to the combination of (1) initializing the JVM and Spring Boot framework, (2) JIT compilation of lazy loaded application code during initial invocation and (3) the time needed to establish a database connection with RDS through [Amazon RDS Proxy](https://aws.amazon.com/rds/proxy/). By enabling SnapStart, Lambda initializes the JVM and Spring Boot prior to the function invocation – resulting in the significantly reduced latency of 1.4s.

| Method | Cold Start Invocations | p50 | P90 | P99 | p99.9 |
| --- | --- | --- | --- | --- | --- |
| PrimingLogGroup-1_ON_DEMAND | 128 | 5047.94 ms | 5386.78 ms | 6158.80 ms | 6195.84 ms |
| PrimingLogGroup-2_SnapStart_NO_PRIMING | 111 | 1177.87 ms | 1288.73 ms | 1419.94 ms | 1425.63 ms |

You can reduce cold starts even further for your latency-sensitive Spring Boot applications by using priming techniques on Lambda functions. Let's explore how to implement priming techniques.

## Priming explained

Priming is the process of preloading dependencies and initializing resources during the INIT phase, rather than during the INVOKE phase to further optimize startup performance with SnapStart. This is required because Java frameworks that use dependency injection load classes into memory when these classes are explicitly invoked, which typically happens during Lambda's INVOKE phase. You can proactively load classes using [Java runtime hooks](https://docs.aws.amazon.com/lambda/latest/dg/snapstart-runtime-hooks-java.html), that are part of the open source [CRaC ](https://openjdk.org/projects/crac/)(Coordinated Restore at Checkpoint) project. This post demonstrates how to use this hook, called `beforeCheckpoint()`, to prime SnapStart-enabled Java functions, in two ways:

1. **Invoke Priming**: This approach involves directly invoking application endpoints or methods in your pre-snapshotting hook so that they are JIT compiled during the INIT phase and included in the snapshot. This can include operations such as invoking API Gateway endpoints or fetching data from an S3 bucket or RDS database to proactively execute the code paths, ensuring that the underlying classes are included in the snapshot.

2. **Class Priming**: This approach involves proactive initialization of classes during the INIT phase, ensuring that they are included in the function's snapshot without risking unwanted changes to application state or data. This can be achieved by leveraging Java's `forName()` method, which loads, links, and initializes the specified class. Initialization refers to the JVM process of loading the class definition into memory, verifying the bytecode, preparing static fields with default values, and executing static initializers. This is different from instantiation, which creates objects of the class using constructors. To generate a list of the classes required for pre-loading, you can use the following VM option, writing the list to a file called classes-loaded.txt: `-Xlog:class+load=info:classes-loaded.txt`

While invoke priming can offer better performance, it requires additional effort to ensure that the actions performed are idempotent and do not have unintended side effects, for instance processing financial transactions in a banking application. For this reason, invoke priming should only be used when code executed during priming is either idempotent or does not modify state. For scenarios where this is not possible, class priming provides a safer alternative by only initializing classes without executing their methods. Note that this assumes your application does not execute state-modifying code during class initialization.

With this context, let's look at how to implement Invoke and Class priming for a Spring Boot sample application.

### Example priming Implementation using CRaC runtime hooks before taking a Lambda snapshot

This post demonstrates both Invoke priming and Class priming using the sample Spring Boot application. The choice between the two approaches depends on the specific requirements and complexities of your application.

**Step 1: Set up your Spring Boot Application** using the `aws-serverless-springboot3-archetype` as explained in our [Quick Start Spring Boot3](https://github.com/aws/serverless-java-container/wiki/Quick-start---Spring-Boot3) guide, adding database connectivity code, or simply clone the sample project from [GitHub repository](https://github.com/aws-samples/lambda-priming-crac-java-cdk).

1. Create a Spring Boot Application.

```java
// src/main/java/software/amazon/awscdk/examples/unicorn/UnicornApplication.java
package software.amazon.awscdk.examples.unicorn;
…
@Import({ UnicornConfig.class })
@SpringBootApplication
public class UnicornApplication {

    private static final Logger log = LoggerFactory.getLogger(UnicornApplication.class);

    public static void main(String... arguments) {
        SpringApplication.run(UnicornApplication.class, arguments);
    }

}
```

2. Add all the necessary Maven dependencies for Spring Boot, AWS Lambda, and Database Connection in your [pom.xml](https://github.com/aws-samples/lambda-priming-crac-java-cdk/blob/main/software/priming/pom.xml) file. The following, highlighted, dependency contains the classes required to use the CRaC runtime hooks.

```xml
...
        <dependency>
            <groupId>org.crac</groupId>
            <artifactId>crac</artifactId>
        </dependency>
...
```

3. Configure Database Connection – Set up the database connection details in application.properties.

```properties
spring.datasource.password=${SPRING_DATASOURCE_PASSWORD} 
spring.datasource.url=${SPRING_DATASOURCE_URL} 
spring.datasource.username=postgres 
spring.datasource.hikari.maximumPoolSize=1 
```

**Step 2: Implement Lambda Function Handler with CRaC runtime hooks and Invoke Priming Approach:**

Create Lambda Function Handler and integrate CRaC runtime hooks to execute `beforeCheckpoint()` and `afterRestore()` methods in your application for before taking and after restoring the snapshot.

1. Implement the `RequestHandler<UnicornRequest, UnicornResponse>` interface in the Lambda function handler class.
2. Implement the CRaC resource interface with two methods: `beforeCheckpoint()` and `afterRestore()`, which defines actions performed before Lambda creates the snapshot and after the snapshot is restored.
3. Add invoke priming by creating a `UnicornRequest` object with a `GET` request to a specific endpoint (such as, `/unicorn`) and call the `handleRequest(unicornRequest, null)` method.

This ensures that the code paths associated with the specified endpoint are JIT compiled and optimized for faster execution during the first invocation after the snapshot is restored.

```java
/src/main/java/software/amazon/awscdk/examples/unicorn/handler/InvokePriming.java
package software.amazon.awscdk.examples.unicorn.handler;

import org.crac.Core;
import org.crac.Resource;
...

public class InvokePriming implements RequestHandler<APIGatewayV2HTTPEvent, APIGatewayV2HTTPResponse>, Resource {
	...

@Override
public APIGatewayV2HTTPResponse handleRequest(APIGatewayV2HTTPEvent event, Context context) {
    var awsLambdaInitializationType = System.getenv("AWS_LAMBDA_INITIALIZATION_TYPE");
    var unicorns = getUnicorns();
    var body = gson.toJson(unicorns);
    return APIGatewayV2HTTPResponse.builder().withStatusCode(200).withBody(body).build();
}

@Override
public void beforeCheckpoint(org.crac.Context<? extends Resource> context)
        throws Exception {
    var event = APIGatewayV2HTTPEvent.builder().build();
    handleRequest(event, null);
}
...
}
```

**Step 3: Implement Class priming Approach:**

The class priming approach focuses on pre-loading required classes to achieve optimal performance. To implement class priming, generate the list of classes that are loaded during the application startup and function execution by running the application locally using the following JVM argument: `-Xlog:class+load=info:classes-loaded.txt`

1. Ensure that your application classes included in the generated `classes-loaded.txt` file are not mutating state during static initialization. Note: the generated `classes-loaded.txt` contains class entries in the following format: `[0.068s][info][class,load] software.amazon.awscdk.examples.unicorn.handler.ClassPriming source: file:/var/task/`

2. Extract only the fully qualified class names from each line and remove the additional logging information. For Example: `software.amazon.awscdk.examples.unicorn.handler.ClassPriming`

3. Use the `ClassLoaderUtil.loadClassesFromFile()` utility method to extract the generated class entries.

```java
//src/main/java/software/amazon/awscdk/examples/unicorn/service/ClassLoaderUtil.java
package software.amazon.awscdk.examples.unicorn;
	...
public class ClassLoaderUtil {
	...
    public static void loadClassesFromFile() {
        log.info("loadClassesFromFile->started");
        Path path = Paths.get("classes-loaded.txt");

        try (BufferedReader bufferedReader = Files.newBufferedReader(path)) {
            Stream<String> lines = bufferedReader.lines();
            lines.forEach(line -> {
                var index1 = line.indexOf("[class,load] ");
                var index2 = line.indexOf(" source: ");

                if (index1 < 0 || index2 < 0) {
                    return;
                }

                var className = line.substring(index1 + 13, index2);
                try {
                    Class.forName(className, true,
                            ClassPriming.class.getClassLoader());
                } catch (Throwable ignored) {
                }
            });

            log.info("loadClassesFromFile->finished");
        } catch (IOException exception) {
            log.error("Error on newBufferedReader", exception);
        }
    }
...
}
```

4. Read a file (such as, `/classes-loaded.txt`) that contains a list of classes that have been loaded during the application's execution in the `beforeCheckpoint()` method.

5. Use the `Class.forName()` method to load and initialize the class, ensuring that it is ready during the snapshot. Note: by systematically pre-loading these classes, the Class priming approach simplifies the optimization process and reduces the complexities associated with Invoke priming.

```java
//src/main/java/software/amazon/awscdk/examples/unicorn/handler/ClassPriming.java
package software.amazon.awscdk.examples.unicorn.handler;

...
import org.crac.Core;
import org.crac.Resource;

public class ClassPriming implements RequestHandler<APIGatewayV2HTTPEvent, APIGatewayV2HTTPResponse>, Resource {

...
        ConfigurableApplicationContext configurableApplicationContext =
				SpringApplication.run(UnicornApplication.class);

        this.unicornService = configurableApplicationContext.getBean(UnicornService.class);
        this.gson = configurableApplicationContext.getBean(Gson.class);

        Core.getGlobalContext().register(this);
    }

    @Override
    public APIGatewayV2HTTPResponse handleRequest(APIGatewayV2HTTPEvent event, Context context) {
        var unicorns = getUnicorns();
        var body = gson.toJson(unicorns);

        return APIGatewayV2HTTPResponse.builder().withStatusCode(200).withBody(body).build();
    }

    @Override
    public void beforeCheckpoint(org.crac.Context<? extends Resource> context)
            throws Exception {

        ClassLoaderUtil.loadClassesFromFile();

    }
...
}
```

**Step 4: AWS CDK Infrastructure Setup**

Before proceeding, review the prerequisites in the project [README](https://github.com/aws-samples/lambda-priming-crac-java-cdk/tree/main#requirements) file.

The CDK stack deploys a serverless application and required infrastructure for testing different Lambda optimization strategies. It creates a VPC with private subnets, an RDS for PostgreSQL instance with a database proxy, and five Lambda functions implementing different optimization approaches (ON_DEMAND without SnapStart, SnapStart without priming, SnapStart with invoke priming, and SnapStart with class priming). Each Lambda function is integrated with API Gateway for HTTP access, configured with Java 21 runtime on ARM64 architecture, and includes CloudWatch log groups for monitoring.

Follow these steps to deploy the infrastructure:

1. Clone the sample repository:
```bash
git clone https://github.com/aws-samples/lambda-priming-crac-java-cdk.git
```

2. Deploy the CDK stack:
```bash
cd lambda-priming-crac-java-cdk/infrastructure
cdk synth
cdk deploy --require-approval never --all 2>&1 | tee cdk_output.txt
```

3. Save the API Gateway URLs: The deployment will output five URLs in this format:
```
# ON_DEMAND endpoint (without SnapStart)
LambdaPrimingCracJavaCdkStack.PrimingJavaRestApi1ONDEMANDEndpoint = https://[id].execute-api.us-east-1.amazonaws.com/prod/

# SnapStart without priming endpoint
LambdaPrimingCracJavaCdkStack.PrimingJavaRestApi2SnapStartNOPRIMINGEndpoint = https://[id].execute-api.us-east-1.amazonaws.com/prod/

# SnapStart with invoke priming endpoint
LambdaPrimingCracJavaCdkStack.PrimingJavaRestApi3SnapStartINVOKEPRIMINGEndpoint = https://[id].execute-api.us-east-1.amazonaws.com/prod/

# SnapStart with class priming endpoint
LambdaPrimingCracJavaCdkStack.PrimingJavaRestApi4SnapStartCLASSPRIMINGEndpoint = https://[id].execute-api.us-east-1.amazonaws.com/prod/

# Database setup endpoint
LambdaPrimingCracJavaCdkStack.PrimingJavaRestApi5DBLOADEREndpoint = https://[id].execute-api.us-east-1.amazonaws.com/prod/
```

4. Extract the URLs into variables for testing:
```bash
ONDEMAND_URL=$(grep -oE 'https://[a-zA-Z0-9.-]+\.execute-api\.[a-zA-Z0-9-]+\.amazonaws\.com/prod/' "cdk_output.txt" | head -n 1)
NOPRIMING_URL=$(grep -oE 'https://[a-zA-Z0-9.-]+\.execute-api\.[a-zA-Z0-9-]+\.amazonaws\.com/prod/' "cdk_output.txt" | head -n 2 | tail -n 1)
INVOKEPRIMING_URL=$(grep -oE 'https://[a-zA-Z0-9.-]+\.execute-api\.[a-zA-Z0-9-]+\.amazonaws\.com/prod/' "cdk_output.txt" | head -n 3 | tail -n 1)
CLASSPRIMING_URL=$(grep -oE 'https://[a-zA-Z0-9.-]+\.execute-api\.[a-zA-Z0-9-]+\.amazonaws\.com/prod/' "cdk_output.txt" | head -n 4 | tail -n 1)
SETUP_URL=$(grep -oE 'https://[a-zA-Z0-9.-]+\.execute-api\.[a-zA-Z0-9-]+\.amazonaws\.com/prod/' "cdk_output.txt" | head -n 5 | tail -n 1)
```

**Step 5: Load database and run performance testing using [artillery](https://www.artillery.io/):**

1. Initialize the database with sample data.
```bash
curl -X GET "$SETUP_URL"

#Expected output: {"message":"Database schema initialized and data loaded"}
```

2. Run performance tests for all endpoints
```bash
artillery run -t "$ONDEMAND_URL" -v '{ "url": "/unicorn" }' ./loadtest.yaml && \
artillery run -t "$NOPRIMING_URL" -v '{ "url": "/unicorn" }' ./loadtest.yaml && \
artillery run -t "$INVOKEPRIMING_URL" -v '{ "url": "/unicorn" }' ./loadtest.yaml && \
artillery run -t "$CLASSPRIMING_URL" -v '{ "url": "/unicorn" }' ./loadtest.yaml
```

**Step 6: Compare the load test results** for On-demand (non-SnapStart), SnapStart, Invoke priming, and Class priming

The performance test results in the table below are sorted from slowest to fastest startup latency. The function without SnapStart performs the slowest due to JVM initialization, class loading and JIT compilation that occurs when the function is invoked. Notice a 4.3x improvement with SnapStart, which resumes invocations from a pre-initialized snapshot thereby avoiding JVM initialization and initial JIT compilation. SnapStart with class priming achieves a 1.4x speed-up over SnapStart, by proactively loading/initializing classes during INIT so that they are included in your function's snapshot. Finally, SnapStart with invoke priming achieves the fastest performance – with a 781.68ms p99.9 cold-start latency that is 1.8x faster than SnapStart. This is because in addition to initializing classes, it also executes methods on the instances of those classes, resulting in even more components being included in the function's snapshot.

Note that with invoke priming, any application code you execute must either be idempotent or modify stub data only. For instance, consider application code that triggers a financial transaction. If this code is executed during invoke priming with real user data, it may drive unintended effects with potentially serious consequences. Class priming avoids this, since application classes are initialized rather than being instantiated and their methods executed. This assumes that application code does not execute state modifying logic during class initialization. We recommend that you keep these considerations in mind when using invoke and/or class priming, and choose the appropriate approach for your use case.

| Method | Cold Start Invocations | p50 | P90 | P99 | p99.9 |
| --- | --- | --- | --- | --- | --- |
| PrimingLogGroup-1_ON_DEMAND | 128 | 5047.94 ms | 5386.78 ms | 6158.80 ms | 6195.84 ms |
| PrimingLogGroup-2_SnapStart_NO_PRIMING | 111 | 1177.87 ms | 1288.73 ms | 1419.94 ms | 1425.63 ms |
| PrimingLogGroup-4_SnapStart_CLASS_PRIMING | 82 | 857.81 ms | 997.49 ms | 1085.94 ms | 1085.94 ms |
| PrimingLogGroup-3_SnapStart_INVOKE_PRIMING | 66 | 608.42 ms | 688.88 ms | 781.68 ms | 781.68 ms |

## Conclusion

This post showed how AWS Lambda SnapStart, enhanced by CRaC runtime hooks, unlocks granular control over cold-start optimization for Java applications through two distinct priming strategies:

- **Invoke Priming**: improves performance by executing critical endpoints during snapshot creation, ideal for idempotent workflows.
- **Class Priming**: preloads classes without triggering business logic, mitigating side-effect risks.

To implement these optimization techniques in your applications evaluate your use case and opt for the optimal priming approach. Track latency reductions and resource utilization of your application via Amazon CloudWatch metrics to quantify performance improvements. By integrating these strategies, developers can achieve sub-second cold starts while maintaining the scalability and cost-efficiency of serverless architecture using Java.

To dive deeper, check out the [GitHub repository](https://github.com/aws-samples/lambda-priming-crac-java-cdk) with the full example code, including setup instructions and reusable patterns you can adapt to your own projects. For more [examples of Java applications running on AWS Lambda](https://serverlessland.com/repos?services=lambda&runtime=Java), visit [serverlessland.com](https://serverlessland.com/) and explore a wide range of resources, tutorials, and real-world use cases.
