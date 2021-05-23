# adding dataset
dataset = read.csv('Data.csv')
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

# Using Backward Elimination manually
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
               data = training_set)
summary(regressor)
# remove column for which p>alpha
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend,
               data = training_set)
summary(regressor)
# remove column for which p>alpha
regressor = lm(formula = Profit ~ R.D.Spend + Marketing.Spend,
               data = training_set)
summary(regressor)
# remove column for which p>alpha,
# but here no such column found so we get our model

# FOR Using Backward Elimination AUTOMATICALLY RUN BELOW CODE
# backwardElimination <- function(x, sl) {
#   numVars = length(x)
#   for (i in c(1:numVars)){
#     regressor = lm(formula = Profit ~ ., data = x)
#     maxVar = max(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"])
#     if (maxVar > sl){
#       j = which(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"] == maxVar)
#       x = x[, -j]
#     }
#     numVars = numVars - 1
#   }
#   return(summary(regressor))
# }
# 
# SL = 0.05
# dataset = dataset[, c(1,2,3,4,5)]
# backwardElimination(training_set, SL)
