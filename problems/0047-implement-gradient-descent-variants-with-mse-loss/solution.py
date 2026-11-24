import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    m=X.shape[0]
    w=weights.copy()

    for _ in range(n_epochs):
        if method == 'batch':
            predictions = X@w
            errors = predictions - y
            gradient = (2/m)* (X.T @ errors)
            w-=learning_rate*gradient
        elif method == 'stochastic':
            for i in range(m):
                X_i=X[i:i+1]
                y_i=y[i:i+1]

                prediction = X_i @ w
                error = prediction - y_i
                gradient = 2*(X_i.T @ error)
                w-=learning_rate*gradient
        else:
            for start in range(0,m,batch_size):
                X_b = X[start:start+batch_size]
                y_b=y[start:start+batch_size]
                k = X_b.shape[0]

                predictions = X_b@w 
                errors=predictions - y_b
                gradient = (2/k)*(X_b.T@errors)
                w-=learning_rate*gradient
    
    # Your code here
    return w
