# Reproducibility Notes

**Important Statement:**
This repository is cleaned for portfolio presentation. Full experimental reproduction requires the original KKBox dataset and an aligned preprocessing pipeline.

## Notebook Status
The provided Jupyter notebook (`legacy_notebook_needs_review.ipynb`) **requires reconciliation**. 
During the codebase audit, it was noted that the uploaded notebook references `diabetes_data_upload.csv`, indicating a mismatch with the core KKBox dataset methodology outlined in the project report.

Because of this mismatch:
- The notebook has been placed in the `notebooks/` directory under a legacy name.
- It should not be considered the definitive, end-to-end reproducible pipeline for the KKBox experiment.
- The **project report** (`reports/Churn_Project_Report.pdf`) remains the authoritative source for the experimental design, features, and model results.

## Required Data Files
To fully reproduce the original KKBox experiment, you must acquire the official dataset from the Kaggle "KKBox's Churn Prediction Challenge". 

Required data files to be placed in `data/raw/` typically include:
- `train.csv` (or equivalent member data)
- `transactions.csv`
- `user_logs.csv`

The pipeline expects these files to be preprocessed into a single dataset containing exactly **970,960 rows and 11 columns**, as documented in the methodology.

## Source of Results
The results presented in the README and methodology summaries (Accuracy, AUC, Precision, Recall, F1-scores) are transcribed directly from the verified `Churn_Project_Report.pdf`. 

## Fixes Required for Exact Reproduction
Before exact reproduction can be achieved:
1. **Data Integration:** The raw KKBox datasets must be downloaded and properly merged based on user IDs.
2. **Notebook Reconciliation:** A new notebook or execution script must be developed that correctly references the KKBox data paths instead of unrelated datasets.
3. **Pipeline Alignment:** The data cleaning and feature engineering steps outlined in `src/preprocessing.py` must be fully implemented to match the exact transformations described in the project report.
