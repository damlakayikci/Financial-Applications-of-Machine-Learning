# Financial-Applications-of-Machine-Learning


This repository contains coursework and projects from the Financial Applications of Machine Learning course at Boğaziçi University. Throughout these exercises, the goal is to apply fundamental and advanced machine learning techniques to various financial datasets and problems, covering areas such as prediction, classification, and time series forecasting.

The repository is organized into four main parts:
	•	Problem Set 1 (ps1)
	•	Problem Set 2 (ps2)
	•	Problem Set 3 (ps3)
	•	Final Project (project)

Each part focuses on different machine learning approaches tailored to financial applications.


## Problem Set 1 (ps1)

In this problem set, the focus is on applying regression techniques to model relationships between financial variables. The primary objective is to predict financial outcomes, such as asset returns, based on historical data and economic indicators.

The methods used in this project include Linear Regression, Ridge Regression, and Lasso Regression. Linear regression is first applied to model simple relationships. Ridge regression is then introduced to handle multicollinearity by applying L2 regularization, while Lasso regression is used to encourage sparsity through L1 regularization.

Model evaluation metrics such as Root Mean Square Error (RMSE) and R² score are used to compare the models. Feature engineering is also explored to enhance model performance.


## Problem Set 2 (ps2)

In Problem Set 2, the emphasis shifts toward classification problems in finance, particularly tasks like predicting credit risk or detecting fraudulent activities.

The methods used include Logistic Regression, Decision Trees, and Random Forests. Logistic regression is applied to solve binary classification problems, such as predicting loan defaults. Decision trees provide an interpretable way to model financial decision-making, and random forests improve predictive accuracy by combining multiple trees through ensemble learning.

Model performance is assessed using metrics like accuracy, precision, and recall, highlighting the importance of selecting the right evaluation metric depending on the financial problem at hand.


## Problem Set 3 (ps3)

This problem set deals with time series analysis and forecasting in finance, which is crucial for applications such as predicting stock prices or interest rates.

The primary methods used here are Autoregressive (AR) models and ARIMA models. The project begins with an investigation of stationarity in time series data, applying differencing techniques when necessary. ARIMA models are then built to capture temporal dependencies, with careful model diagnostics performed to ensure adequacy.

Through this exercise, key concepts like time series decomposition, trend, and seasonality are also explored, giving hands-on experience in building financial forecasting models.


## Final Project (project)

In the final project, a more comprehensive machine learning pipeline is constructed, applying multiple advanced models to a complex financial dataset.

The methods used include Gradient Boosting Machines (GBM), specifically implementations like XGBoost, along with Support Vector Machines (SVM) and Neural Networks. Gradient boosting is utilized for its strength in handling structured financial data with high predictive power. Support Vector Machines are explored for classification tasks involving high-dimensional datasets. Neural networks are introduced to model complex nonlinear relationships, especially in financial time series data.

The project involves significant data preprocessing, feature selection, hyperparameter tuning, and thorough performance evaluation. Practical applications include developing predictive models for trading strategies and assessing portfolio risks based on model forecasts.


Getting Started

To run the notebooks in this repository, you can follow these steps:
1. **Clone the repository:**
  ```bash
git clone https://github.com/damlakayikci/Financial-Applications-of-Machine-Learning.git
  ```

2. **Navigate into a subproject folder (e.g., ps1):**
  ```bash
cd Financial-Applications-of-Machine-Learning/ps1
  ```

3. **Install the required dependencies:**
  ```bash
pip install -r requirements.txt
  ```

4. **Launch Jupyter Notebook:**
  ```bash
jupyter notebook
  ```


Each subproject contains its own set of scripts and notebooks demonstrating the application of the relevant machine learning techniques.

