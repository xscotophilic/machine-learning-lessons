# adding dataset
dataset <- read.csv('Data.csv')
X <- dataset[, 4:5] # selecting only 4th and 5th column for learning purpose

# ---------------------------------------------------
# dealing with missing values
X$Annual.Income..k.. <- ifelse(is.na(X$Annual.Income..k..), ave(X$Annual.Income..k.., FUN = function(x) mean(x, na.rm = TRUE)), X$Annual.Income..k..)
X$Spending.Score..1.100. <- ifelse(is.na(X$Spending.Score..1.100.), ave(X$Spending.Score..1.100., FUN = function(x) mean(x, na.rm = TRUE)), X$Spending.Score..1.100.)

# ---------------------------------------------------

# No need to encode any variable, as there aren't any categorical data

# ---------------------------------------------------

# No need to split data in test and training dataset

# ---------------------------------------------------

# No need to Apply scalar

# ---------------------------------------------------

# Using Dendogram to find optimal number of clusters

dendogram <- hclust(dist(X, method = 'euclidean'), method = 'ward.D')
plot(dendogram,
     main = paste("Dendogram"),
     xlab = "Customers",
     ylab = "Euclidean distances")

no_of_clusters <- 5 # 5 is optimal no of clusters as you can see in graph

# ---------------------------------------------------

# Training the hierarchical clustering model on dataset

hc <- hclust(dist(X, method = 'euclidean'), method = 'ward.D')
y_hc <- cutree(hc, no_of_clusters)

# ---------------------------------------------------
# Graph for hierarchical clustering
# Graph will take some time to process so give it some time

# if you haven't installed 'cluster' library you have to run below line once.
# install.packages('cluster')

# adding lib
library(cluster)
clusplot(X,
         y_hc,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 2, 
         plotchar = FALSE,
         span = TRUE,
         main = paste("Clusters of clients"),
         xlab = 'Anual Income',
         ylab = 'Spending score'
)
