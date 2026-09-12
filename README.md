# Insurance Analytics & Customer Insights

An end-to-end insurance analytics project using **Microsoft SQL Server, Python, NLP, and Power BI** to analyze insurance performance, claims activity, customer demographics, and customer feedback.

> **Note:** This project uses fictional/sample insurance data and was developed for portfolio and educational purposes.

## Project Overview

This project transforms raw insurance and customer feedback data into interactive business intelligence dashboards and customer sentiment insights.

The analysis consists of two primary components:

1. **Insurance Performance Analysis** — analyzes premiums, coverage, claims, policy status, policy types, and customer demographics.
2. **Customer Sentiment Analysis** — uses Natural Language Processing (NLP) to classify customer sentiment and identify common feedback topics.

The project demonstrates an end-to-end analytics workflow combining **Microsoft SQL Server for data analysis, Python for NLP and machine learning, and Power BI for interactive visualization and reporting**.

---

## Tech Stack

- **Microsoft SQL Server** — Data querying and analysis
- **Python** — Sentiment and topic analysis
- **Pandas** — Data cleaning and transformation
- **VADER** — Sentiment classification
- **TF-IDF** — Text feature extraction
- **K-Means Clustering** — Customer feedback topic discovery
- **Silhouette Analysis** — Cluster evaluation
- **Power BI / DAX** — Data modeling, KPIs, and dashboard development
- **Excel / CSV** — Data storage and processed outputs

---

## Insurance Overview Dashboard

The **Insurance Overview Dashboard** provides an interactive view of insurance operations, financial performance, policies, claims, and customer demographics.

### Key Metrics

| Metric | Value |
|---|---:|
| Premium Amount | **$5.97M** |
| Coverage Amount | **$600.33M** |
| Claim Amount | **$16.90M** |

### Analysis Includes

- Premium amount by policy type
- Claim status and claim amounts
- Active vs. inactive policies
- Claims by customer age group
- Customer demographics
- Policy, claim, and customer-level filtering

The dashboard uses interactive slicers to allow users to investigate individual **policies, claims, and customers**.

The complete dashboard can be viewed in:

`final dashboard/InsuranceDataAnalysis (1).pdf`

The Power BI project file is also included:

`final dashboard/InsuranceDataAnalysis.pbix`

---

## Customer Sentiment Analysis

To extend the insurance analysis beyond operational metrics, I analyzed **97 customer reviews** using Python and Natural Language Processing.

### Sentiment Analysis

I used **VADER Sentiment Analysis** to generate sentiment scores and classify each customer review as positive, neutral, or negative.

| Metric | Result |
|---|---:|
| Positive Reviews | **77.32%** |
| Negative Reviews | **12.37%** |
| Average Sentiment Score | **0.39** |

### Topic Discovery

I transformed customer feedback using **TF-IDF vectorization** and applied **K-Means clustering** to identify groups of similar reviews.

Multiple cluster sizes were evaluated using **silhouette analysis**, and six clusters were selected to balance cluster separation with business interpretability.

The six identified customer feedback topics were:

- **Policy & Pricing**
- **Claims & Processes**
- **Digital Access & Coverage**
- **Customer Service**
- **Issue Resolution**
- **Overall Experience & Value**

The complete Python analysis is available in:

`sentiment analysis/FeedbackAnalysis.py`

The processed sentiment dataset is available in:

`sentiment analysis/Insurance_Feedback_Analyzed.xlsx`

---

## Key Insights

- **77.32%** of customer reviews were classified as positive.
- **Overall Experience & Value** had the highest average sentiment score at **0.78**.
- **Customer Service** and **Digital Access & Coverage** had the lowest average sentiment scores at **0.22**.
- Topic-level sentiment analysis identified potential opportunities for improving **customer service and digital experiences**.
- Combining operational insurance metrics with customer feedback provides a more comprehensive view of both **business performance and customer experience**.

---

## Project Workflow

```text
                    Raw Data
                       |
          +------------+------------+
          |                         |
   Insurance Data            Customer Feedback
          |                         |
 Microsoft SQL Server          Python / Pandas
          |                         |
   Data Analysis             VADER Sentiment
          |                         |
          |                 TF-IDF Vectorization
          |                         |
          |                 K-Means Clustering
          |                         |
          +------------+------------+
                       |
                    Power BI
                       |
             Interactive Dashboards
                       |
                Business Insights
```

---

## Repository Structure

```text
Insurance-Analytics-Customer-Insights/
│
├── data/
│   ├── Insurance+Customer+Feedback.xlsx
│   └── InsuranceData.csv
│
├── final dashboard/
│   ├── InsuranceDataAnalysis (1).pdf
│   └── InsuranceDataAnalysis.pbix
│
├── sentiment analysis/
│   ├── FeedbackAnalysis.py
│   └── Insurance_Feedback_Analyzed.xlsx
│
└── README.md
```

### Folder Descriptions

**`data/`**  
Contains the original insurance and customer feedback datasets used for analysis.

**`final dashboard/`**  
Contains the final Power BI `.pbix` project and a PDF export for easy viewing without Power BI.

**`sentiment analysis/`**  
Contains the Python NLP analysis script and the processed Excel dataset containing sentiment scores, sentiment classifications, and customer feedback topics.

---

## Skills Demonstrated

`SQL` `Microsoft SQL Server` `Python` `Pandas` `Power BI` `DAX` `NLP` `VADER` `TF-IDF` `K-Means Clustering` `Silhouette Analysis` `Machine Learning` `Data Cleaning` `Data Visualization` `Sentiment Analysis` `Business Intelligence`
