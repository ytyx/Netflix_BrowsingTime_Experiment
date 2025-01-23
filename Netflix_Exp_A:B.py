# Import required libraries for A/B testing
from scipy.stats import ttest_ind
import numpy as np
import pandas as pd

# Data
# group_A = pd.read_csv('Browsing time for current homepage')
# group_B = pd.read_csv('Browsing time for redesigned homepage')

# Combine into one DataFrame
ab_data = pd.DataFrame({
    'BrowsingTime': np.concatenate([group_A, group_B]),
    'Group': ['A'] * len(group_A) + ['B'] * len(group_B)
})

# Calculate summary statistics
summary_stats = ab_data.groupby('Group')['BrowsingTime'].agg(['mean', 'std', 'count'])
print("Summary Statistics for A/B Testing:")
print(summary_stats)

# Conduct a two-sample t-test to compare the means
t_stat, p_value = ttest_ind(group_A, group_B, equal_var=False)
print("\nA/B Testing Results:")
print(f"T-Statistic: {t_stat:.3f}")
print(f"P-Value: {p_value:.5f}")

# Evaluate the lift
mean_A = np.mean(group_A)
mean_B = np.mean(group_B)
lift = ((mean_A - mean_B) / mean_A) * 100
print(f"\nLift in Browsing Time Reduction: {lift:.2f}%")

# Visualize the A/B testing results
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.boxplot(data=ab_data, x='Group', y='BrowsingTime', palette="Set2")
plt.title("A/B Testing Results: Browsing Time Comparison", fontsize=16)
plt.ylabel("Browsing Time (minutes)")
plt.xlabel("Group")
plt.show()

# Interpretation of results
if p_value < 0.05:
    print("\nThe difference between Group A and Group B is statistically significant (p < 0.05).")
    print("The redesigned homepage significantly reduced browsing time.")
else:
    print("\nThe difference between Group A and Group B is not statistically significant (p ≥ 0.05).")
    print("No significant improvement observed with the redesigned homepage.")
