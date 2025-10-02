# Problem 3 – Defining Issues (Questions to Explore)

## Purpose
Based on the dataset overview (see `reports/problem2_summary.md`), we propose guiding questions and hypotheses for the next analysis step. Good questions help focus EDA on meaningful insights.

---

## Guiding Questions

1. **Does income level affect default risk?**  
   Columns: `AMT_INCOME_TOTAL`, `TARGET`  
   Hypothesis: Lower income may increase default probability.  

2. **Does loan amount or credit size relate to default?**  
   Columns: `AMT_CREDIT`, `AMT_ANNUITY`, `TARGET`  
   Hypothesis: Higher credit relative to income increases risk.  

3. **Does age correlate with default probability?**  
   Columns: `DAYS_BIRTH`, `TARGET`  
   Hypothesis: Younger or older applicants may differ in repayment ability.  

4. **Are certain contract types more likely to default?**  
   Columns: `NAME_CONTRACT_TYPE`, `TARGET`  
   Hypothesis: Product type influences default likelihood.  

5. **Does employment or income type affect default?**  
   Columns: `NAME_INCOME_TYPE`, `DAYS_EMPLOYED`, `TARGET`  
   Hypothesis: Stable employment → lower default risk.  

6. **Do external scores (EXT_SOURCE_1/2/3) predict default?**  
   Columns: `EXT_SOURCE_1/2/3`, `TARGET`  
   Hypothesis: Higher scores → lower default probability.  

7. **How do missing values distribute across classes?**  
   Columns: All features + `TARGET`  
   Hypothesis: Missingness may differ by default status.  

8. **Does family or housing status affect default?**  
   Columns: `NAME_FAMILY_STATUS`, `CNT_FAM_MEMBERS`, `TARGET`  
   Hypothesis: Family size or living arrangement impacts repayment.  

9. **Are certain occupations or education levels riskier?**  
   Columns: `OCCUPATION_TYPE`, `NAME_EDUCATION_TYPE`, `TARGET`  
   Hypothesis: Occupation/education link to repayment stability.  

10. **Does the ratio of credit to income affect default?**  
    Columns: `AMT_CREDIT`, `AMT_INCOME_TOTAL`, `TARGET`  
    Hypothesis: Higher ratios indicate greater risk.  

---

## Prioritization Table

| ID | Question (short)              | Priority | Selected |
|----|-------------------------------|----------|----------|
| 1  | Income vs default             | High     |          |
| 2  | Credit amount vs default      | High     |          |
| 3  | Age vs default                | Medium   |          |
| 4  | Contract type vs default      | Medium   |          |
| 5  | Employment & income type      | Medium   |          |
| 6  | External scores vs default    | High     |          |
| 7  | Missingness patterns          | High     |          |
| 8  | Family / housing              | Low      |          |
| 9  | Occupation / education        | Low      |          |
| 10 | Credit/Income ratio           | High     |          |

---

## Next Steps (Problem 4)
1. Select at least 5 high/medium priority questions.  
2. For each, create tables and plots in `src/problem4_data_exploration.py`.  
3. Save results as:  
   - Plots → `plots/`  
   - Tables → `reports/` (CSV)  
   - Interpretations → `reports/problem4_findings.md`  
4. Add new questions if they arise during EDA.  
