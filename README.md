# Employee Attrition and Loss Prediction

## Project Overview
This project aims to predict employee attrition and estimate the expected salary loss for a company based on employee profiles. The solution combines classification models to predict attrition likelihood and regression models to predict future salary, thereby enabling proactive risk management and financial planning.

---

## Key Objectives
- Predict whether an employee is likely to stay or leave the organization.
- Estimate the future salary of employees based on features such as performance, tenure, and job level.
- Calculate the expected financial loss considering attrition probability and future salary estimates.

---

## Dataset
- Employee profile data including:
  - Performance Rating
  - Total Working Years
  - Job Level
  - OverTime Status
  - Marital Status
  - Monthly Income and other HR metrics

---

## Project Workflow
1. **Data Cleaning and Preprocessing**
   - Handled missing values
   - Label encoding for categorical features
   - Standardization for numerical features

2. **Model Building**
   - **Attrition Prediction (Classification Models)**:
     - Logistic Regression
     - Random Forest Classifier with SMOTE (best performing)
   - **Future Salary Prediction (Regression Models)**:
     - Ridge Regression
     - Random Forest Regressor

3. **Evaluation Metrics**
   - Classification: Accuracy, Precision, Recall, F1-Score
   - Regression: R² Score, RMSE, MAPE

4. **Business Metrics**
   - Expected Salary Loss Calculation based on attrition probability

---

## Final Results
- **Attrition Prediction Accuracy (Random Forest + SMOTE)**: 93.11%
- **Salary Prediction Accuracy (Ridge and Random Forest Regressor)**: R² = 0.994
- **Total Expected Salary Loss (for \"Likely to Stay\" employees)**: INR 860,099

---


