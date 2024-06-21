# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:41:01 2019

@author: anilk
"""
print("Hello World!");

#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fake = pd.DataFrame({'cat': ['red', 'green', 'blue'], 'val': [1, 2, 3]})
# =============================================================================
# x=fake['cat']
# y=fake['val']
# plt.bar(x,y)
# =============================================================================
ax = sns.barplot(x = 'cat', y = 'val', 
              data = fake, 
              color = 'black')
#plt.xlabel("common xlabel")
#plt.ylabel("common ylabel")
ax.set(xlabel='common xlabel', ylabel='common ylabel')
#ax.get_xticklabels() this is needed because of string labels are there
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
#ax.set(xlabel='common xlabel', ylabel='common ylabel', title='some title')
plt.show()





