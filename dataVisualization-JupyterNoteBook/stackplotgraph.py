import matplotlib.pyplot as plt
import numpy as np

days=[1,2,3,4,5]
sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,7,2]
playing=[8,5,7,8,13]

arr=np.array(days)
#in stackplot we cannot give label so to ceate legend use following

plt.plot([],[],color='m', label="sleeping",linewidth=5)
plt.plot([],[],color='c', label="Eating",linewidth=5)
plt.plot([],[],color='r', label="Working",linewidth=5)
plt.plot([],[],color='b', label="Playing",linewidth=5)
#this doesnot hav label attribute, s indicates size of marker
plt.stackplot(days,sleeping,eating,working,playing,
                            colors=['m','c','r','b'])

# plt.bar(arr-0.5,sleeping,width=0.2)
# plt.bar(arr+0.5,working,width=0.2)
# plt.xticks(np.linspace(start=1,stop=6,num=6,endpoint=True))
# plt.yticks(np.linspace(start=2,stop=14,num=10,endpoint=True))
plt.xlabel('plot number')
plt.ylabel('Important var')
plt.legend(loc="upper left")
plt.title('This my first in matplotlib graph\nThis is on next line')
plt.show()




#plt.plot(x,y,label="First line")
#plt.plot(x1,y1,label="Second Line")
#plt.legend() #for legend add label in plot method
