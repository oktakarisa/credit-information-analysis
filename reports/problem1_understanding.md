# Problem 1: Understanding the Competition and Data

## Competition Outline

This assignment is based on a credit risk prediction competition. The main objective is to analyze a dataset containing customer credit information and identify factors that influence the likelihood of default. The project involves:

- Understanding the dataset structure and variables
- Identifying and addressing data quality issues
- Exploring relationships between features and the target variable (default)
- Summarizing findings and proposing actionable insights

## Data Appearance & Understanding

The dataset contains various features related to customer demographics, financial status, and credit history. Typical columns include:

- **ID**: Unique customer identifier
- **Age**: Customer age
- **Income**: Annual income
- **Credit Amount**: Amount of credit granted
- **Contract Type**: Type of credit contract
- **Target**: Default indicator (binary)

A sample of the data is available in the `data/` directory. For a detailed summary of columns, missing values, and data types, refer to:
- `reports/problem2_summary.md`
- `reports/problem2_missing_values.csv`

## Setting Issues

During analysis, several issues were identified:

- **Missing Values**: Some columns contain missing or incomplete data.
- **Data Types**: Certain columns may require type conversion for proper analysis.
- **Outliers**: Extreme values in income, age, or credit amount may affect results.
- **Imbalanced Target**: The default indicator may be imbalanced, impacting model performance.

These issues are documented in `reports/problem3_define_issues.md` and explored in the EDA notebook.

## Data Search & Exploration

Data exploration was performed using:

- **Jupyter Notebook (`notebooks/credit_eda.ipynb`)**: Interactive analysis of distributions, correlations, and relationships.
- **Scripts in `src/`**: Automated data overview, missing value analysis, and feature engineering.
- **Visualizations in `plots/`**: Key plots for target distribution, age vs default, contract type vs default, correlation heatmap, credit amount vs target, and income vs target.

---

*This document summarizes the competition outline, data appearance, identified issues, and data search/exploration process for the Credit Information Analysis assignment.*
