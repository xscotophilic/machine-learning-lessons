# Data preprocessing

Data preprocessing is a crucial step in the machine learning pipeline. It transforms raw, messy data into a clean and structured format suitable for modeling, which can significantly improve the performance and reliability of machine learning algorithms.

## Why is data preprocessing important?
- Real-world data is often incomplete, inconsistent, and contains errors or outliers.
- Proper preprocessing ensures that the data fed into models is accurate, relevant, and in the right format, leading to better results.

## Example
**Raw data:**
| Country | Age | Salary  | Purchased |
|---------|-----|---------|-----------|
| France  | 44  | 72000   | No        |
| Spain   | 27  | 48000   | Yes       |
| Germany | 30  |         | No        |

**After preprocessing:**
- Missing values filled or removed
- Categorical data encoded (e.g., Country → numbers)
- Features scaled

## Common libraries
- **Python:** pandas, numpy, scikit-learn
- **R:** dplyr, tidyr, caret

## Typical steps
- Getting the dataset
- Importing libraries
- Importing datasets
- Finding missing data
- Encoding categorical data
- Splitting the dataset into training and test sets
- Feature scaling

## Directory structure
- `python/` — Python code examples for preprocessing
- `r/` — R code examples for preprocessing

## Further reading
- [scikit-learn: Preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html)
- [R for Data Science: Data tidying](https://r4ds.had.co.nz/tidy-data.html)
