# Support Vector Regression (SVR)

### In most Linear regression models & Polynomial regression models, the objective is to minimize the sum of squared errors.

### Support Vector Regression (SVR) gives us the flexibility to define how much error is acceptable in our model and will find an appropriate line (or hyperplane in higher dimensions) to fit the data.

- First, let's define certain terms.

  1. Kernel: A function for converting lower-dimensional data to higher-dimensional data.

  2. Hyper Plane: In SVM, this is essentially the line that separates the data classes. Although, in SVR, it will be defined as a line that will assist us in predicting a continuous value or a target value.

  3. Boundary lines: Other than the Hyper Plane, there are two lines in SVM that form a margin. The support vectors might be inside or outside the boundary lines. The two classes are separated by this line. The premise is the same in SVR.

  4. Support vectors: The data points closest to the boundary are called support vectors. The distance between the points is minimal or negligible.

<p align="center">
    <img src="https://user-images.githubusercontent.com/47301282/120436365-79295b00-c39c-11eb-8b44-f697a60b13b3.png" />
</p>

- Blue line: Hyper Plane; Red Line: Boundary Line; Green Dots: Given Data

- How all the points are within the boundary line(Red Line). When we're working with SVR, our goal is to think about the points that are within the boundary line. The line hyperplane with the greatest number of points is our best fit line.

#### For Aditional Reading:

Chapter 4 - Support Vector Regression

[from: Efficient Learning Machines: Theories, Concepts, and Applications for Engineers and System Designers](https://github.com/xscotophilic/Machine-Learning-Basic-Lessons/files/6582436/Support.Vector.Regression.pdf)

By Mariette Awad & Rahul Khanna (2015)
