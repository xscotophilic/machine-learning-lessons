# *************************************************************************************
# ** Part 1 Data processing
# *************************************************************************************

# adding dataset
dataset <- read.csv('Data.csv')
dataset <- dataset[, 4:14]

# ---------------------------------------------------
# No need to deal with missing values for given dataset
# dataset$col_name = ifelse(is.na(dataset$col_name),
                          # ave(dataset$col_name, FUN = function(x) mean(x, na.rm = TRUE)),
                          # dataset$col_name)

# ---------------------------------------------------
# encoding the categorical variables (i.e. Geography and Gender) as a factor
dataset$Geography <- as.numeric(factor(dataset$Geography,
                                      levels = c('France', 'Spain', 'Germany'),
                                      labels = c(1, 2, 3))) 
dataset$Gender <- as.numeric(factor(dataset$Gender,
                                   levels = c('Female', 'Male'),
                                   labels = c(1, 2))) 

# ---------------------------------------------------
# splitting data in test and training dataset

# if you haven't installed caTools library you have to run below line once.
# install.packages('caTools')
# adding lib
library(caTools)
set.seed(404)
split <- sample.split(dataset$Exited, SplitRatio = 0.8)
training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)

# ---------------------------------------------------
# Applying scalar
# -11 means do not apply scaling on 11th column
training_set[, -11] <- scale(training_set[, -11])
test_set[, -11] <- scale(test_set[, -11])

# *************************************************************************************
# ** Part 2 Building the ANN
# *************************************************************************************

# ---------------------------------------------------
# if you haven't installed 'h2o' library follow the steps given on below link.
# http://docs.h2o.ai/h2o/latest-stable/h2o-docs/downloading.html#install-in-r
# adding lib
library(h2o)
h2o.init(nthreads = -1)
# fitting the ANN
classifier <- h2o.deeplearning(y = 'Exited',
                              training_frame = as.h2o(training_set),
                              activation = 'Rectifier',
                              hidden = c(6, 6), # 6 + 6 neurons in 2 hidden layers
                              epochs = 100,
                              train_samples_per_iteration = -2)

# *************************************************************************************
# ** Part 3 Making the predictions and evaluating the model
# *************************************************************************************

# ---------------------------------------------------
# Predicting the values
prob_pred <- h2o.predict(classifier, newdata = as.h2o(test_set[-11]))
y_pred <- prob_pred > 0.5
y_pred <- as.vector(y_pred)

# ---------------------------------------------------
# Creating confusion metrix
cm <- table(test_set[, 11], y_pred)
acc_score <- (cm["0", "0"]+cm["1", "1"])/(cm["0", "0"]+cm["0", "1"]+cm["1", "0"]+cm["1", "1"])

# shutting down the h2o
h2o.shutdown()