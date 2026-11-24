import numpy as np

def sgd_update(X, y, weights, learning_rate, n_iter):
    n_samples = X.shape[0]
    w = weights.astype(float).copy()

    for i in range(n_iter):
        idx = i % n_samples
        x_i = X[idx]
        y_i = y[idx]

        # 1. Прогноз для одного объекта (скалярное произведение векторов)
        y_pred = np.dot(x_i, w)

        # 2. Градиент MSE для одного объекта: 2 * (y_pred - y_i) * x_i
        error = y_pred - y_i
        gradient = 2 * error * x_i

        # 3. Обновление весов
        w -= learning_rate * gradient

    return w.tolist()