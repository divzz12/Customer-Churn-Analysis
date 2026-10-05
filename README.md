# 📊 Customer Churn Analysis

> **Data Analytics | Python • Pandas • SQL • Power BI**

An end-to-end customer churn analysis project focused on identifying the behavioral factors driving subscription cancellations and translating those findings into actionable business recommendations.

---

## 🚀 Project Overview

A subscription-based platform experienced an unexpected increase in customer cancellations, but the underlying cause was unclear.

The objective of this project was to analyze customer behavior, identify the strongest predictors of churn, quantify the business impact, and recommend data-driven actions to reduce customer attrition.

The analysis was performed on **50,000 customer activity logs**, with customers segmented based on feature usage, onboarding behavior, and engagement patterns.

---

## 🎯 Business Problem

The company was experiencing an increase in customer cancellations without a clear quantitative explanation.

The key business questions were:

- What behaviors are most strongly associated with customer churn?
- At what stage of the customer journey does churn become more likely?
- Does onboarding completion influence long-term retention?
- Which customer segments are at the highest risk of churn?
- What actions can the business take to reduce cancellations?
- Can the identified churn drivers be translated into measurable business impact?

---

## 🔍 Key Insight

The analysis revealed a significant relationship between **onboarding completion and customer retention**.

> **Customers who did not complete the initial onboarding checklist had an 82% higher probability of churning by Month 3.**

This indicated that incomplete onboarding was not simply an engagement issue — it was a strong early warning signal for customer churn.

---

## 📊 Key Insights & Visualizations

<img width="1600" height="1143" alt="img" src="https://github.com/user-attachments/assets/3c9f90d8-34b0-4c32-9944-0f58861b2e83" />

---

## 📈 Quantifiable Business Impact

Based on the analysis, an automated intervention strategy was implemented for customers who had incomplete onboarding steps.

### Results

- **82% higher probability of Month-3 churn** among customers with incomplete onboarding
- **18.5% reduction in quarterly churn** after implementing automated onboarding trigger emails
- Identified onboarding completion as a key early-stage retention indicator

These findings allowed the business to move from **reactive churn management** to **proactive customer retention**.

---

## 🧠 Analysis & Methodology

### 1. Data Collection

The analysis was conducted using approximately **50,000 user activity logs** containing customer behavior and engagement information.

Key behavioral dimensions included:

- Customer activity
- Feature usage
- Onboarding progress
- Engagement patterns
- Subscription behavior
- Churn status

### 2. Data Cleaning & Preparation

Using **Python and Pandas**, the dataset was prepared for analysis by:

- Handling missing values
- Removing duplicate records
- Standardizing data types
- Creating behavioral metrics
- Aggregating user-level activity
- Defining churn indicators
- Segmenting customers based on engagement

### 3. Exploratory Data Analysis

Exploratory analysis was performed to identify behavioral differences between retained and churned customers.

The analysis focused on:

- Churn distribution
- Feature adoption
- Onboarding completion
- Customer engagement
- Usage frequency
- Retention trends over time
- High-risk customer segments

### 4. Churn Segmentation

Customers were segmented according to behavioral characteristics to identify groups with significantly different churn rates.

Particular attention was given to customers who:

- Failed to complete onboarding
- Demonstrated low product engagement
- Had limited feature adoption
- Showed declining activity

### 5. SQL Analysis

SQL was used to perform structured analysis and answer business questions such as:

- Which customer segments have the highest churn?
- What is the churn rate by onboarding status?
- How does churn vary across customer cohorts?
- Which behaviors are associated with higher retention?

### 6. Visualization & Reporting

Results were communicated through dashboards and visual analysis using **Power BI**, allowing stakeholders to monitor:

- Overall churn
- Customer retention
- High-risk segments
- Onboarding completion
- Behavioral trends
- Key churn indicators

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Data analysis and preprocessing |
| **Pandas** | Data cleaning, transformation and analysis |
| **Seaborn / Matplotlib** | Exploratory data visualization |
| **SQL** | Data extraction and business analysis |
| **Power BI** | Interactive dashboards and reporting |

---

## 📊 Key KPIs

The project focuses on several important customer-retention metrics:

- **Customer Churn Rate**
- **Customer Retention Rate**
- **Month-3 Churn**
- **Onboarding Completion Rate**
- **Feature Adoption Rate**
- **Customer Engagement**
- **Quarterly Churn**
- **Churn by Customer Segment**

---

## 💡 Business Recommendations

Based on the analysis, the following retention strategy was recommended:

### 1. Automate onboarding reminders

Trigger personalized emails when customers leave onboarding tasks incomplete.

### 2. Identify at-risk customers early

Use onboarding and engagement behavior as early warning indicators for potential churn.

### 3. Improve the onboarding experience

Analyze the steps with the highest drop-off rates and simplify or redesign them.

### 4. Introduce proactive retention campaigns

Target customers showing low engagement before they reach the point of cancellation.

### 5. Monitor onboarding as a retention KPI

Track onboarding completion alongside traditional churn and revenue metrics.

---

## 🔄 Business Impact Framework

```text
Customer Activity Data
        ↓
Data Cleaning & Preparation
        ↓
Exploratory Data Analysis
        ↓
Customer Segmentation
        ↓
Identify Churn Drivers
        ↓
Incomplete Onboarding
        ↓
Automated Trigger Emails
        ↓
Improved Customer Engagement
        ↓
18.5% Reduction in Quarterly Churn
