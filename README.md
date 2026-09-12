# Insurance Analytics & Customer Insights

An end-to-end insurance analytics project using **Microsoft SQL Server, Python, NLP, and Power BI** to analyze policy performance, claims activity, customer demographics, and customer feedback.

> **Note:** This project uses fictional/sample insurance data and is intended for portfolio and educational purposes.

## Project Overview

This project transforms raw insurance and customer feedback data into interactive business intelligence dashboards. The analysis focuses on two areas:

1. **Insurance Performance** — premiums, coverage, claims, policies, and customer demographics.
2. **Customer Sentiment** — sentiment classification and topic discovery from customer reviews.

The goal was to demonstrate an end-to-end analytics workflow combining **SQL data analysis, Python-based NLP, and Power BI visualization** to identify actionable business and customer insights.

## Tech Stack

- **Microsoft SQL Server** — Data querying and analysis
- **Python** — Customer feedback analysis
- **Pandas** — Data cleaning and transformation
- **VADER** — Sentiment analysis
- **TF-IDF** — Text feature extraction
- **K-Means Clustering** — Customer feedback topic discovery
- **Silhouette Analysis** — Cluster evaluation
- **Power BI / DAX** — Data modeling, KPIs, and interactive dashboards
- **Excel** — Data storage and intermediate processing

## Dashboard 1: Insurance Overview

The **Insurance Overview Dashboard** provides an interactive view of insurance operations and financial performance.

### Key Metrics

- **$5.97M** Premium Amount
- **$600.33M** Coverage Amount
- **$16.90M** Claim Amount

### Analysis Includes

- Premium amount by policy type
- Claim status and claim amounts
- Active vs. inactive policies
- Claims by customer age group
- Customer demographics
- Policy and claim-level filtering

Interactive slicers allow users to investigate individual **policies, claims, and customers**.

<!-- Replace with your actual screenshot path -->
![Insurance Overview Dashboard](images/insurance-overview.png)

## Dashboard 2: Customer Sentiment Analysis

To expand the insurance analysis beyond operational metrics, I analyzed **97 customer reviews** using Natural Language Processing (NLP).

### Sentiment Analysis

I used **VADER Sentiment Analysis** to generate sentiment scores and classify each review as positive, neutral, or negative.

| Metric | Result |
|---|---:|
| Positive Reviews | **77.32%** |
| Negative Reviews | **12.37%** |
| Average Sentiment Score | **0.39** |

### Topic Discovery

Customer feedback was transformed using **TF-IDF vectorization** and grouped using **K-Means clustering**.

I evaluated multiple cluster sizes using **silhouette scores** and selected six clusters to balance statistical separation with business interpretability.

The resulting customer feedback topics were:

- Policy & Pricing
- Claims & Processes
- Digital Access & Coverage
- Customer Service
- Issue Resolution
- Overall Experience & Value

<!-- Replace with your actual screenshot path -->
![Customer Sentiment Dashboard](images/customer-sentiment.png)

## Key Insights

- **77.32%** of customer reviews were classified as positive.
- **Overall Experience & Value** had the highest average sentiment score at **0.78**.
- **Customer Service** and **Digital Access & Coverage** had the lowest average sentiment scores at **0.22**.
- Topic-level sentiment analysis highlighted potential opportunities to improve customer service and digital experiences.

## Project Workflow

```text
Insurance Data
     |
Microsoft SQL Server
     |
Data Analysis & Preparation
     |
     +----------------------+
     |                      |
Insurance Data        Customer Reviews
     |                      |
     |               Python / Pandas
     |                      |
     |              VADER Sentiment
     |                      |
     |              TF-IDF Vectorization
     |                      |
     |              K-Means Clustering
     |                      |
     +----------+-----------+
                |
             Power BI
                |
      Interactive Dashboards
```

## Repository Structure

```text
insurance-analytics/
│
├── data/
│   ├── insurance_data.csv
│   └── customer_feedback.xlsx
│
├── python/
│   └── sentiment_analysis.py
│
├── sql/
│   └── insurance_analysis.sql
│
├── powerbi/
│   └── insurance_dashboard.pbix
│
├── images/
│   ├── insurance-overview.png
│   └── customer-sentiment.png
│
└── README.md
```

## Skills Demonstrated

`SQL` `Python` `Pandas` `Power BI` `DAX` `NLP` `VADER` `TF-IDF` `K-Means Clustering` `Machine Learning` `Data Cleaning` `Data Visualization` `Sentiment Analysis` `Business Intelligence`
