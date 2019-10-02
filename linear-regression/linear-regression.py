from numpy import *

def error(data, a, b):
    error = 0.0
    for i in range(len(data)):
        x = data[i, 0]
        y = data[i, 1]
        error += (y - (a * x + b)) ** 2
    return error / float(len(data))

def gradient_descent(data, a, b, learning_rate, num_iterations):
    for i in range(num_iterations):
        a, b = step_gradient(data, a, b, learning_rate)
    return [a, b]

def step_gradient(data, a, b, learning_rate):
    a_gradient = 0.0
    b_gradient = 0.0
    for i in range(len(data)):
        x = data[i, 0]
        y = data[i, 1]
        a_gradient += -2 * (y - a * x - b) * x
        b_gradient += -2 * (y - a * x - b)
    new_a = a - a_gradient * learning_rate / float(len(data))
    new_b = b - b_gradient * learning_rate / float(len(data))
    return [new_a, new_b]
