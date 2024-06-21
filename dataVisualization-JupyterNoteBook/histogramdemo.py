# -*- coding: utf-8 -*-
"""
Created on Thu May 27 08:53:47 2021

@author: anilk
"""
import matplotlib.pyplot as plt
import numpy as np
x=[100,200,300]
y=[50,34,40,10,33,32,32,31,23,45,22,25,45,44,27,42,34,35,37,44,46,42]

#to change the color of line use color attribute otherwise default color will be assigned

#plt.plot(x,y,color="green")
plt.hist(y,bins=4)
#plt.xticks(np.linspace(start=100,stop=300,num=5,endpoint=True))
plt.yticks(np.linspace(start=1,stop=7,num=7,endpoint=True))
#this is for giving label to x axis
plt.xlabel('plot number')
#this is for giving label to y axis
plt.ylabel('Important var')
#plt.legend()
plt.grid()
plt.title('This my first in matplotlib graph\nThis is on next line')
plt.show()

