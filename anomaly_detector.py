import random
import numpy as np
import matplotlib.pyplot as plt

def data_stream_generator(mean=0, std_dev=1, num_samples=100):
    """Simulate a data stream with a normal distribution and random noise."""
    for _ in range(num_samples):
        # Simulate normal data with seasonal variation
        seasonal_effect = 10 * np.sin(2 * np.pi * _ / 50)  # Seasonal pattern
        noise = random.gauss(0, std_dev)
        yield mean + seasonal_effect + noise

def detect_anomaly(data_point, mean, std_dev, threshold=3):
    """Detect anomalies based on Z-score."""
    if std_dev == 0:  # Prevent division by zero
        return False
    z_score = (data_point - mean) / std_dev
    return abs(z_score) > threshold

def monitor_data_stream(num_samples=100):
    """Monitor the data stream for anomalies and visualize results."""
    data_points = []
    anomalies = []

    for data_point in data_stream_generator(num_samples=num_samples):
        data_points.append(data_point)

        # Calculate mean and std deviation for the current window
        if len(data_points) > 10:  # Consider last 10 points
            recent_data = data_points[-10:]
            mean = np.mean(recent_data)
            std_dev = np.std(recent_data)

            if detect_anomaly(data_point, mean, std_dev):
                anomalies.append(data_point)
                print(f"Anomaly detected: {data_point}")

    return data_points, anomalies

def visualize_data(data_points, anomalies):
    """Visualize the data stream and detected anomalies."""
    plt.figure(figsize=(10, 5))
    plt.plot(data_points, label='Data Stream', color='blue')
    plt.scatter([i for i, val in enumerate(data_points) if val in anomalies],
                anomalies, color='red', label='Anomalies', zorder=5)
    plt.title('Data Stream with Detected Anomalies')
    plt.xlabel('Sample Index')
    plt.ylabel('Value')
    plt.axhline(y=np.mean(data_points) + 3*np.std(data_points), color='r', linestyle='--', label='Upper Threshold')
    plt.axhline(y=np.mean(data_points) - 3*np.std(data_points), color='g', linestyle='--', label='Lower Threshold')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    num_samples = 100
    data_points, anomalies = monitor_data_stream(num_samples)
    visualize_data(data_points, anomalies)