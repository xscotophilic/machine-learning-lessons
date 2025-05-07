# Regression

> Regression models are used to predict a continuous value by estimating the relationship between the target and independent variables. They are fundamental tools in machine learning for uncovering trends and making predictions based on data.

## Table of Contents

- [Overview](#overview)
- [Key Terminologies](#key-terminologies)
- [Types of Regression](#types-of-regression)
- [Further Reading](#further-reading)

## Overview

Regression analysis is a statistical method used to examine the relationship between one dependent (target) variable and one or more independent (predictor) variables. It is widely used for:

- Predicting real/continuous values (e.g., house prices, temperatures)
- Identifying trends and patterns in data
- Quantifying the strength of relationships between variables

**Use Cases:**
- Forecasting sales or stock prices
- Predicting medical outcomes (e.g., blood pressure)
- Risk assessment in insurance

## Key Terminologies

1. **Dependent Variable**: The main factor in regression analysis that we wish to predict or understand. Also known as the target variable.
2. **Independent Variable**: A predictor that affects the dependent variable or is used to predict its values.
3. **Outliers**: Observations that stand out from the rest due to extremely high or low values. Outliers can skew results and should be handled carefully.

**Mathematical Intuition:**
- Regression models estimate a function $f$ such that $y = f(X) + \epsilon$, where $y$ is the target, $X$ are the predictors, and $\epsilon$ is the error term.
- The most common approach is to minimize the sum of squared errors between predicted and actual values.

## Types of Regression

1. **Simple Linear Regression**
2. **Multiple Linear Regression**
3. **Polynomial Regression**
4. **Support Vector Regression**
5. **Decision Tree Regression**
6. **Random Forest Regression**
7. **Ridge Regression**
8. **Lasso Regression**

Each type of regression has its own strengths and is suited for different kinds of data and problem statements.

## Further Reading

- [Regression Analysis (Wikipedia)](https://en.wikipedia.org/wiki/Regression_analysis)
- [Scikit-learn Regression Documentation](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)
