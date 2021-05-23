# adding dataset
dataset = read.csv('Data.csv')
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
# Applying Kernel PCA
# if you haven't installed 'kernlab' library you have to run below line once.
# install.packages('kernlab')
# adding lib
library(kernlab)
kpca = kpca(~., data = training_set[-3], kernel = 'rbfdot', features = 2)
training_set_kpca = as.data.frame(predict(kpca, training_set))
training_set_kpca$Purchased = training_set$Purchased
test_set_kpca = as.data.frame(predict(kpca, test_set))
test_set_kpca$Purchased = test_set$Purchased

# ---------------------------------------------------
# fitting logistic regression classification to the training set
classifier = glm( formula = Purchased ~ ., family = binomial, data = training_set_kpca)

# Predicting the test set results
# here test_set[-3] means we want prediction for last column
y_prob_pred = predict(classifier, type = 'response',newdata = test_set_kpca[-3])
# y_pred will show if customer will purchase item or not
y_pred = ifelse(y_prob_pred > 0.5, 1, 0)

# ---------------------------------------------------
# Creating confusion metrix
cm = table(test_set_kpca[, 3], y_pred)

# ---------------------------------------------------

# Visualising the Training set results
library(ElemStatLearn)
set = training_set_kpca
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.1)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.1)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('V1', 'V2')
prob_set = predict(classifier, type = 'response', newdata = grid_set)
y_grid = ifelse(prob_set > 0.5, 1, 0)
plot(set[, -3],
     main = 'Logistic Regression (Training set)',
     xlab = 'KPC1', ylab = 'KPC2',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))

# Visualising the Test set results
library(ElemStatLearn)
set = test_set_kpca
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.1)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.1)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('V1', 'V2')
prob_set = predict(classifier, type = 'response', newdata = grid_set)
y_grid = ifelse(prob_set > 0.5, 1, 0)
plot(set[, -3],
     main = 'Logistic Regression (Test set)',
     xlab = 'KPC1', ylab = 'KPC2',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))
