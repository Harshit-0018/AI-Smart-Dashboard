import numpy as np
from sklearn.linear_model import LinearRegression

def predict_future(data):
    X = np.arange(len(data)).reshape(-1, 1)
    y = data.values

    model = LinearRegression()
    model.fit(X, y)

    future_X = np.arange(len(data), len(data) + 10).reshape(-1, 1)
    predictions = model.predict(future_X)

    return predictions