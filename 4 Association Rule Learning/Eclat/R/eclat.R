# Data Preprocessing

# if you haven't installed 'arules' library you have to run below line once.
# install.packages('arules')
library(arules)
dataset <- read.csv('Data.csv')
dataset <- read.transactions('Data.csv', sep = ',', rm.duplicates = TRUE)
summary(dataset)

# Plotting top 10 frequent Items
itemFrequencyPlot(dataset, topN = 10)

# Training Eclat on the dataset
rules <- eclat(data = dataset, parameter = list(support = 0.003, minlen = 2))

# Visualising the results
inspect(sort(rules, by = 'support')[1:10])