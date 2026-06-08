"""
Preprocessing script for the KKBox Customer Churn Prediction project.
This is a clean template based on the verified methodology.
Full reproduction requires the original KKBox dataset.

Expected input columns:
- city
- registered_via
- payment_method
- payment_plan_days
- is_auto_renew
- is_cancel
- registration_day
- transaction_day
- membership_expire_day
- last_play_day

Target column:
- is_churn
"""

import pandas as pd
import numpy as np

def load_data(file_path):
    """
    Loads the raw KKBox dataset.
    Note: The original dataset was described as an 8.33GB compressed file.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded dataset with shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Please download the KKBox dataset.")
        return None

def clean_data(df):
    """
    Perform data cleaning and transformation according to the report:
    - Handle missing values
    - Format dates
    - Encode categorical variables
    """
    # Placeholder for actual data cleaning logic
    # e.g., mapping categories, filling missing values
    print("Cleaning data...")
    return df

def feature_engineering(df):
    """
    Engineer features based on member data, transactions, and user activity logs.
    """
    # Placeholder for feature engineering
    print("Engineering features...")
    return df

def preprocess_pipeline(raw_data_path, processed_data_path):
    """
    Runs the full preprocessing pipeline.
    """
    df = load_data(raw_data_path)
    if df is not None:
        df_clean = clean_data(df)
        df_features = feature_engineering(df_clean)
        
        # Save processed data
        df_features.to_csv(processed_data_path, index=False)
        print(f"Processed dataset saved to {processed_data_path}")
        # Expected preprocessed dataset size in report: 970,960 rows and 11 columns
        print("Expected rows: ~970,960")

if __name__ == "__main__":
    raw_path = "../data/raw/train.csv" # Update as per Kaggle files
    processed_path = "../data/processed/kkbox_processed.csv"
    print("Running preprocessing scaffold...")
    preprocess_pipeline(raw_path, processed_path)
