# Kernel PCA

> Kernel Principal Component Analysis (Kernel PCA) is an extension of Principal Component Analysis (PCA) using kernel methods. By applying a kernel, the originally linear operations of PCA are performed in a reproducing kernel Hilbert space, enabling nonlinear dimensionality reduction. Kernel PCA allows us to construct nonlinear versions of algorithms that can be expressed solely in terms of dot products, by leveraging the kernel trick.

## Table of Contents
1. [Introduction](#kernel-pca)
2. [How Kernel PCA Works](#how-kernel-pca-works)
3. [Further Reading](#further-reading)

## How Kernel PCA Works

- Kernel PCA projects data into a higher-dimensional space using a kernel function, then performs PCA in that space to capture nonlinear relationships.
- Common kernels include the Gaussian (RBF), polynomial, and sigmoid kernels.
- This approach is especially useful for datasets where linear PCA fails to capture the underlying structure.

**Mathematical Intuition:**
- The kernel trick allows computation of dot products in high-dimensional space without explicitly transforming the data.
- Kernel PCA finds principal components in this new space, enabling nonlinear dimensionality reduction.

## Further Reading
- [Kernel PCA vs PCA vs ICA in TensorFlow/Scikit-learn - Towards Data Science](https://towardsdatascience.com/kernel-pca-vs-pca-vs-ica-in-tensorflow-sklearn-60e17eb15a64)
- [ML | Introduction to Kernel PCA - GeeksforGeeks](https://www.geeksforgeeks.org/ml-introduction-to-kernel-pca/)
