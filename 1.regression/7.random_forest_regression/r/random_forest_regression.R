# adding dataset
dataset = read.csv('data.csv')
dataset = dataset[2:3]

# ---------------------------------------------------
# No need to deal with missing values
# as csv file doesn't contain any column which can have missing values

# ---------------------------------------------------
# No need to encode any variable as there aren't any categorical data

# ---------------------------------------------------
# splitting a dataset into training and test

# if you haven't installed caTools library you have to run below line once.
# install.packages('caTools')

# adding lib
library(caTools)

# splitting data in test and training dataset
set.seed(404)
split = sample.split(dataset$Salary, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# ---------------------------------------------------
# No need to apply scalar because of the way Random Forest Regression model is build

# ---------------------------------------------------
# fitting Random Forest Regression to the training set
# if you haven't installed randomForest library you have to run below line once.
# install.packages('randomForest')

# adding lib
library(randomForest)
set.seed(404)
# abc[] returns dataframe and abc$col_name returns vector
regressor = randomForest(x = training_set[1], y = training_set$Salary, ntree = 100)

# Predicting the test set results
y_pred = predict(regressor, newdata = test_set)

# ---------------------------------------------------
# if you haven't installed ggplot2 library you have to run below line once.
# install.packages('ggplot2')

# Visualising the Random Forest Regression Training set results

# For high resolution
X_train_grid = seq(min(training_set$Level), max(training_set$Level), 0.01)

library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$Level, y = training_set$Salary),
             color = 'green') +
  geom_point(aes(x = test_set$Level, y = predict(regressor, newdata = test_set)),
             color = 'red') +
  geom_line(aes(x = X_train_grid, y = predict(regressor, newdata = data.frame(Level = X_train_grid))),
            colour = 'blue') +
  ggtitle('Salary vs Position (Random Forest Regression)') +
  xlab('Position') +
  ylab('Salary')