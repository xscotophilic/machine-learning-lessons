# adding dataset
dataset = read.csv('data.csv')

# dealing with missing values
dataset$Age = ifelse(is.na(dataset$Age), ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary), ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Salary)

# transforming/ factoring an independent variable
dataset$Country = factor(dataset$Country, levels = c('France', 'Spain', 'Germany'), labels = c(1,2,3))

# transforming/ factoring a dependent variable
dataset$Purchased = factor(dataset$Purchased, levels = c('No', 'Yes'), labels = c(0,1))

# if you haven't installed caTools library you have to run below line once.
# install.packages('caTools')

# adding lib
library(caTools)

# splitting data in test and training dataset
set.seed(404)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Applying scalar
training_set[, 2:3] = scale(training_set[, 2:3])
test_set[, 2:3] = scale(test_set[, 2:3])