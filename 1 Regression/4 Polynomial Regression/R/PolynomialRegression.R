# adding dataset
dataset = read.csv('Data.csv')

# ---------------------------------------------------
# here 1st column is already encoded and represented as column 2 in csv file
# so we will use only 2nd column as an independent variable
dataset = dataset[2:3]

# No need to deal with missing values
# as csv file doesn't contain any column which can have missing values

# No need to transform any independent variable
# as we will be using 2nd column (which is numerical) to train and test model.

# ---------------------------------------------------
# splitting a dataset into training and test
# We have only 10 rows as data so we will not split dataset
# if you haven't installed ggplot2 library you have to run below line once.
# install.packages('ggplot2')

# ---------------------------------------------------
# Applying simple linear regression
linear_regressor = lm(formula = Salary ~ . , data = dataset)
# ---------------------------------------------------
# Graph for linear regressor
# GREEN DOTS REPRESENTS THE ACTUAL VALUES
# BLUE DOTS REPRESENTS THE REGRESSION LINE
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), color = 'green') +
  geom_line(aes(x = dataset$Level, y = predict(linear_regressor, newdata = dataset)), color = 'blue') +
  ggtitle('Salary vs Position (Linear regression)') +
  xlab('Positions') +
  ylab('Salary')

# ---------------------------------------------------
# Applying polynomial regression
dataset$PolyLevel = dataset$Level^3
polynomial_regressor = lm(formula = Salary ~ . , data = dataset)
# ---------------------------------------------------
# Graph for polynomial regressor 
# GREEN DOTS REPRESENTS THE ACTUAL VALUES
# BLUE DOTS REPRESENTS THE REGRESSION LINE
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary), color = 'green') +
  geom_line(aes(x = dataset$Level, y = predict(polynomial_regressor, newdata = dataset)), color = 'blue') +
  ggtitle('Salary vs Position (Polynomial regression)') +
  xlab('Positions') +
  ylab('Salary')

# ---------------------------------------------------
# Predicting a new result with Linear Reg
y_pred = predict(linear_regressor, newdata = data.frame(Level = 6.5))
# Predicting a new result with Polynomial Reg
y_pred = predict(polynomial_regressor, newdata = data.frame(Level = 6.5, PolyLevel = (6.5)^3))
