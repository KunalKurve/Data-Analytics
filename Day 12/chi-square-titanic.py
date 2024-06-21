import pandas as pd
from scipy.stats import chi2_contingency

df = pd.read_csv("titanic-tested.csv")

'''
Null Hypothesis (H0): Assumes there is no association between the variables  we re testing (passenger class and survival).
Alternative Hypothesis (Ha): Assumes there is an association between the variables.
'''

# Create a contingency table
contingency_table = pd.crosstab(df["Pclass"], df["Survived"])

print(contingency_table)

# Perform the Chi-square test
chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

# Print the results
print("Chi-square statistic:", chi2_stat)
print("p-value:", p_value)
print("Degrees of freedom:", dof)

# Interpretation
if p_value < 0.05:
    print("Reject H0, so there is a statistically significant association between passenger class and survival (p < 0.05).")
else:
    print("Do not reject H0, so there is no statistically significant association between passenger class and survival (p >= 0.05).")
