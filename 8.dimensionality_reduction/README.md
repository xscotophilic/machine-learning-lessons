# Dimensionality Reduction

> Dimensionality reduction is the process of reducing the number of input variables (features) in a dataset, making data easier to visualize and models less prone to overfitting.

## Table of Contents

- [Overview](#overview)
- [Key Terminologies](#key-terminologies)
- [Types of Dimensionality Reduction](#types-of-dimensionality-reduction)
- [Further Reading](#further-reading)

## Overview

High-dimensional data can be difficult to analyze and visualize. Dimensionality reduction techniques help simplify data, improve model performance, and reduce computational cost.

**Use Cases:**
- Data visualization (e.g., plotting high-dimensional data in 2D)
- Noise reduction
- Preprocessing for machine learning models

## Key Terminologies

- **Feature Selection**: Identifying and selecting the most relevant features.
- **Feature Extraction**: Creating new features from existing ones (e.g., using PCA).
- **Curse of Dimensionality**: The phenomenon where the feature space becomes sparse as dimensions increase, making analysis harder.

**Mathematical Intuition:**
- Dimensionality reduction seeks to project data from a high-dimensional space to a lower-dimensional one, preserving as much information as possible.
- Techniques like PCA find new axes (principal components) that capture the most variance in the data.

## Types of Dimensionality Reduction

- **Linear Methods**
  - Principal Component Analysis (PCA) ([see details](principal_component_analysis/README.md))
  - Linear Discriminant Analysis (LDA) ([see details](linear_discriminant_analysis/README.md))
- **Non-linear Methods**
  - Kernel PCA ([see details](kernel_pca/README.md))
  - Isomap, t-SNE, etc.

## Further Reading

- [Dimensionality Reduction Techniques – GeeksforGeeks](https://www.geeksforgeeks.org/dimensionality-reduction-techniques/)
