import numpy as np
import time
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt


def simulate_data_stream(num_points=1000):
    for _ in range(num_points):
        value = np.sin(time.time() * 0.1) + np.random.normal(0, 0.1)
        yield value
        time.sleep(0.1)


def detect_anomalies(data_stream):
    model = IsolationForest(contamination=0.05)
    values = []

    for value in data_stream:
        values.append(value)
        if len(values) > 50:  # Fit the model every 50 points
            predictions = model.fit_predict(np.array(values).reshape(-1, 1))
            for i, pred in enumerate(predictions):
                if pred == -1:
                    print(f"Anomaly detected: {values[i]}")


def visualize_data(data_stream):
    plt.ion()
    plt.figure()

    for value in data_stream:
        plt.scatter(time.time(), value)
        plt.pause(0.1)


# Run the simulation and detection
data_stream = simulate_data_stream()
detect_anomalies(data_stream)
visualize_data(data_stream)

