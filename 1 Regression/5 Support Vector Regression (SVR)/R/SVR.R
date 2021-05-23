# adding dataset
dataset = read.csv('Data.csv')
dataset = dataset[2:3]

# ---------------------------------------------------
# No need to deal with missing values
# as csv file doesn't contain any column which can have missing values

# ---------------------------------------------------
# splitting a dataset into training and test
# We have only 10 rows as data so we will not split dataset

# if you haven't installed caTools library you have to run below line once.
# install.packages('caTools')

# adding lib
# library(caTools)
# 
# splitting data in test and training dataset
# set.seed(404)
# split = sample.split(dataset$Salary, SplitRatio = 0.8)
# training_set = subset(dataset, split == TRUE)
# test_set = subset(dataset, split == FALSE)

# ---------------------------------------------------
# Applying scalar
# No need to scale
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])

# ---------------------------------------------------
# fitting SVR to the training set
# if you haven't installed e1071 library you have to run below line once.
# install.packages('e1071')

# adding lib
library(e1071)
regressor = svm(formula = Salary ~ .,
               data = dataset,
               type = 'eps-regression')

# Predicting the test set results
y_pred = predict(regressor, newdata = data.frame(Level = 6.5))

# ---------------------------------------------------
# if you haven't installed ggplot2 library you have to run below line once.
# install.packages('ggplot2')

# Visualising the Training set results
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)),
            color = 'blue') +
  ggtitle('Salary vs Position (Training set)') +
  xlab('Position') +
  ylab('Salary')