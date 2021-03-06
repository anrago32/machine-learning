# Machine Learning

This repository contains machine learning algorithms implemented in Python.

## Regression

For regression models, the hypothesis function h generates an output according to the parameters theta. Gradient descent is used to minimize the cost function for the hypothesis and find ideal parameters. Alpha represents the learning rate and m represents the size of the training data set.

### Basic Regression

#### Hypotheses

Linear Hypothesis:

![formula](http://latex.codecogs.com/svg.latex?h_%5Ctheta%28x%29%3D%5Ctheta_0%2B%5Ctheta_1x)

Logistic Hypothesis:

![formula](http://latex.codecogs.com/svg.latex?h_%5Ctheta%28x%29%3D%5Cfrac%7B1%7D%7B1%2Be%5E%7B-%28%5Ctheta_0%2B%5Ctheta_1x%29%7D%7D)

#### Algorithm

Repeat Until Convergence:

![formula](http://codecogs.com/svg.latex?%5Ctheta_0%3D%5Ctheta_0-%5Calpha%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%5Ctheta%28x_i%29-y_i%29)

![formula](http://codecogs.com/svg.latex?%5Ctheta_1%3D%5Ctheta_1-%5Calpha%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%5Ctheta%28x_i%29-y_i%29x_i)

### Multivariate Regression

#### Hypotheses

Linear Hypothesis:

![formula](http://latex.codecogs.com/svg.latex?h_%5Ctheta%28x%2Cy%29%3D%5Ctheta_0%2B%5Ctheta_1x%2B%5Ctheta_2y)

Logistic Hypothesis:

![formula](http://latex.codecogs.com/svg.latex?h_%5Ctheta%28x%2Cy%29%3D%5Cfrac%7B1%7D%7B1%2Be%5E%7B-%28%5Ctheta_0%2B%5Ctheta_1x%2B%5Ctheta_2y%29%7D%7D)

#### Algorithm

Repeat Until Convergence:

![formula](http://codecogs.com/svg.latex?%5Ctheta_0%3D%5Ctheta_0-%5Calpha%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%5Ctheta%28x_i%2Cy_i%29-z_i%29)

![formula](http://codecogs.com/svg.latex?%5Ctheta_1%3D%5Ctheta_1-%5Calpha%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%5Ctheta%28x_i%2Cy_i%29-z_i%29x_i)

![formula](http://codecogs.com/svg.latex?%5Ctheta_2%3D%5Ctheta_2-%5Calpha%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%5Ctheta%28x_i%2Cy_i%29-z_i%29y_i)

### Polynomial Regression

#### Hypotheses

Linear Hypothesis:

![formula](http://latex.codecogs.com/svg.latex?h_%5Ctheta%28x%29%3D%5Ctheta_0%2B%5Ctheta_1x%2B%5Ctheta_2x%5E2)

Logistic Hypothesis:

![formula](http://codecogs.com/svg.latex?h_%5Ctheta%28x%29%3D%5Cfrac%7B1%7D%7B1%2Be%5E%7B-%28%5Ctheta_0%2B%5Ctheta_1x%2B%5Ctheta_2x%5E2%29%7D%7D)

#### Algorithm

Repeat Until Convergence:

![formula](http://codecogs.com/svg.latex?%5Ctheta_0%3D%5Ctheta_0-%5Calpha%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%5Ctheta%28x_i%29-y_i%29)

![formula](http://codecogs.com/svg.latex?%5Ctheta_1%3D%5Ctheta_1-%5Calpha%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%5Ctheta%28x_i%29-y_i%29x_i)

![formula](http://latex.codecogs.com/svg.latex?%5Ctheta_2%3D%5Ctheta_2-%5Calpha%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%28h_%5Ctheta%28x_i%29-y_i%29x_i%5E2)

## License

[MIT License](https://opensource.org/licenses/mit-license.html)
