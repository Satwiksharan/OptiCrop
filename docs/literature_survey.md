# Epic 1: Problem Definition and Understanding

# 📚 Literature Survey

## Overview

Several studies in precision agriculture demonstrate that Machine Learning techniques significantly improve crop recommendation accuracy by analyzing soil nutrients and climatic conditions.

This survey reviews commonly used machine learning models and their strengths in agricultural prediction systems.

---

## Algorithms Reviewed

### Logistic Regression

- Simple and computationally efficient.
- Performs well on linearly separable datasets.
- Limited in modeling complex agricultural relationships.

### K-Nearest Neighbors (KNN)

- Predicts crops based on similarity with historical data.
- Easy to implement.
- Performance decreases with larger datasets.

### Decision Tree

- Generates interpretable decision rules.
- Handles non-linear relationships effectively.
- Can overfit without proper pruning.

### Random Forest

- Ensemble learning technique using multiple decision trees.
- Provides high prediction accuracy.
- Reduces overfitting and improves generalization.
- Frequently reported as one of the best-performing algorithms for crop recommendation.

### K-Means Clustering

- Unsupervised learning algorithm.
- Groups regions with similar soil and climate characteristics.
- Useful for exploratory analysis rather than direct crop prediction.

---

## Key Findings

Previous research highlights the importance of:

- Data preprocessing and cleaning
- Feature scaling using StandardScaler or MinMaxScaler
- Proper model evaluation and validation
- Balanced datasets for improved prediction accuracy

Among the evaluated models, Random Forest consistently demonstrates superior performance for crop recommendation problems involving multiple environmental variables.
