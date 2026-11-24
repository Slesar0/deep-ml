import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape
    y = y.reshape(-1, 1)  # Ensure y is a column vector
    theta = np.zeros((n, 1))  # Initialize weights to zeros

    for _ in range(iterations):
        y_pred = X@theta
        error = y_pred-y
        gragient = (1/m) * (X.T@error)

        theta = theta - alpha * gragient
    # Your code here: implement gradient descent

    return theta.flatten()