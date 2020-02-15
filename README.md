# Machine Learning
Machine learning algorithms implemented in Python

## Linear Regression

### Single Variable Algorithm

![formula](http://latex.codecogs.com/svg.latex?h_%5Ctheta%28x%29%3D%5Ctheta_0%2B%5Ctheta_1x)

Repeat until convergence:

![formula](http://latex.codecogs.com/svg.latex?%5Ctheta_0%3D%5Ctheta_0-%5Cfrac%7B%5Calpha%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7B%5Cinfty%7D%28h_%5Ctheta%28x_i%29-y_i%29)

![formula](http://latex.codecogs.com/svg.latex?%5Ctheta_1%3D%5Ctheta_1-%5Cfrac%7B%5Calpha%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7B%5Cinfty%7D%28h_%5Ctheta%28x_i%29-y_i%29x_i)

### Multi Variable Algorithm

![formula](http://latex.codecogs.com/svg.latex?h_%5Ctheta%28x%29%3D%5Ctheta_0%2B%5Ctheta_1x%2B%5Ctheta2_y)

Repeat until convergence:

![formula](http://latex.codecogs.com/svg.latex?%5Ctheta_1%3D%5Ctheta_1-%5Cfrac%7B%5Calpha%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7B%5Cinfty%7D%28h_%5Ctheta%28x_i%2Cy_i%29-z_i%29)

![formula](http://latex.codecogs.com/svg.latex?%5Ctheta_1%3D%5Ctheta_1-%5Cfrac%7B%5Calpha%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7B%5Cinfty%7D%28h_%5Ctheta%28x_i%2Cy_i%29-z_i%29x_i)

![formula](http://latex.codecogs.com/svg.latex?%5Ctheta_2%3D%5Ctheta_2-%5Cfrac%7B%5Calpha%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7B%5Cinfty%7D%28h_%5Ctheta%28x_i%2Cy_i%29-z_i%29y_i)

## Logistic Regression

### Single Variable Algorithm

![formula](http://latex.codecogs.com/svg.latex?%5Cfrac%7B1%7D%7B1%2Be%5E%7B-%28%5Ctheta_0%2B%5Ctheta_1x%29%7D%7D)

Repeat until convergence:

![formula](http://codecogs.com/svg.latex?%5Ctheta_0%3D%5Ctheta_0-%5Calpha%5Csum_%7Bi%3D1%7D%5E%7B%5Cinfty%7D%28h_%5Ctheta%28x_i%29-y_i%29)

![formula](http://codecogs.com/svg.latex?%5Ctheta_1%3D%5Ctheta_1-%5Calpha%5Csum_%7Bi%3D1%7D%5E%7B%5Cinfty%7D%28h_%5Ctheta%28x_i%29-y_i%29x_i)

### Multi Variable Algorithm

![formula](http://latex.codecogs.com/svg.latex?%5Cfrac%7B1%7D%7B1%2Be%5E%7B-%28%5Ctheta_0%2B%5Ctheta_1x%2B%5Ctheta_2y%29%7D%7D)

Repeat until convergence:

![formula](http://codecogs.com/svg.latex?%5Ctheta_1%3D%5Ctheta_1-%5Calpha%5Csum_%7Bi%3D1%7D%5E%7B%5Cinfty%7D%28h_%5Ctheta%28x_i%2Cy_i%29-z_i%29)

![formula](http://codecogs.com/svg.latex?%5Ctheta_1%3D%5Ctheta_1-%5Calpha%5Csum_%7Bi%3D1%7D%5E%7B%5Cinfty%7D%28h_%5Ctheta%28x_i%2Cy_i%29-z_i%29x_i)

![formula](http://codecogs.com/svg.latex?%5Ctheta_1%3D%5Ctheta_1-%5Calpha%5Csum_%7Bi%3D1%7D%5E%7B%5Cinfty%7D%28h_%5Ctheta%28x_i%2Cy_i%29-z_i%29y_i)
