# adding dataset
dataset = read.csv('salary_data.csv')

# if you haven't installed caTools library you have to run below line once.
# install.packages('caTools')

# adding lib
library(caTools)

# splitting data in test and training dataset
set.seed(404)
split = sample.split(dataset$Salary, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# fitting simple regression to the training set
regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)

# Predicting the test set results
y_pred = predict(regressor, newdata = test_set)

# if you haven't installed ggplot2 library you have to run below line once.
# install.packages('ggplot2')

# Visualising the Training set results
library(ggplot2)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             color = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            color = 'blue') +
  ggtitle('Salary vs Experience(Training set)') +
  xlab('Years of experience') +
  ylab('Salary')

# Visualising the Test set results
library(ggplot2)
ggplot() +
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             color = 'green') +
  geom_line(aes(x = test_set$YearsExperience, y = predict(regressor, newdata = test_set)),
            color = 'yellow') +
  ggtitle('Salary vs Experience(Test set)') +
  xlab('Years of experience') +
  ylab('Salary')