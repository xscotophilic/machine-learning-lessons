# -----------------------------------------------------

# Importing the dataset
dataset <- read.csv('Data.csv')

# -----------------------------------------------------

# Implementing Upper Confidence Bound
N <- 10000
d <- 10
sums_of_rewards <- integer(d)
numbers_of_selection <- integer(d)
ads_selected <- integer(0)
total_reward <- 0

for (n in 1:N){
  ad <- 0
  max_upper_bound <- 0
  for (i in 1:d){
    if (numbers_of_selection[i] > 0){
      average_reward <- sums_of_rewards[i]/numbers_of_selection[i]
      delta_i <- sqrt(((3/2) * log(n)) / numbers_of_selection[i])
      upper_bound <- average_reward + delta_i
    } else{
      upper_bound <- 1e400
    }
    if (upper_bound > max_upper_bound){
      max_upper_bound <- upper_bound
      ad <- i
    }
  }
  ads_selected <- append(ads_selected, ad)
  numbers_of_selection[ad] <- numbers_of_selection[ad] + 1
  reward <- dataset[n, ad]
  sums_of_rewards[ad] <- sums_of_rewards[ad] + reward
  total_reward <- total_reward + reward
}
# First 10 rounds will select all 10 ads and after that we use given algorithm to select ads

# -----------------------------------------------------

# Visualising the results
hist(ads_selected,
     col = 'blue',
     main = 'Histogram of ads selections',
     xlab = 'Ads',
     ylab = 'Number of times each ad was selected')