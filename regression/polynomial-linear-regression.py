# Polynomial Linear Regression
# Linear regression with polynomial function using gradient descent
# Written by Alex Rago, 2020

def hypothesis(parameters, x):
    return parameters[0] + parameters[1] * x + parameters[2] * x ** 2


def linear_regression(data, learning_rate, num_iterations):
    parameters = [0, 0, 0]

    for i in range(num_iterations):
        parameters = step_gradient(data, learning_rate, parameters)

    return parameters


def step_gradient(data, learning_rate, parameters):
    alpha = learning_rate

    for point in data:
        x = point[0]
        y = point[1]
        h_x = hypothesis(parameters, x)
        parameters[0] -= alpha * (h_x - y)
        parameters[1] -= alpha * (h_x - y) * x
        parameters[2] -= alpha * (h_x - y) * x ** 2

    return parameters


def main():
    print("Test Code")


if __name__ == "__main__":
    main()
