import numpy as np

def detect_anomalies(data):
    mean = np.mean(data)
    std = np.std(data)

    anomalies = []
    for i, value in enumerate(data):
        if abs(value - mean) > 2 * std:
            anomalies.append((i, value))

    return anomalies