import matplotlib.pyplot as plt

x=[1,2,3]
y=[5,7,4]
x2=[1,2,3]
y2=[10,13,14]
#to change the color of line use color attribute otherwise default color will be assigned

plt.plot(x,y,label="First line",color="green")
plt.plot(x2,y2,label="Second Line",color="brown")
#this is for giving label to x axis
plt.xlabel('plot number')
#this is for giving label to y axis
plt.ylabel('Important var')
plt.legend()
#plt.grid()
plt.title('This my first in matplotlib graph\nThis is on next line')
plt.show()


#x2=[1,2,3]
#y2=[10,13,14]
#plt.plot(x,y,label="First line")
#plt.plot(x1,y1,label="Second Line")
#plt.legend() #for legend add label in plot method
