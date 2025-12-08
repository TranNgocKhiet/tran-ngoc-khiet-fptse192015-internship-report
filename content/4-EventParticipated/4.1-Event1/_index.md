---
title: "Event 1"
weight: 1
chapter: false
pre: " <b> 4.1. </b> "
---

# Workshop Report: AWS Cloud Mastery Series #1 — AI/ML/GenAI on AWS

**Date:** Saturday, November 15, 2025  
**Time:** 8:30 AM – 12:00 PM  
**Location:** Bitexco Financial Tower, Ho Chi Minh City  
**Host:** Kha Van  
**Attendees:** 348 participants

## Overview

The first session of the AWS Cloud Mastery Series introduced modern machine learning and generative AI approaches on AWS, with a focus on practical applications and hands-on demonstrations. The workshop covered both SageMaker for traditional ML workflows and Amazon Bedrock for building with foundation models.

## Session Breakdown

### 8:30 – 9:00 AM | Welcome & Introduction

The session opened with participant registration and networking, followed by an overview of the AI/ML landscape in Vietnam. The organizers set expectations for the day's learning objectives and conducted an ice-breaker activity to encourage collaboration among the 348 attendees.

### 9:00 – 10:30 AM | AWS AI/ML Services Overview

This segment introduced Amazon SageMaker as a comprehensive end-to-end ML platform:

- **Data Preparation & Labeling:** Techniques for preparing datasets and labeling for supervised learning
- **Model Training & Tuning:** Hyperparameter optimization and AutoML capabilities
- **Deployment:** Moving trained models to production with integrated MLOps support
- **Live Demo:** A hands-on walkthrough of SageMaker Studio, showing how to launch experiments and monitor training jobs

Key takeaway: SageMaker eliminates the need to manage underlying infrastructure while providing full control over model training and deployment.

### 10:30 – 10:45 AM | Coffee Break

### 10:45 AM – 12:00 PM | Generative AI with Amazon Bedrock

The second half focused on building with foundation models using Amazon Bedrock:

#### Foundation Models Overview
- **Claude, Llama, Titan Comparison:** Different models for different use cases (reasoning, creative, multilingual)
- **Model Selection Guide:** How to choose the right model based on latency, cost, and accuracy requirements

#### Prompt Engineering Techniques
- **Chain-of-Thought Reasoning:** Breaking down complex problems into step-by-step workflows
- **Few-Shot Learning:** Using examples to guide model behavior
- **Advanced Prompting:** Patterns for extracting structured data and controlling output format

#### Retrieval-Augmented Generation (RAG)
- **Architecture & Integration:** Connecting external knowledge bases to Bedrock
- **Knowledge Base Integration:** Keeping models up-to-date with proprietary data
- **Reducing Hallucinations:** Using retrieval to ground model responses in facts

#### Bedrock Agents
- **Multi-Step Workflows:** Automating complex business processes
- **Tool Integration:** Connecting models to databases, APIs, and other services
- **Error Handling:** Graceful degradation and retry logic

#### Safety & Compliance
- **Guardrails:** AWS's content filtering and safety mechanisms
- **Output Filtering:** Preventing harmful or inappropriate responses

#### Live Demo: Building a Generative AI Chatbot
The instructors demonstrated a complete RAG-powered chatbot on Bedrock, showing:
1. Document upload and knowledge base indexing
2. Query processing with retrieval
3. Model inference with guardrails applied
4. Real-time response generation

## Personal Reflections

### What I Learned

The workshop clarified the distinction between traditional ML (SageMaker) and generative AI (Bedrock). Traditional ML remains essential for classification, regression, and time-series forecasting, while Bedrock excels at text understanding, generation, and reasoning tasks.

The practical emphasis on prompt engineering and RAG resonated particularly—these techniques are immediately applicable and require no machine learning expertise to implement.

### Key Insights

1. **Foundation models are production-ready:** AWS has invested heavily in security, compliance, and scaling for enterprise workloads.
2. **RAG is essential for enterprise AI:** Organizations cannot rely on foundation models alone; knowledge integration is critical for accuracy.
3. **Prompt engineering is a real skill:** Well-crafted prompts and few-shot examples can dramatically improve model output quality.
4. **Vietnam's AI landscape is growing:** With 348 participants, there's clear momentum in the local AI community.

### Next Steps

- Experiment with Bedrock's prompt playground for internal projects
- Design a RAG architecture for our team's knowledge base
- Evaluate which use cases benefit from foundation models vs. traditional ML
- Consider AWS's SageMaker Canvas for low-code model building

## Some pictures from the event

![event-picture-1](/images/event-1/IMG_20251115_100905.jpg)
![event-picture-2](/images/event-1/IMG_20251115_101516%20(2).jpg)

> This workshop was an excellent foundation for understanding modern AI on AWS. The combination of theory, live demos, and hands-on exploration created a comprehensive introduction to both traditional ML and generative AI workflows.
