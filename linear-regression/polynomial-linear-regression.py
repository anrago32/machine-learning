def hypothesis(parameters, x):
    return parameters[0] + parameters[1] * x + parameters[2] * x * x


def linear_regression(data, learning_rate, num_iterations):
    parameters = [0, 0, 0]

    for i in range(num_iterations):
        parameters = step_gradient(data, learning_rate, parameters)

    return parameters


def step_gradient(data, learning_rate, parameters):
    a = learning_rate
    m = len(data)

    for point in data:
        x = point[0]
        y = point[1]
        h_x = hypothesis(parameters, x)
        parameters[0] -= (a / m) * (h_x - y)
        parameters[1] -= (a / m) * (h_x - y) * x
        parameters[2] -= (a / m) * (h_x - y) * x * x

    return parameters


def main():
    print("Test code goes here")


if __name__ == "__main__":
    main()
