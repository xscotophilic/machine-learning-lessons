# adding dataset
dataset = read.csv('data.csv')
dataset = dataset[, 3:5]
# ---------------------------------------------------
# dealing with missing values
dataset$Age = ifelse(is.na(dataset$Age), ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Age)
dataset$EstimatedSalary = ifelse(is.na(dataset$EstimatedSalary), ave(dataset$EstimatedSalary, FUN = function(x) mean(x, na.rm = TRUE)), dataset$EstimatedSalary)

# ---------------------------------------------------
# No need to encode any variable, as there aren't any categorical data
# and dependent variable is already encoded as 1 and 0.

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
training_set[, 1:2] = scale(training_set[, 1:2])
test_set[, 1:2] = scale(test_set[, 1:2])

# ---------------------------------------------------
# fitting logistic regression classification to the training set
classifier = glm( formula = Purchased ~ ., family = binomial, data = training_set)

# Predicting the test set results
# here test_set[-3] means we want prediction for last column
y_prob_pred = predict(classifier, type = 'response',newdata = test_set[-3])
# y_pred will show if customer will purchase item or not
y_pred = ifelse(y_prob_pred > 0.5, 1, 0)

# ---------------------------------------------------
# Creating confusion metrix
cm = table(test_set[, 3], y_pred)
print(cm)
