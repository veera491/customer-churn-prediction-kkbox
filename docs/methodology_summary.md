# Methodology Summary

## Problem Statement
Customer churn is a critical issue that directly affects the revenue and growth of subscription-based businesses, particularly in the music streaming domain. The goal of this project is to identify whether a customer is likely to churn using historical user, transaction, and activity data. 

## Churn Prediction Motivation
Predicting churn allows companies to proactively implement retention strategies. By accurately identifying at-risk customers, a music streaming service can offer targeted incentives, improve user satisfaction, and ultimately reduce revenue loss.

## Literature Review Summary
Extensive research exists on customer churn, primarily focused on the telecommunications and banking sectors. However, churn prediction in the music streaming domain presents unique challenges due to differences in user engagement patterns and subscription models. This project builds upon established supervised machine learning techniques to address this specific domain.

## Dataset Summary
The project utilizes the KKBox customer churn dataset from Kaggle. The original compressed dataset was 8.33GB, containing data across three main sources:
- **Member Data:** Demographic information and registration details.
- **Transactions:** Payment histories, plans, and subscription renewals.
- **User Activity Logs:** Daily listening behaviors.

## Data Preprocessing
Preprocessing involved:
- Handling missing values and formatting dates.
- Extracting relevant time-based features (e.g., membership expiration, last play date).
- Merging disparate data sources into a single coherent structure.
- The final preprocessed dataset consisted of **970,960 rows and 11 columns**, ready for modeling.

## Exploratory Data Analysis (EDA)
EDA focused on understanding feature distributions and correlations:
- Analyzed data types across member, transaction, and log features.
- Generated a correlation heatmap to identify relationships between numerical features.
- Investigated the class distribution of the target variable (`is_churn`).

## Framework
The experimental framework followed a standard machine learning pipeline: Data Acquisition -> Data Preprocessing & Cleaning -> Exploratory Data Analysis -> Feature Selection -> Model Training -> Model Evaluation -> Result Comparison.

## Model Training
Four supervised machine learning classification algorithms were implemented and trained on the preprocessed dataset:
1. Logistic Regression
2. Naive Bayes
3. K-Nearest Neighbors (KNN)
4. Random Forest

## Model Evaluation
Models were evaluated using a suite of standard classification metrics to handle potential class imbalances and provide a comprehensive performance overview:
- Accuracy
- Precision
- Recall
- F1-score
- ROC Curve and AUC Score
- Confusion Matrix

## Results
Random Forest achieved the best overall performance, significantly outperforming other models in key metrics:
- **Logistic Regression:** Accuracy 0.93, AUC 0.89, Precision 0.77, Recall 0.43, F1-score 0.55
- **Naive Bayes:** Accuracy 0.89, AUC 0.85, Precision 0.45, Recall 0.57, F1-score 0.50
- **KNN:** Accuracy 0.96, AUC 0.89, Precision 0.85, Recall 0.71, F1-score 0.77
- **Random Forest:** Accuracy 0.97, AUC 0.97, Precision 0.89, Recall 0.78, F1-score 0.83

## Limitations
- **Data Availability:** The complete dataset is excessively large (8.33GB compressed) and is not included in the repository due to size and licensing constraints.
- **Domain Focus:** Music streaming churn studies are less prevalent than telecom churn, meaning fewer direct baselines exist.
- **Model Scope:** Only four supervised machine learning models were compared.
- **Advanced Techniques:** No deep learning models (e.g., ANN, LSTM) were implemented in this iteration.
- **Deployment:** The project focused on offline evaluation; there is no production deployment.

## Future Work
- Implement advanced ensemble methods such as XGBoost or LightGBM.
- Explore deep learning baselines (ANN, LSTM) for sequential user log data.
- Incorporate feature importance analysis and SHAP values for model interpretability.
- Develop a Streamlit dashboard for interactive result visualization.
- Deploy a simple web demo to showcase real-time prediction capabilities.
- Integrate drift monitoring to account for changing customer behavior over time.
