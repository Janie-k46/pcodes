import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset Construction
data1 = {
    'ID': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006'],
    'Pulse': [72, 85, 60, 78, 65, 90],
    'Systolic': [120, 135, 110, 125, 115, 140],
    'Cholesterol': [190, 220, 180, 200, 210, 230]
}
df1 = pd.DataFrame(data1)

# (a) Pulse Statistics
print(f"Pulse Mean: {df1['Pulse'].mean():.2f}")
print(f"Pulse Std Dev: {df1['Pulse'].std():.2f}")

# (b) Covariance and Eigen Decomposition
cov_matrix = df1[['Pulse', 'Systolic', 'Cholesterol']].cov()
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
print("\nEigenvalues:", eigenvalues)

# (c) Cholesterol Variability
print(f"Cholesterol Variance: {df1['Cholesterol'].var()}")
print(f"Cholesterol IQR: {stats.iqr(df1['Cholesterol'])}")

# (d) Z-score for Anomaly Detection
df1['Pulse_ZScore'] = stats.zscore(df1['Pulse'])
print("\nPulse Z-Scores:\n", df1[['ID', 'Pulse', 'Pulse_ZScore']])