# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 14:31:15 2020

@author: anilk
"""
print("Hello World!");

#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



enrollment=[10,100,70,34,56,110,124,145,120,111,45,35,4,7]
#classroom=[x for x in range(len(enrollment))
students=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
df=pd.DataFrame({"enrollments":enrollment,"student":students})
#plt.scatter(enrollment,students,label="This is scatter chart",color="green",marker="*",s=200)#s=marker size
#plt.plot(enrollment,students)
sns.scatterplot(x="enrollments", y="student" ,data=df)

plt.xlabel('plot number')
plt.ylabel('Important var')
plt.legend()
plt.title('This my first in matplotlib graph\nThis is on next line')
plt.show()