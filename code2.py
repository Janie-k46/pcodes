# Dataset Construction
data2 = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'UnitsSold': [200, 230, 210, 250, 220, 260],
    'Revenue': [4000, 4600, 4200, 5000, 4400, 5200],
    'Customers': [120, 140, 130, 150, 135, 160]
}
df2 = pd.DataFrame(data2)

# (a) Revenue Growth Rate
df2['Growth_Rate'] = df2['Revenue'].pct_change() * 100

# (b) Dispersion Measures
print("\nCustomer Dispersion:\n", df2['Customers'].describe()[['std', 'min', 'max']])

# (c) Pearson Correlation (UnitsSold vs Revenue)
correlation = df2['UnitsSold'].corr(df2['Revenue'])
print(f"\nPearson Correlation: {correlation:.2f}")

# Visualization for Correlation
sns.scatterplot(x='UnitsSold', y='Revenue', data=df2)
plt.title('Correlation: Units Sold vs Revenue')
plt.show()