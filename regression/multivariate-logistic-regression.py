# Multivariate Logistic Regression
# Logistic regression with multiple variables using gradient descent
# Written by Alex Rago, 2020

from math import e


def hypothesis(parameters, x, y):
    exponent = parameters[0] + parameters[1] * x + parameters[2] * y
    return 1 / (1 + e ** -exponent)


def logistic_regression(data, learning_rate, num_iterations):
    parameters = [0, 0, 0]

    for i in range(num_iterations):
        parameters = step_gradient(data, learning_rate, parameters)

    return parameters


def step_gradient(data, learning_rate, parameters):
    alpha = learning_rate

    for point in data:
        x = point[0]
        y = point[1]
        z = point[2]
        h_xy = hypothesis(parameters, x, y)
        parameters[0] -= alpha * (h_xy - z)
        parameters[1] -= alpha * (h_xy - z) * x
        parameters[2] -= alpha * (h_xy - z) * y

    return parameters


def main():
    print("Test Code")


if __name__ == "__main__":
    main()
