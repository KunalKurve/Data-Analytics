import matplotlib.pyplot as plt



#in stackplot we cannot give label so to ceate legend use following
slices=[7,8,6,11,7]
activities=['excercise', 'sleeping','eating','working','playing']
cols=['g','c','m','r','k']

#to draw piechart in anticlockwise direction
#counterclock=False

#plt.pie(slices,labels=activities,colors=cols,counterclock=False)
plt.pie(slices,labels=activities,colors=cols,shadow=True,explode=(0,0.2,0,0,0),startangle=90)

plt.title('This my first in matplotlib graph\nThis is on next line')
plt.show()




#plt.plot(x,y,label="First line")
#plt.plot(x1,y1,label="Second Line")
#plt.legend() #for legend add label in plot method
