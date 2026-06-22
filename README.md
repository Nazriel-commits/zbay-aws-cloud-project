# ZBay - AWS Cloud Infrastructure Project

## Overview
ZBay is a fictional e-commerce startup that provides an online platform for local artisans to sell handmade products (jewelry, home decor, organic personal care items).  

This project demonstrates the design and deployment of a **highly available, scalable, and secure cloud infrastructure** on AWS.

## Video Presentation
[Watch the full walkthrough on YouTube](https://youtu.be/fxPhxQBbFCI)

## Architecture Overview

| AWS Service | Purpose |
|-------------|---------|
| **VPC** | Isolated network with public/private subnets across 2 AZs |
| **EC2** | Hosts the web application (t3a.medium instance) |
| **RDS (MySQL)** | Managed database for products, users, orders |
| **EBS** | 30 GB persistent storage for application data and logs |
| **Application Load Balancer (ALB)** | Distributes traffic across multiple EC2 instances |
| **Auto Scaling Group** | Scales instances based on CPU usage (2–6 instances) |
| **Lambda** | Email validation function integrated with web form |
| **CloudWatch** | Monitoring, dashboards, and scaling triggers |
| **IAM** | Secure role-based access control |

## Key Features Implemented

- Multi-AZ VPC with public/private subnets and NAT Gateway
- EC2 instance with termination protection and CloudWatch monitoring
- Serverless email validation via AWS Lambda + PHP web form
- 30 GB EBS volume attached, formatted, and snapshotted
- RDS MySQL database integrated with EC2 web server
- Application Load Balancer + Auto Scaling Group (2–6 instances)
- Target Tracking Scaling Policy based on CPU utilization (60% threshold)

## Estimated Monthly Cost
~$160/month (breakdown in report)
