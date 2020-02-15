def hypothesis(parameters, x, y):
    return parameters[0] + parameters[1] * x + parameters[2] * y


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
        z = point[2]
        h_xy = hypothesis(parameters, x, y)
        parameters[0] -= (a / m) * (h_xy - z)
        parameters[1] -= (a / m) * (h_xy - z) * x
        parameters[2] -= (a / m) * (h_xy - z) * y

    return parameters


def main():
    print("Test code goes here")


if __name__ == "__main__":
    main()
