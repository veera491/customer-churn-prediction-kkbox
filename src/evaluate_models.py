"""
Model evaluation script for the KKBox Customer Churn Prediction project.
Calculates accuracy, precision, recall, F1-score, ROC curve, and AUC score.
"""

import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report
import joblib

# The reported best results from the original study:
REPORTED_RESULTS = {
    'Logistic Regression': {'accuracy': 0.93, 'AUC': 0.89, 'precision': 0.77, 'recall': 0.43, 'f1': 0.55},
    'Naive Bayes': {'accuracy': 0.89, 'AUC': 0.85, 'precision': 0.45, 'recall': 0.57, 'f1': 0.50},
    'KNN': {'accuracy': 0.96, 'AUC': 0.89, 'precision': 0.85, 'recall': 0.71, 'f1': 0.77},
    'Random Forest': {'accuracy': 0.97, 'AUC': 0.97, 'precision': 0.89, 'recall': 0.78, 'f1': 0.83}
}

def evaluate_model(model, X_test, y_test, model_name):
    """
    Evaluate a trained model and print classification metrics.
    """
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else y_pred
    
    print(f"--- Evaluation for {model_name} ---")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred):.4f}")
    print(f"Recall: {recall_score(y_test, y_pred):.4f}")
    print(f"F1-score: {f1_score(y_test, y_pred):.4f}")
    print(f"AUC: {roc_auc_score(y_test, y_prob):.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

def main():
    print("This script provides the evaluation scaffold to compare reproduced models against the reported baselines.")
    print("\n--- Original Study Reported Baselines ---")
    df_results = pd.DataFrame(REPORTED_RESULTS).T
    print(df_results)
    
    print("\nBest Model: Random Forest achieved the best performance.")
    
    # Example logic to load and evaluate:
    # X_test, y_test = load_test_data()
    # model = joblib.load('../results/random_forest.joblib')
    # evaluate_model(model, X_test, y_test, 'Random Forest')

if __name__ == "__main__":
    main()
