# Comprehensive Machine Learning

Hey there!

This repo is a collection of machine learning scripts and code examples in Python and R. It covers the basics, some advanced topics, and everything in between — all explained with simple code and real examples. If you’re starting out or revising ML topics, this should be quite helpful.

Feel free to clone, explore, and modify things as you like. It’s all open and made for learning.

---

## What You’ll Find Here

Everything is split into folders based on the topic. Each one has a few Python & R Language files with clear explanations and code you can run directly.

Here’s what’s included:

- **Regression** – Linear, polynomial, SVR, decision tree, and random forest regressions.
- **Classification** – Logistic regression, KNN, decision trees, random forests, SVMs, and Naive Bayes.
- **Clustering** – K-Means and hierarchical clustering.
- **Association Rule Learning** – Apriori and Eclat algorithms.
- **Reinforcement Learning** – Bandit algorithms like UCB and Thompson Sampling.
- **NLP** – Basic text processing in Python and R.
- **Deep Learning** – Neural networks and CNNs.
- **Dimensionality Reduction** – PCA, LDA, and kernel PCA.
- **XGBoost** – Implementations in both Python and R.

---

## 🛠️ How to Set It Up

### Prerequisites

* Python - `3.9.6`
* R - `4.5.0`

### Environment Setup

Before installing dependencies, it's recommended to set up isolated environments for Python and R:

- **Python:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
- **R:**
  You can use [renv](https://rstudio.github.io/renv/) or your preferred R environment manager.

---

Install all dependencies using the Makefile:

```bash
make install_python   # For Python dependencies
make install_r        # For R dependencies
```

### Running the Code

1. First, clone the repo:

   ```bash
   git clone https://github.com/xscotophilic/machine-learning-lessons.git
   cd machine-learning-lessons
   ```

2. To run Python scripts:

   ```bash
   make run_python DIR=your_folder
   ```
   Replace `your_folder` with the subdirectory you want to run (e.g., `1.regression/1.data_preprocessing`).

3. To run R scripts:

   ```bash
   make run_r DIR=your_folder
   ```
   Replace `your_folder` with the subdirectory you want to run (e.g., `1.regression/1.data_preprocessing`).

---

## 🎯 Why This Repo Exists

I made this mainly to revise and understand machine learning in a hands-on way. This is my attempt to keep things simple and practical. If it helps you learn faster or makes some concept click, that’s great!

---

## 🤝 Want to Contribute?

If you spot a mistake, have a better explanation, or want to add your own examples:

* Fork the repo
* Create a branch
* Make your changes
* Raise a pull request

Even small improvements like fixing typos or simplifying explanations help a lot.

---

## 📄 License

MIT License – you’re free to use it however you like.
