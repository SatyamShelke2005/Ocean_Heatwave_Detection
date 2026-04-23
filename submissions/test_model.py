import numpy as np

def predict(X_train, y_train, X_test):
    return np.random.randint(0, 2, len(X_test))
