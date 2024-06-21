'''
Here we use chi2_contingency
Purpose: It is used for conducting a chi-square test of independence or association between two categorical variables by analyzing a contingency table (also known as a two-way table)
'''

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as ws
from scipy.stats import chi2_contingency

df = pd.read_csv("heart_failure_clinical_records_dataset.csv")
print(df.head())

print("Against Age")
print(chi2_contingency(pd.crosstab(index=df['age'], columns=df['DEATH_EVENT'])))
''' This will give a table like this:
DEATH_EVENT   0   1
age
40.000        7   0
41.000        1   0
42.000        6   1
43.000        1   0
44.000        2   0
45.000       13   6
'''
# test statistic > critical value and p-value is also low, so reject H0 for age

print (pd.crosstab(index=df['age'], columns=df['DEATH_EVENT']))

print("Against Anaemia")
print(chi2_contingency(pd.crosstab(index=df['anaemia'], columns=df['DEATH_EVENT'])))

print("Against Diabetes")
print(chi2_contingency(pd.crosstab(index=df['diabetes'], columns=df['DEATH_EVENT'])))

print("Against High Blood Pressure")
print(chi2_contingency(pd.crosstab(index=df['high_blood_pressure'], columns=df['DEATH_EVENT'])))

print("Against Sex")
print(chi2_contingency(pd.crosstab(index=df['sex'], columns=df['DEATH_EVENT'])))

# The only column that has relationship with Death Events is age, that we can also see in graph below

plt.figure(figsize=(20,6))
title = plt.title('Survival and Deaths by Age', fontsize=20)
title.set_position([0.5, 1.15])
ax = sns.countplot(x="age", hue="DEATH_EVENT", data=df)
ax.set_xlabel('Age')
ax.set_ylabel('Count')
a = ax.set_xticklabels(ax.get_xticklabels(), rotation=0, horizontalalignment='center')
plt.show()

# Exercise: Improve this graph

# Exercise: Try it for other variables

