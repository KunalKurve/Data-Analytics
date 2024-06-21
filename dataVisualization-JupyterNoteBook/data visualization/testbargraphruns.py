# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 19:06:00 2021

@author: anilk
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
runs={
      "year":[2010,2011,2014,2016,2017],
      "runs":[100,50,150,30,40]
      }

df=pd.DataFrame(runs)
plt.bar(df['year'],df['runs'])
plt.xticks(np.linspace(2009,2018,num=10,endpoint=True),rotation="45")
plt.show()