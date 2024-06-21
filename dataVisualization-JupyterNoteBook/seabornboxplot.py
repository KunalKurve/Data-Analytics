# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 16:16:00 2021

@author: anilk
"""

#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



import seaborn as sns
# Load the data

tips = sns.load_dataset("tips")

sns.boxplot(x='day',y='total_bill',data=tips)
plt.show()

tips.info()

sns.countplot(x="sex",data=tips)
plt.show()


sns.countplot(x="day",hue="sex",data=tips)
plt.show()

sns.distplot(x=tips['tip'],kde=True,color="darkred",bins=20)

sns.heatmap(tips.isnull(),yticklabels=False,cmap="viridis")


