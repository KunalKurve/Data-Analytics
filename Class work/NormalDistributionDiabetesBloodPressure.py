import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import os

# Read the dataset
data = pd.read_csv("diabetes.csv")

# Extract the BloodPressure column into a new series
blood_pressure_series = data['BloodPressure']
print(blood_pressure_series.head())

# save the dataframe for offline viewing
if os.path.exists("deletethis-1.csv"):
    os.remove("deletethis-1.csv")  # Remove the file if it exists

data.to_csv("deletethis-1.csv", index=False)

# Calculate mean and standard deviation
mu, std = blood_pressure_series.mean(), blood_pressure_series.std()

# Calculate z-score for each value
z_scores = (blood_pressure_series - mu) / std

# Plot normal distribution graph of BloodPressure
plt.figure(figsize=(12, 6))

# Histogram
plt.subplot(1, 2, 1)
plt.hist(blood_pressure_series, bins=20, density=True, alpha=0.6, color='b', edgecolor='black')

# Fit a normal distribution to the data
x = np.linspace(blood_pressure_series.min(), blood_pressure_series.max(), 100)
p = stats.norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
plt.title(title)
plt.xlabel('Blood Pressure')
plt.ylabel('Density')
plt.grid(True)

# QQ Plot
plt.subplot(1, 2, 2)
stats.probplot(blood_pressure_series, dist="norm", plot=plt)
plt.title('QQ Plot')

plt.tight_layout()
plt.show()

# Plot graph showing mean +- 3 SD
plt.figure(figsize=(10, 6))
plt.hist(blood_pressure_series, bins=20, density=True, alpha=0.6, color='b', edgecolor='black')

# Fit a normal distribution to the data
x = np.linspace(blood_pressure_series.min(), blood_pressure_series.max(), 1000)
p = stats.norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
plt.title(title)
plt.xlabel('Blood Pressure')
plt.ylabel('Density')
plt.grid(True)

# Plot mean +- 3 SD
for i in range(1, 4):
    plt.axvline(mu - i*std, color='r', linestyle='--', linewidth=2, label=f'Mean - {i} SD')
    plt.axvline(mu + i*std, color='r', linestyle='--', linewidth=2)

plt.legend()
plt.show()

# Check if mean +- 1SD, mean +- 2SD, and mean +- 3SD satisfy the empirical rule
within_1sd = (z_scores <= 1) & (z_scores >= -1)
within_2sd = (z_scores <= 2) & (z_scores >= -2)
within_3sd = (z_scores <= 3) & (z_scores >= -3)

percentage_within_1sd = np.sum(within_1sd) / len(blood_pressure_series) * 100
percentage_within_2sd = np.sum(within_2sd) / len(blood_pressure_series) * 100
percentage_within_3sd = np.sum(within_3sd) / len(blood_pressure_series) * 100

print(f"Percentage of data within mean ± 1 SD: {percentage_within_1sd:.2f}%")
print(f"Percentage of data within mean ± 2 SD: {percentage_within_2sd:.2f}%")
print(f"Percentage of data within mean ± 3 SD: {percentage_within_3sd:.2f}%")

# Create DataFrame to store BloodPressure, z-score, and within_1sd, within_2sd, within_3sd flags
result_df = pd.DataFrame({
    'BloodPressure': blood_pressure_series,
    'z_score': z_scores,
    'within_1sd': within_1sd,
    'within_2sd': within_2sd,
    'within_3sd': within_3sd
})

print(result_df.head())

if os.path.exists("deletethis-2.csv"):
    os.remove("deletethis-2.csv")  # Remove the file if it exists

result_df.to_csv("deletethis-2.csv", index=False)

# Outlier z-score box plot
plt.figure(figsize=(8, 6))
plt.boxplot(result_df['z_score'], vert=False, flierprops=dict(marker='*', markerfacecolor='red', markersize=10))
plt.xlabel('Z-score')
plt.title('Boxplot of Z-scores')
plt.grid(True)
plt.show()
