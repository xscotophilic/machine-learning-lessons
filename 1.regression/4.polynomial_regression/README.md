# Polynomial Regression

> Polynomial regression extends linear regression by modeling the relationship between the independent variable(s) and the dependent variable as an nth degree polynomial. This allows the model to capture non-linear patterns in the data.

## Table of Contents

- [Overview](#overview)
- [Polynomial Expression](#polynomial-expression)
- [Model Fitting Example](#model-fitting-example)
- [Model Comparison](#model-comparison)
- [Further Reading](#further-reading)

## Overview

Linear regression sometimes cannot capture complex patterns in data, leading to underfitting. To address this, we can increase the model's complexity by introducing polynomial features—powers of the original features—enabling the model to fit a higher-order equation.

<p align="center">
    <img src="readme_assets/polynomial_regression_insufficiency.png" alt="Linear Regression Insufficiency" width="500"/>
</p>

## Polynomial Expression

A polynomial regression model of degree *n* can be expressed as:

<p align="center">
    <img src="readme_assets/polynomial_regression_equation.png" alt="Polynomial Regression Equation" width="400"/>
</p>

## Model Fitting Example

Fitting a polynomial regression model (degree = 2):

<p align="center">
    <img src="readme_assets/polynomial_regression_fit_degree2.png" alt="Polynomial Regression Fit (Degree 2)" width="400"/>
</p>

## Model Comparison

Comparing the fit of models with different polynomial degrees:

<p align="center">
    <img src="readme_assets/polynomial_regression_degree_comparison.png" alt="Polynomial Regression Degree Comparison" width="500"/>
</p>

## Further Reading

- [Polynomial Regression — Towards Data Science](https://towardsdatascience.com/polynomial-regression-bbe8b9d97491)
