# Simple linear regression

- Simple linear regression is a statistical approach which enables us to summarise and examine the connection of two (quantitative) continuous variables.

- Independent variables: Data that can be controlled directly. Dependent variables: Data that cannot be controlled directly.

  - Example: If you want to know whether caffeine affects your appetite, the presence/absence of a given amount of caffeine would be the independent variable. How hungry you are would be the dependent variable.

- Linear regression models provide a simple approach towards supervised learning. They are simple yet effective.

  - Linear implies: organised or extended in a straight or almost straight line. Linear means that a straight line may be used for the relationship between dependent and independent variable.

  - equation of a line: `y = mx + c`

  1. y is the dependent variable i.e. the estimated and predicted variable.

  2. x is a standalone variable i.e. a controlled variable. It's the entry.

  3. M's the slope. The angle of the line is determined.

  4. C is intercept. C is intercept.

---

## Model Building and Interpretation

- Basics: The training data is used to create the model. The testing data is used to evaluate the model performance.

- The essence of LR is to find the line that best fits the data points on the plot.

<p align="center">
  <img src="https://user-images.githubusercontent.com/47301282/119482339-60ec8700-bd71-11eb-8d65-46f3bbca3a50.png" alt="data"/>
</p>

- In terms of Machine Learning, this follows the convention: `h(X) = W0 + W1.X` Where W0 and W1 are weights, X is the input feature, and h(X) is the label (i.e. y-value).

- The way Linear Regression works is by trying to find the weights (namely, W0 and W1) that lead to the best-fitting line for the input data (i.e. X features) we have. The best-fitting line is determined in terms of lowest cost.

<p align="center">
  <img src="https://user-images.githubusercontent.com/47301282/119482343-621db400-bd71-11eb-8673-4f8ea30dd6a9.png" alt="Linear Regression"/>
</p>

- Depending on the Machine Learning application at hand, costs might take several forms. However, costs often relate to the loss or error the model outputs from the actual training data. The cost function that we commonly utilise is the Squared Error Cost when it comes to linear regression.

<p align="center">
  <img src="https://user-images.githubusercontent.com/47301282/119482333-5fbb5a00-bd71-11eb-8909-f3f124ae9f15.png" alt="Error"/>
</p>

- Training a Machine Learning model is all about using a Learning Algorithm to find the weights (W0, W1 in our formula) that minimise the cost.

---

<p align="center">
  <img src="https://user-images.githubusercontent.com/47301282/119249633-c268f600-bbb7-11eb-8f83-113142958427.png" alt="Thankyou!"/>
</p>
