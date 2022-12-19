import numpy as np


def my_svm(dataset, label):
    rate = 1  # rate for gradient descent
    epochs = 10000  # no of iterations
    weights = np.zeros(dataset.shape[1])  # Create an array for storing the weights

    # Min. the objective function(Hinge loss) by gradient descent
    for epoch in range(1, epochs):
        for n, data in enumerate(dataset):
            if (label[n] * np.dot(dataset[n], weights.T)) < 1:
                weights = weights + rate * ((dataset[n] * label[n]) + (-2 * (1 / epoch) * weights))
            else:
                weights = weights + rate * (-2 * (1 / epoch) * weights)

    return weights


def predict(test_data, weights):
    results = []
    for data in test_data:
        result = np.dot(data, weights)
        results.append(-1 if result < 0 else 1)
    return results