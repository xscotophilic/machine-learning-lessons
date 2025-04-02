# adding dataset
dataset_original <- read.delim('data.tsv', quote = '', stringsAsFactors = FALSE)

# ---------------------------------------------------
# Cleaning Texts

# if you haven't installed 'tm' library you have to run below line once.
# install.packages('tm')
library(tm)
# if you haven't installed 'SnowballC' library you have to run below line once.
# install.packages('SnowballC')
library(SnowballC)
corpus <- VCorpus(VectorSource(dataset_original$Review))
corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeWords, stopwords())
corpus <- tm_map(corpus, stemDocument)
corpus <- tm_map(corpus, stripWhitespace)

# ---------------------------------------------------
# Creating the Bag of Words model
dtm <- DocumentTermMatrix(corpus)
# By checking DTM we can see that it has 1577 columns
dtm <- removeSparseTerms(dtm, 0.999) # we keep 99.9% of the words in dtm
# Transforming into dataframe
dataset <- as.data.frame(as.matrix(dtm))
dataset$Liked <- dataset_original$Liked

# ---------------------------------------------------
# No need to encode any independent variable, as there aren't any categorical data

# and dependent variable is already encoded as 1 and 0, but it's better if we factor dependent variable.
# encoding the target feature as a factor
dataset$Liked = factor(dataset$Liked, levels = c(0, 1))

# ---------------------------------------------------
# splitting data in test and training dataset

# if you haven't installed caTools library you have to run below line once.
# install.packages('caTools')
# adding lib
library(caTools)
set.seed(404)
split = sample.split(dataset$Liked, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# ---------------------------------------------------
# No need to apply scalar
# -3 means do not apply scaling on 3rd column
# training_set[, -3] = scale(training_set[, -3])
# test_set[, -3] = scale(test_set[, -3])

# ---------------------------------------------------
# Random Forest Classification and the training set
# if you haven't installed 'randomForest' library you have to run below line once.
# install.packages('randomForest')
# adding lib
library(randomForest)
classifier = randomForest(x = training_set[-692],
                          y = training_set$Liked,
                          ntree = 10)

# y_pred will show if customer will purchase item or not
y_pred = predict(classifier, newdata = test_set[-692])

# ---------------------------------------------------
# Creating confusion metrix
cm = table(test_set[, 692], y_pred)
acc_score <- (cm["0", "0"]+cm["1", "1"])/(cm["0", "0"]+cm["0", "1"]+cm["1", "0"]+cm["1", "1"])
