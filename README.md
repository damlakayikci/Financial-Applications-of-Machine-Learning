# 📈 Financial Applications of Machine Learning

This repository contains a series of projects exploring the applications of machine learning techniques in financial data analysis and investment strategy development. The projects involve predictive modeling, classification, time series forecasting, and portfolio optimization using real-world and simulated financial data.

## Contents

- [Problem Set 1 (PS1)](#problem-set-1-ps1)
- [Problem Set 2 (PS2)](#problem-set-2-ps2)
- [Problem Set 3 (PS3)](#problem-set-3-ps3)
- [Final Project](#final-project)
- [Machine Learning Methods Used](#machine-learning-methods-used)
- [Libraries Used](#libraries-used)
- [Running the Code](#running-the-code)

---

## Problem Set 1 (PS1)

**Objective**:  
Predict stock returns using regression methods and evaluate model performance.

**Techniques**:
- **Linear Regression**: Basic modeling of returns.
- **Ridge Regression**: Regularization to prevent overfitting.
- **Lasso Regression**: Variable selection and regularization.

**Key Concepts**:
- Model selection based on predictive accuracy.
- Bias-variance tradeoff analysis.

📂 See folder: [`ps1`](./ps1)

---

## Problem Set 2 (PS2)

**Objective**:  
Build classifiers to predict whether a stock's future return will be positive or negative.

**Techniques**:
- **Logistic Regression**: Baseline classification method.
- **k-Nearest Neighbors (k-NN)**: Non-parametric classification.
- **Decision Trees**: Simple tree-based modeling.
- **Random Forests**: Ensemble learning for better generalization.

**Key Concepts**:
- Classification accuracy, confusion matrices.
- Model complexity vs performance.

📂 See folder: [`ps2`](./ps2)

---

## Problem Set 3 (PS3)

**Objective**:  
Model and forecast stock return volatility using time series methods.

**Techniques**:
- **Autoregressive Models (AR)**
- **Moving Average Models (MA)**
- **ARMA / ARIMA Models**: For capturing complex dependencies.
- **GARCH Models**: For volatility clustering and dynamic variance modeling.

**Key Concepts**:
- Time series stationarity and differencing.
- Volatility forecasting.

📂 See folder: [`ps3`](./ps3)

---

## Final Project

**Objective**:  
Develop a factor-based investment strategy using advanced machine learning techniques and evaluate its performance on real-world data.

**Techniques**:
- **Linear Regression with Feature Engineering**: Create predictors based on financial factors.
- **Ensemble Methods (Bagging, Boosting)**: Improve predictive performance.
- **Sharpe Ratio and Return Metrics**: Evaluate investment profitability and risk-adjusted returns.

**Key Concepts**:
- Model interpretability.
- Backtesting and out-of-sample evaluation.

📂 See folder: [`project`](./project)

---

## Machine Learning Methods Used

- **Regression Models**:  
  Linear Regression, Ridge Regression, Lasso Regression

- **Classification Models**:  
  Logistic Regression, k-Nearest Neighbors (k-NN), Decision Trees, Random Forests

- **Time Series Models**:  
  AR, MA, ARMA, ARIMA, GARCH

- **Ensemble Methods**:  
  Bagging, Boosting

- **Evaluation Metrics**:  
  Mean Squared Error (MSE), Accuracy, Sharpe Ratio, Return Analysis

---

## Libraries Used

- **numpy**
- **pandas**
- **matplotlib**
- **seaborn**
- **scikit-learn**
- **statsmodels**
- **arch** (for GARCH models)
- **scipy**

---

## Running the Code

Each subproject (`ps1`, `ps2`, `ps3`, `project`) contains its own Python scripts or Jupyter notebooks.  
To run a project:

1. Clone the repository:
    ```bash
    git clone https://github.com/damlakayikci/Financial-Applications-of-Machine-Learning.git
    cd Financial-Applications-of-Machine-Learning
    ```

2. Install the necessary packages:
    ```bash
    pip install numpy pandas matplotlib seaborn scikit-learn statsmodels arch scipy
    ```

3. Navigate to the desired subproject folder:
    ```bash
    cd ps1
    python ps1_solution.py
    ```

> Note: Some subprojects are implemented as Jupyter notebooks (`.ipynb`). You can open them using:
> ```bash
> jupyter notebook
> ```

---
