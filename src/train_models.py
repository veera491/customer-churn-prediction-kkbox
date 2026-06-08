"""
Model training script for the KKBox Customer Churn Prediction project.
Compares supervised models: Logistic Regression, Naive Bayes, KNN, Random Forest.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib

def load_processed_data(file_path):
    """Load the preprocessed 970,960 row dataset."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: Processed data not found at {file_path}")
        return None

def train_models(X_train, y_train):
    """
    Train Logistic Regression, Naive Bayes, KNN, and Random Forest models.
    """
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000),
        'Naive Bayes': GaussianNB(),
        'KNN': KNeighborsClassifier(n_neighbors=5),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42)
    }
    
    trained_models = {}
    for name, model in models.items():
        print(f"Training {name}...")
        model.fit(X_train, y_train)
        trained_models[name] = model
        
    return trained_models

def main():
    processed_data_path = "../data/processed/kkbox_processed.csv"
    df = load_processed_data(processed_data_path)
    
    if df is not None:
        X = df.drop(columns=['is_churn'])
        y = df['is_churn']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        trained_models = train_models(X_train, y_train)
        
        # Save models for evaluation
        for name, model in trained_models.items():
            model_filename = f"../results/{name.replace(' ', '_').lower()}.joblib"
            joblib.dump(model, model_filename)
            print(f"Saved model: {model_filename}")

if __name__ == "__main__":
    print("Running model training scaffold...")
    main()
