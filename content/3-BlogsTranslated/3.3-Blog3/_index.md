---
title: "Blog 3"
weight: 1
chapter: false
pre: " <b> 3.3. </b> "
---

# Operating BYOL Windows Server Workloads Effectively on AWS

by Ali Alzand, Jon Madison, and Mike Gupta | on 01 JUL 2025 | in [Amazon EC2](https://aws.amazon.com/blogs/modernizing-with-aws/category/compute/amazon-ec2/), [AWS Config](https://aws.amazon.com/blogs/modernizing-with-aws/category/management-tools/aws-config/), [AWS Cost and Usage Report](https://aws.amazon.com/blogs/modernizing-with-aws/category/aws-cloud-financial-management/aws-cost-and-usage-report/), [AWS License Manager](https://aws.amazon.com/blogs/modernizing-with-aws/category/management-tools/aws-license-manager/), [AWS Migration Hub](https://aws.amazon.com/blogs/modernizing-with-aws/category/migration/aws-migration-hub/), [Technical How-to](https://aws.amazon.com/blogs/modernizing-with-aws/category/post-types/technical-how-to/), [Windows on AWS](https://aws.amazon.com/blogs/modernizing-with-aws/category/aws-on-windows/) | [Permalink](https://aws.amazon.com/blogs/modernizing-with-aws/operating-byol-windows-server-workloads-effectively-on-aws/) | Share

One way that customers running [Microsoft Workloads on Amazon Web Services (AWS)](https://aws.amazon.com/microsoft/) may reduce costs is taking advantage of **Bring Your Own License** (BYOL) for eligible licenses they own. In this blog post, we are going to share a few practices to help you optimize your operation of BYOL Windows Server workloads on AWS.

## Introduction

A common way to run your Windows Server workloads on [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) is to use the “license included” option. This has the benefit of not having to purchase or manage your own licenses and the flexibility of per-second billing. However, if you have already purchased licenses and they are eligible for use on AWS, then it makes sense to bring them and reduce your costs accordingly.

We will review several specific techniques to help you when running BYOL Windows Server workloads on AWS. They are:

- Preparing your on-premises servers for import to AWS as [Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html).
- Transition and manage your Windows licenses from BYOL to license included when appropriate.
- Detecting configuration issues using an [AWS Config](https://aws.amazon.com/config/) custom rule.
- Understanding data related to your BYOL Windows instances in the [AWS Cost and Usage Report](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/) (AWS CUR).
  
## BYOL for Windows on AWS

To take advantage of BYOL, you need to confirm that they are eligible. AWS provides [guidance for Microsoft Licensing on AWS](https://aws.amazon.com/windows/resources/licensing/). When determining if your Windows licenses are eligible for BYOL on AWS, consider:

- Licenses must be perpetual, and purchased before October 1, 2019, or as a true-up on an Enterprise Agreement (EA) that was active at that time.
- The Windows version must be Windows Server 2019 or earlier.
  
If your licenses are eligible, then you can use them on AWS. Regardless of whether or not you have Software Assurance on your licenses, Windows Server is not eligible for [License Mobility](https://aws.amazon.com/windows/resources/licensemobility/). This means that the licenses will need to apply to hardware dedicated to you alone. [Amazon EC2 Dedicated Hosts](https://aws.amazon.com/ec2/dedicated-hosts/) are a solution that fulfills this requirement. Dedicated Hosts provide you with a familiar experience for running your Amazon EC2 instances, without the need to manage hardware or a hypervisor. [AWS License Manager](https://aws.amazon.com/license-manager/) is a service used to manage licenses in AWS, and it is key to an effective BYOL Windows strategy.

The billing for your Amazon EC2 Windows instances is determined from the [usage operation](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/billing-info-fields.html#billing-info) field that the instance inherits from its source AMI. Windows instances that run with the license included, regardless of tenancy, use the usage operation of **RunInstances:0002**. However, when you use your own license for a Windows instance on dedicated hosts, the usage operation of **RunInstances:0800** is required. The [how to create an Amazon EC2 AMI usage and billing information report](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-create-an-amazon-ec2-ami-usage-and-billing-information-report/) blog post will help you generate the usage operation for the instances in your organization.

## Preparing your images for BYOL

One requirement for using your own Windows licenses on AWS is to supply your own AMI, rather than using one created by AWS. When bringing your own image to AWS, you have different options to produce them. If the destination for your Windows server is BYOL on dedicated hosts, these tools will help you ensure your AMI is ready for use.

[VM Import/Export](https://aws.amazon.com/ec2/vm-import/) (VMIE) is a tool that helps you to import virtual machine images from your existing virtualization platform as Amazon Machine Images. The first step is to export your virtual machine using a standard [format](https://docs.aws.amazon.com/vm-import/latest/userguide/prerequisites.html#vmimport-image-formats) such as Open Virtual Appliance (OVA), ESX Virtual Machine Disk (VMDK), or Virtual Hard Disk (VHD/VHDX). Then, upload the image to an [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (S3) bucket in anticipation of the conversion process.

To use VMIE, use [these instructions](https://docs.aws.amazon.com/vm-import/latest/userguide/required-permissions.html#vmimport-role) to create an [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) role named “vmimport” that the service will use to perform operations on your behalf.

When using the [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI) to [import a Windows image](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportImage.html) that you are planning on using for BYOL on dedicated hosts, it is necessary to specify the license type to set the usage operation correctly on the resultant AMI. To import an image, a command such as the following can be used (in this case for an OVA image in an S3 bucket):

```
aws ec2 import-image –usage-operation RunInstances:0800 –disk-containers Format=OVA,Url=s3://<<my-bucket>>/<<my-image-name>>.ova
```

This will start an import job that, once completed, will yield an AMI with the proper usage code for Windows BYOL.

[Migration Hub Orchestrator](https://docs.aws.amazon.com/migrationhub/latest/ug/gs-orchestrator.html) is a tool that lets you create workflows to automate tasks and simplify the migration process. One of the workflow templates that Orchestrator provides is “Import virtual machine images to AWS”. Use this workflow to import an image for Windows BYOL.

1. Open the AWS console and navigate to the [Migration Hub Console](https://console.aws.amazon.com/migrationhub/home).
2. Choose **Workflows** in the **Orchestrate** side menu.
3. Choose **Create Workflow** (Figure 1)

![A screenshot to create a workflow for the Migration hub console](/images/blog-3/Picture1v2.png)

<div style="text-align:center;">Figure 1: Create Workflow</div>

4. Select the **Import virtual machine images to AWS** template (Figure 2) and choose **Next**

![A screenshot to select the template that import a virtual machine image to AWS](/images/blog-3/Picture2-18.png)

<div style="text-align:center;">Figure 2: Select the import virtual machine template</div>

5. On the **Configure your workflow** page, enter a **Name** for the workflow, and optionally enter a **Description**.
6. In the **Source environment configuration** section, populate the **Disk container** field, which is the S3 bucket where you stored your image from on premises. The name must conform to the requirements from the [Migration Hub Orchestrator documentation](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/import-vm-images.html#source-env-config-import-vm-images).
   
![A screenshot to populate the Disk container field](/images/blog-3/Picture3v2.png)

<div style="text-align:center;">Figure 3: Configure source environment</div>

7. In the **Target environment configuration** section, select the operating system and license for the virtual machines created with the resultant AMI. Choose **Windows Server BYOL without SQL Server**.
   
![A screenshot to select the target Operating system and application license](/images/blog-3/Picture4-14.png)

<div style="text-align:center;">Figure 4: Choose the licensing model</div>

8. Use the rest of the fields to further customize your AMI based on your requirements. These include the boot mode, [AWS Key Management Service](https://aws.amazon.com/kms/) (KMS) encryption key, tags and license specification (for business case analysis). You also have the option to leave these with their default values. Choose
9. On the **Review and submit** page, choose
    
After uploading an image and creating your workflow, it is ready to run by choosing **Run workflow**.

![A screenshot to run the  workflow for the Migration hub console](/images/blog-3/Picture5-15.png)

<div style="text-align:center;">Figure 5: Run Workflow</div>

## Managing license conversion properly

There are scenarios in which you will need to switch Amazon EC2 instances from the BYOL licensing model to license included and vice versa. These include (but are not limited to):

- Upgrading the operating system of the Amazon EC2 instance to Windows Server 2022, which is not eligible for BYOL, regardless of tenancy.
- Moving an Amazon EC2 instance off a dedicated host to run it on shared tenancy EC2, which is not eligible for BYOL.
- Moving an Amazon EC2 instance that is eligible for BYOL from shared tenancy to a dedicated host.
  
When you need to switch the licensing model of an Amazon EC2 instance, use the [License type conversion](https://docs.aws.amazon.com/license-manager/latest/userguide/license-conversion.html) feature in AWS License Manager. License type conversion lets you change the usage operation. See our guide for [eligible license types for Windows and SQL Server in License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-types-windows.html).

## Detecting configuration issues with AWS Config

[AWS Config](https://aws.amazon.com/config/) is a service that helps you assess, audit, and evaluate the configuration of your AWS resources. By leveraging a custom AWS Config Rule, you can detect potential license misconfiguration in instances running on dedicated hosts, saving unnecessary licensing costs.

The [aws-config-rules repository](https://github.com/awslabs/aws-config-rules) contains custom AWS Config Rules to deploy to your AWS account using the [AWS Config Rules Development Kit (RDK)](https://github.com/awslabs/aws-config-rdk). Use the custom AWS Config Rule called [EC2_INSTANCE_LICENSE_INCLUDED_DEDICATED_HOST](https://github.com/awslabs/aws-config-rules/tree/master/python/EC2_INSTANCE_LICENSE_INCLUDED_DEDICATED_HOST) to detect instances with license-included Windows Server (usage operation RunInstances:0002) running on Dedicated Hosts.

Use [AWS CloudShell](https://aws.amazon.com/cloudshell/) to run the RDK and test the AWS Config rules deployment. To install the custom rule, open CloudShell in the [AWS Console](https://aws.amazon.com/console/) in the desired AWS Region, and run the following commands:

```Bash
pip install rdk
rdk init
git clone https://github.com/awslabs/aws-config-rules
cd aws-config-rules/python
rdk deploy EC2_INSTANCE_LICENSE_INCLUDED_DEDICATED_HOST
```

Once the rule has completed deployment, view the rule in the [AWS Config console](https://console.aws.amazon.com/config/home). For instances with mis-configured licenses, either move them to Shared tenancy or follow the [License Conversion process](https://aws.amazon.com/vi/blogs/modernizing-with-aws/operating-byol-windows-server-workloads-effectively-on-aws/#manage-license) accordingly.

![A screenshot for the custom AWS config rule](/images/blog-3/Picture6-10.png)

<div style="text-align:center;">Figure 6: Custom Config rule</div>

## Understanding CUR data for BYOL instances

[AWS Cost and Usage Reports (CUR)](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) contains the most comprehensive set of cost and usage data available. Use [Amazon Athena](https://aws.amazon.com/athena/) to [query your CUR data](https://docs.aws.amazon.com/cur/latest/userguide/cur-query-athena.html). The following query shows the licenses your instances are being billed for:

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

Based on the results of the above Query, the line_item_operation field shows what you’re being [billed](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-info-fields.html#billing-info) for.
 
![A screenshot for the output of the AWS CUR query](/images/blog-3/Image-from-iOS.jpg)

<div style="text-align:center;">Figure 7: AWS CUR output</div>

## Conclusion

Implementing BYOL for Windows Server workloads on AWS successfully, requires careful attention to license eligibility, configuration, and ongoing management. By understanding the key requirements – from license purchase dates and Windows Server versions to proper usage operation codes on dedicated hosts – organizations can effectively reduce their cloud infrastructure costs while maintaining compliance. Success depends on three key elements:

1. Proper license evaluation – identifying eligible licenses based on purchase date and Windows Server version
2. Accurate configuration – ensuring correct usage operation codes to avoid double-billing on dedicated hosts
3. Ongoing monitoring – maintaining regular assessment of usage and costs

By following these practices, organizations can optimize their Windows Server deployment costs while maintaining licensing compliance on AWS.

Ready to start optimizing your Windows Server costs on AWS? Request an [AWS Optimization and Licensing Assessment](https://aws.amazon.com/optimization-and-licensing-assessment/) to begin evaluating your licensing opportunities and potential cost savings.

---

AWS has significantly more services, and more features within those services, than any other cloud provider, making it faster, easier, and more cost effective to move your existing applications to the cloud and build nearly anything you can imagine. Give your Microsoft applications the infrastructure they need to drive the business outcomes you want. Visit our [.NET on AWS](https://aws.amazon.com/blogs/dotnet/) and [AWS Database](https://aws.amazon.com/blogs/database/) blogs for additional guidance and options for your Microsoft workloads. [Contact us](https://pages.awscloud.com/MAP-windows-contact-us.html) to start your migration and modernization journey today.

TAGS: [Amazon EC2](https://aws.amazon.com/blogs/modernizing-with-aws/tag/amazon-ec2/), [AWS License Manager](https://aws.amazon.com/blogs/modernizing-with-aws/tag/aws-license-manager/), [Cost Savings](https://aws.amazon.com/blogs/modernizing-with-aws/tag/cost-savings/), [Microsoft](https://aws.amazon.com/blogs/modernizing-with-aws/tag/microsoft/), [Windows On AWS](https://aws.amazon.com/blogs/modernizing-with-aws/tag/windows-on-aws/), [Windows Server](https://aws.amazon.com/blogs/modernizing-with-aws/tag/windows-server/)

<div style="display: flex; align-items: center;">
  <img src="/images/blog-3/aaalzand-400.jpg" alt="Ali Alzand" style="width:120px; border-radius:8px; margin-right:16px;">
  <p>
    <strong>Ali Alzand</strong><br>
    Ali is a Microsoft Specialist Solutions Architect at Amazon Web Services who helps global customers unlock the power of the cloud by migrating, modernizing, and optimizing their Microsoft workloads. He specializes in cloud operations — leveraging AWS services like Systems Manager, Amazon EC2 Windows, and EC2 Image Builder to drive cloud transformation. Outside of work, Ali enjoys exploring the outdoors, firing up the grill on weekends for barbecue with friends, and sampling all the eclectic food has to offer.
  </p>
</div>

<div style="display: flex; align-items: center; margin-bottom: 24px;">
  <img src="/images/blog-3/Screenshot-2025-06-30-at-8.26.18-AM.png" alt="Jon Madison" style="width:120px; border-radius:8px; margin-right:16px;">
  <p>
    <strong>Jon Madison</strong><br>
    Jon Madison is a Pr. Delivery Consultant on the AWS Professional Services (ProServe) Energy Team. He has a background in Cloud Infrastructure, Security, and DevOps, and is passionate about helping customers with cloud adoption and building scalable solutions and processes. In his free time Jon enjoys cooking, gaming, and spending time with his family and friends.
  </p>
</div>

<div style="display: flex; align-items: center;">
  <img src="/images/blog-3/MikeGupta.jpg" alt="Mike Gupta" style="width:120px; border-radius:8px; margin-right:16px;">
  <p>
    <strong>Mike Gupta</strong><br>
    Mike Gupta is a Senior Technical Account Manager at AWS based out of New York City. In his role, he provides strategic technical guidance to help customers use AWS best practices to plan and build solutions. He’s dedicated to empower customers to develop scalable, resilient, and cost-effective architectures. In his free time, Mike enjoys spending time with his wife and family, exploring local history and trying new restaurants.
  </p>
</div>
