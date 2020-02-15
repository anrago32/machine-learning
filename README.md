# Machine Learning
Machine learning algorithms implemented in Python

## Linear Regression

### Single Variable

Repeat until convergence:

![](http://latex.codecogs.com/svg.latex?%5Ctheta_0%3D%5Ctheta_0-%5Cfrac%7B%5Calpha%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7B%5Cinfty%7D%28h_%5Ctheta%28x_i%29-y_i%29)

![github-small](http://latex.codecogs.com/png.latex?%5Ctheta_1%3D%5Ctheta_1-%5Cfrac%7B%5Calpha%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7B%5Cinfty%7D%28h_%5Ctheta%28x_i%29-y_i%29x_i)

### Multi Variable

Repeat until convergence:

![github-small](http://latex.codecogs.com/jpg.latex?%5Ctheta_1%3D%5Ctheta_1-%5Cfrac%7B%5Calpha%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7B%5Cinfty%7D%28h_%5Ctheta%28x_i%2Cy_i%29-z_i%29)

![github-small](http://latex.codecogs.com/svg.latex?%5Ctheta_1%3D%5Ctheta_1-%5Cfrac%7B%5Calpha%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7B%5Cinfty%7D%28h_%5Ctheta%28x_i%2Cy_i%29-z_i%29x_i)

![github-small](http://latex.codecogs.com/svg.latex?%5Ctheta_2%3D%5Ctheta_2-%5Cfrac%7B%5Calpha%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7B%5Cinfty%7D%28h_%5Ctheta%28x_i%2Cy_i%29-z_i%29y_i)

## Logistic Regression

### Single Variable

Repeat until convergence:

![github-small](http://codecogs.com/svg.latex?%5Ctheta_0%3D%5Ctheta_0-%5Calpha%5Csum_%7Bi%3D1%7D%5E%7B%5Cinfty%7D%28h_%5Ctheta%28x_i%29-y_i%29)

![github-small](http://codecogs.com/svg.latex?%5Ctheta_1%3D%5Ctheta_1-%5Calpha%5Csum_%7Bi%3D1%7D%5E%7B%5Cinfty%7D%28h_%5Ctheta%28x_i%29-y_i%29x_i)

### Multi Variable

Repeat until convergence:

![github-small](http://codecogs.com/svg.latex?%255Ctheta_1%253D%255Ctheta_1-%255Calpha%255Csum_%257Bi%253D1%257D%255E%257B%255Cinfty%257D%2528h_%255Ctheta%2528x_i%2529-y_i%2529)

![github-small](http://codecogs.com/svg.latex?%255Ctheta_1%253D%255Ctheta_1-%255Calpha%255Csum_%257Bi%253D1%257D%255E%257B%255Cinfty%257D%2528h_%255Ctheta%2528x_i%2529-y_i%2529x_i)

![github-small](http://codecogs.com/svg.latex?%255Ctheta_2%253D%255Ctheta_2-%255Calpha%255Csum_%257Bi%253D1%257D%255E%257B%255Cinfty%257D%2528h_%255Ctheta%2528x_i%2529-y_i%2529y_i)
