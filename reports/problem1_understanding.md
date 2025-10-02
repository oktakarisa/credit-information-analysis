# Problem 1 – Understanding the Competition

## What kind of company is Home Credit?

1. The goal of consumer finance company Home Credit is to increase financial inclusion for people with little to no formal credit history. 

2. Due to inadequate documentation or borrowing histories, many people find it difficult to obtain loans, leaving them open to predatory lenders. 

3. This is addressed by Home Credit by providing secure and equitable lending experiences.  They use both conventional credit data and data from other sources, like transactional data and telco usage, to accomplish this successfully.

## What’s the main goal of the competition?

1. The competition challenges participants to predict how likely it is that a loan applicant will default on their repayment obligations. 

2. More specifically, the task is to predict the probability of the **TARGET variable** (default vs. no default) for each applicant using the provided dataset. 

3. Submissions are evaluated based on the Area Under the ROC Curve (AUC), which measures how well the predicted probabilities distinguish between repayers and defaulters.

## Why would the company benefit from these predictions?

Repayment ability predictions that are accurate have obvious business benefits:

 **1. Decrease danger:**  Home Credit can reduce the amount of money lost due to unpaid loans by more accurately identifying applicants who are at high risk of default.  

 **2. Increase financial inclusion:** The business can provide loans to more individuals who might otherwise be turned down by more confidently identifying trustworthy applicants, even those with little credit history.  

 **3. Improved loan arrangement:**  Home Credit can offer loans with better terms (principal, maturity, and repayment schedule) that raise the chance of successful repayment thanks to enhanced risk assessment.  

 **4. Sustainable growth:** By combining financial security with wider client inclusion, the company's profitability and the goal of empowering marginalized communities are supported.

---

### Dataset Preparation

For this stage:

- Download **application_train.csv** (the main dataset of loan applicants and repayment information).

- Download **HomeCredit_columns_description.csv** (the metadata file explaining each feature in the dataset).

- Ignore the other CSV files for now, as they are not needed in this early phase.

---

**Citation:**  
Anna Montoya, inversion, KirillOdintsov, and Martin Kotek. *Home Credit Default Risk.* https://kaggle.com/competitions/home-credit-default-risk, 2018. Kaggle.
