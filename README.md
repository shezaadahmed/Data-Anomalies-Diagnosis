# Project Description: 
The goal of this project is to develop a Python script that detects anomalies in a continuous data stream, simulating floating-point numbers. This data could represent metrics such as financial transactions or system metrics, with a focus on identifying unusual patterns. This project also deeply focuses on developing a robust Python script capable of detecting anomalies in real-time data streams, which can be critical for applications such as financial monitoring and
system performance analysis.
# Chosen Algorithms:
**1). Statistical Methods:** Z-Score <br>
**2). Machine Learning:** K-Means Clustering, Isolation Forest <br>
**3). Neural Networks:** Autoencoders, Recurrent Neural Networks (RNN’s) <br>
**4). Time Series Analysis:** Seasonal Decomposition of Time Series
**5). Ensemble Methods:** Random Cut Forest.
# Effectiveness:
**1). Real-Time Detection:** It enables immediate anomaly detection as data is
processed. <br>
**2). Immediate Results:** Anomalies are detected on-the-fly, allowing for quick
responses to potential issues. <br>
**3). User-Friendly:** The threshold concept is intuitive, making it accessible for users
with varying technical backgrounds. <br>
**4). Simplicity:** This algorithm is easy to implement and runs efficiently in real-time
applications.
# Software Frameworks and Libraries:
**Data Processing**
```bash
- pandas, numpy - Data manipulation
- scikit-learn - Standard ML algorithms
- pyod – Specialized anomaly detection library
- river – Online ML & anomaly detection on data streams
```
**Streaming / Real-Time Processing**
```bash
- Kafka + kafka-python – Distributed streaming
- Spark Streaming or Apache Flink (optional for large-scale data)
```
**Visualization**
```bash
- matplotlib, seaborn, plotly – Visualize anomalies and metrics
```
**Monitoring & Logging**
```bash
- logging, mlflow, TensorBoard (if using deep learning)
```
**Evaluation**
```bash
- sklearn.metrics – Precision, recall, F1-score, ROC-AUC for anomaly detection
```


