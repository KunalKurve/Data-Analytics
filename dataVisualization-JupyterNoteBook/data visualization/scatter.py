import matplotlib.pyplot as plt

#students enrooled on particularday
enrollment=[10,100,70,34,56,110,124,145,120,111,45,35,4,7]
#classroom=[x for x in range(len(enrollment))
#day no
students=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]


plt.scatter(enrollment,students,label="This is scatter chart",color="green",marker="*",s=50)#s=marker size
#plt.plot(enrollment,students,color="red",label="students data")


plt.xlabel('enrollment')
plt.ylabel('Students')
plt.legend()
plt.title('This my first in matplotlib graph\nThis is on next line')
plt.show()




#plt.plot(x,y,label="First line")
#plt.plot(x1,y1,label="Second Line")
#plt.legend() #for legend add label in plot method
