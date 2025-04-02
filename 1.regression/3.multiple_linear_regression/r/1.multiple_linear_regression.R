# adding dataset
dataset = read.csv('data.csv')
# transforming/ factoring an independent variable
dataset$State = factor(dataset$State, levels = c('New York', 'California', 'Florida'), labels = c(1,2,3))

# if you haven't installed caTools library you have to run below line once.
# install.packages('caTools')

# adding lib
library(caTools)

# splitting data in test and training dataset
set.seed(404)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Fitting multiple linear regression to the Training set
regressor = lm(formula = Profit ~ ., data = training_set)

# Predicting the test results
y_pred = predict(regressor, newdata = test_set)