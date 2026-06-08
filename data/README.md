# Data Directory

This directory is intended to store the raw and processed datasets for the KKBox customer churn prediction project. 

**Note: The full dataset is not included in this repository due to size limitations and licensing.**

## Dataset Details
According to the original project report:
- The raw dataset was sourced from the KKBox Customer Churn Prediction Challenge on Kaggle.
- The original compressed data was approximately **8.33GB**.
- Data sources included:
  - Member demographic data
  - Transaction records
  - User activity logs
- The final **preprocessed dataset** used for modeling consisted of **970,960 rows and 11 columns**.

## Expected Features
The preprocessed dataset (`processed/kkbox_processed.csv`) should contain the following columns:
1. `city`
2. `registered_via`
3. `payment_method`
4. `payment_plan_days`
5. `is_auto_renew`
6. `is_cancel`
7. `registration_day`
8. `transaction_day`
9. `membership_expire_day`
10. `last_play_day`
11. `is_churn` (Target Variable)

## Setup Instructions
To run the full end-to-end pipeline:
1. Create `raw/` and `processed/` folders inside this `data/` directory.
2. Download the compatible KKBox churn dataset from Kaggle.
3. Place the downloaded files into the `data/raw/` directory.
4. Run the data preprocessing script from the `src/` directory to generate the processed dataset.

**Warning:** Do not commit the raw or processed datasets to Git. They are ignored in the `.gitignore` file.
