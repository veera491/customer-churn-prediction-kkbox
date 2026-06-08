# Results Directory

This directory stores the generated models and evaluation figures for the KKBox Customer Churn Prediction project.

**Note: Result figures and metrics can be regenerated when the compatible dataset is available.**

## Expected Outputs
When the full pipeline is executed with the original dataset, the following outputs are expected to be generated in the `figures/` subdirectory:

- `data_type_overview.png`: Overview of data types during EDA.
- `framework.png`: Diagram of the project framework.
- `correlation_heatmap.png`: Heatmap of feature correlations.
- `logistic_regression_metrics.png`: Confusion matrix and metrics for Logistic Regression.
- `naive_bayes_metrics.png`: Confusion matrix and metrics for Naive Bayes.
- `knn_metrics.png`: Confusion matrix and metrics for KNN.
- `random_forest_metrics.png`: Confusion matrix and metrics for Random Forest.
- `model_comparison_roc.png`: ROC curve comparing all evaluated models.

Trained model artifacts (`.joblib` files) will also be saved in this main `results/` directory during execution. These are ignored by Git.
