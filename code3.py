from sklearn.linear_model import LinearRegression

# Dataset Construction
data3 = {
    'Temp': [24, 28, 22, 27, 23, 26],
    'Humidity': [60, 55, 70, 58, 72, 62],
    'EnergyUsage': [350, 400, 300, 420, 320, 380],
    'WindSpeed': [10, 12, 8, 11, 7, 9],
    'Location': ['Residential', 'Residential', 'Industrial', 'Residential', 'Industrial', 'Residential']
}
df3 = pd.DataFrame(data3)

# (a) Feature Transformation (Standardization)
df3['Temp_Scaled'] = (df3['Temp'] - df3['Temp'].mean()) / df3['Temp'].std()

# (b) Grouped Statistics
grouped_stats = df3.groupby('Location')['EnergyUsage'].mean()
print("\nMean Energy Usage by Location:\n", grouped_stats)

# (c) Regression Model
X = df3[['Temp', 'Humidity', 'WindSpeed']]
y = df3['EnergyUsage']
model = LinearRegression().fit(X, y)

print(f"\nRegression Intercept: {model.intercept_:.2f}")
print("Coefficients (Temp, Humidity, WindSpeed):", model.coef_)

# Visualization of Energy Usage across Locations
sns.barplot(x='Location', y='EnergyUsage', data=df3)
plt.title('Mean Energy Consumption by Location')
plt.show()