# adding dataset
dataset = read.csv('data.csv')
dataset = dataset[, 3:5]

# ---------------------------------------------------
# dealing with missing values
dataset$Age = ifelse(is.na(dataset$Age), ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Age)
dataset$EstimatedSalary = ifelse(is.na(dataset$EstimatedSalary), ave(dataset$EstimatedSalary, FUN = function(x) mean(x, na.rm = TRUE)), dataset$EstimatedSalary)

# ---------------------------------------------------
# No need to encode any independent variable, as there aren't any categorical data

# and dependent variable is already encoded as 1 and 0, but it's better if we factor dependent variable.
# encoding the target feature as a factor
dataset$Purchased = factor(dataset$Purchased, levels = c(0, 1))

# ---------------------------------------------------
# splitting data in test and training dataset

# if you haven't installed caTools library you have to run below line once.
# install.packages('caTools')
# adding lib
library(caTools)
set.seed(404)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# ---------------------------------------------------
# Applying scalar
# -3 means do not apply scaling on 3rd column
training_set[, -3] = scale(training_set[, -3])
test_set[, -3] = scale(test_set[, -3])

# ---------------------------------------------------
# Decision Tree Classification and the training set
# if you haven't installed 'rpart' library you have to run below line once.
# install.packages('rpart')
# adding lib
library(rpart)
classifier = rpart(formula = Purchased ~ ., data = training_set)

# y_pred will show if customer will purchase item or not
y_pred = predict(classifier, newdata = test_set[-3], type = 'class')

# ---------------------------------------------------
# Creating confusion metrix
cm = table(test_set[, 3], y_pred)
print(cm)