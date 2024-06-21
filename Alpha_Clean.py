# -*- coding: utf-8 -*-
"""
Perform the pre-requisite viz. :
Assessing the Data

i. Data cleaning
ii. Inspection
iii. Manipulation if required
iv. Extracting meaningful visualization based on your understanding
v. Data consolidation if required

Q1. Find out the alternative sources of fuel available in 2008 & 2018 respectively and by how much?
Q2. Is there any improvement in ‘fuel economy’ with respect to vehicle class from 2008 to 2018, perform the necessary steps to examine?
Q3. Is there any change in characteristics of SmartWay Vehicles ?
Q4. Which all features are associated with better fuel economy?
Q5. How much improvement is there in miles/gallon or mpg? Also, which vehicle has improved the most?

"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('all_alpha_08.xls')
df1.info()

df2 = pd.read_csv('all_alpha_18.xls')
df2.info()

df3 = pd.read_csv('clean_08.xls')
df3

df4 = pd.read_csv('clean_18.xls')
df4

# For 2008
missing_values_count1 = df1.isnull().sum()
print(missing_values_count1)

# For 2018
missing_values_count2 = df2.isnull().sum()
print(missing_values_count2)

#2008
df1.fillna({'Trans':'Unknown', 'Drive': 'Unknown'}, inplace = True)
new1_missing_values_count1 = df1.isnull().sum()
print(new1_missing_values_count1)

df1.fillna(df1['Unadj Cmb MPG'].mean(), inplace = True)
print("\nAfter data cleaning. Missing value count:")
new2_missing_values_count1 = df1.isnull().sum()
print(new2_missing_values_count1)

#2018
df2.fillna(df2['Displ'].mean(), inplace = True)
df2.fillna(df2['Cyl'].mean(), inplace = True)
print("\nAfter data cleaning. Missing value count:")
new_missing_values_count2 = df2.isnull().sum()
print(new_missing_values_count2)

print(df1.corr())

plt.figure(figsize = (12,8))
sns.barplot(df1, x="Displ", y="Unadj Cmb MPG")
plt.xticks(rotation = 90)
plt.show()

print(df2.corr())
# Correlation of alpha 2018

correlation2 = df2.select_dtypes(exclude = object).corr()
print(correlation2)

cmap = sns.diverging_palette(10, 220, as_cmap = True)
sns.heatmap(correlation2, vmin = -1.0, annot = True, vmax = 1.0, square = True, cmap = cmap)
plt.show()


# Q1
print(df3["fuel"].value_counts())
print(df4["fuel"].value_counts())

df3['Year'] = 2008
df4['Year'] = 2018
fuel_df = pd.concat([df3, df4], axis = 0)
print(fuel_df)

# Q2
fuel_eco_2008 = df3.groupby('veh_class')['cmb_mpg'].mean()
fuel_eco_2018 = df4.groupby('veh_class')['cmb_mpg'].mean()

fuel_improvement = fuel_eco_2018 - fuel_eco_2008

fuel_improvement.plot.pie(figsize = (12,6), autopct = '%1.1f')
plt.title('Improvement in ‘fuel economy’ with respect to vehicle class from 2008 to 2018')
plt.xlabel('Vehicle Class')
plt.ylabel('Improvement in Combined MPG')
plt.show()

# Q3
smartway_2008 = df3[df3['smartway'] != 'no']
smartway_2018 = df4[df4['smartway'] != 'No']

change_in_smartway = smartway_2018.describe() - smartway_2008.describe()
print(change_in_smartway)

# Q4
correlation = df3.select_dtypes(exclude = object).corr()
print(correlation)

cmap = sns.diverging_palette(10, 220, as_cmap = True)
sns.heatmap(correlation, vmin = -1.0, annot = True, vmax = 1.0, square = True, cmap = cmap)
plt.show()

# Q5
avg_mpg_08 = df3.groupby('model')['cmb_mpg'].mean()
avg_mpg_18 = df4.groupby('model')['cmb_mpg'].mean()

mpg_improvement = avg_mpg_18 - avg_mpg_08

most_improved_model = mpg_improvement.idxmax()
most_improved_value = mpg_improvement.max()

print(most_improved_model)
print(most_improved_value)