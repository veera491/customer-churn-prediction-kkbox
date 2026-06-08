# Customer Churn Prediction in Music Streaming

## Overview
This project predicts customer churn in the music streaming domain using the KKBox churn dataset. It compares supervised machine learning models, including Logistic Regression, Naive Bayes, K-Nearest Neighbors (KNN), and Random Forest, to identify the best-performing approach for identifying users at risk of canceling their subscriptions.

**Note:** The available notebook requires reconciliation with the KKBox dataset pipeline. The project report is the authoritative source for the KKBox churn experiment.

## Problem Statement
Customer churn directly affects subscription-based businesses, impacting retention and revenue. The goal is to identify whether a customer is likely to churn using historical user demographic, transaction, and activity data, allowing for proactive retention strategies.

## Project Objectives
- Review churn prediction research within the music streaming domain.
- Analyze the KKBox customer churn data.
- Preprocess and transform customer, transaction, and activity features.
- Train multiple supervised machine learning models.
- Evaluate model performance using standard classification metrics.
- Select the best-performing model based on comparative analysis.

## Dataset
- **Source:** KKBox/Kaggle churn dataset.
- **Original Size:** Described as an 8.33GB compressed dataset.
- **Data Sources:** Member data, transactions, and user activity logs.
- **Preprocessed Data:** The final modeled dataset contained 970,960 rows and 11 columns.
- **Availability:** Dataset files are not included in this repository due to size and licensing constraints. 
- Please see `data/README.md` for setup instructions.

## Final Features
The models utilized the following preprocessed attributes:
- `city`
- `registered_via`
- `payment_method`
- `payment_plan_days`
- `is_auto_renew`
- `is_cancel`
- `registration_day`
- `transaction_day`
- `membership_expire_day`
- `last_play_day`
- `is_churn` (Target Variable)

## Methodology
The experimental framework consists of the following steps:
1. Literature Review
2. Data Acquisition
3. Data Preprocessing
4. Exploratory Data Analysis
5. Model Training
6. Model Evaluation
7. Model Comparison

## Exploratory Data Analysis
Key EDA steps included:
- Data type analysis across the different data sources.
- Correlation heatmap generation to understand feature relationships.
- General feature understanding and profiling.
- Analysis of the churn target distribution (where available).

## Models Compared
- Logistic Regression
- Naive Bayes
- K-Nearest Neighbors (KNN)
- Random Forest

## Results

| Model | Accuracy | AUC | Precision | Recall | F1-score |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.93 | 0.89 | 0.77 | 0.43 | 0.55 |
| Naive Bayes | 0.89 | 0.85 | 0.45 | 0.57 | 0.50 |
| KNN | 0.96 | 0.89 | 0.85 | 0.71 | 0.77 |
| Random Forest | 0.97 | 0.97 | 0.89 | 0.78 | 0.83 |

**Note:** Random Forest achieved the strongest overall performance with 0.97 accuracy and 0.97 AUC.



## How to Run

1. **Create a virtual environment:**
```bash
python -m venv .venv
```

2. **Activate the environment:**
For macOS/Linux:
```bash
source .venv/bin/activate
```
For Windows:
```bash
.venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the Jupyter Notebook:**
```bash
jupyter notebook notebooks/legacy_notebook_needs_review.ipynb
```

**Important:** The full dataset is not included. Exact reproduction requires compatible KKBox files placed under `data/raw/` and may require path updates within the code.

## Project Structure
```text
customer-churn-prediction-kkbox-clean/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── notebooks/
│   └── legacy_notebook_needs_review.ipynb
├── src/
│   ├── preprocessing.py
│   ├── train_models.py
│   ├── evaluate_models.py
│   └── utils.py
├── reports/
│   └── Churn_Project_Report.pdf
├── results/
│   ├── README.md
│   └── figures/
├── data/
│   └── README.md
└── docs/
    ├── methodology_summary.md
    └── reproducibility_notes.md
```

## My Contribution
This repository is a portfolio-cleaned version of the academic project materials available to me. Contribution details should be verified before using strong ownership language. 
- Worked on notebook-based ML experimentation and model comparison.
- Performed preprocessing/EDA and trained classification models.
- Evaluated Logistic Regression, Naive Bayes, KNN, and Random Forest using accuracy, precision, recall, F1-score, ROC, and AUC.
- Documented findings and model comparison.


## Limitations
- Dataset not included due to size/licensing.
- Full reproduction requires original KKBox files.
- Music streaming churn studies are less common than telecom churn.
- Only four supervised ML models were compared.
- No deep learning models were implemented.
- No production deployment.
- Notebook reproducibility must be verified if dataset paths are incomplete or mismatched.

## Future Work
- Add XGBoost/LightGBM.
- Add deep learning baselines such as ANN/LSTM.
- Add feature importance and SHAP.
- Add Streamlit dashboard.
- Add deployment as a simple web demo.
- Add drift monitoring for changing customer behavior.
