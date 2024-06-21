# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# Define a variable N
N = 500

#Construct the colormap
#There are six variations of the default theme,
#called deep, muted, pastel, bright, dark, and colorblind.
current_palette = sns.color_palette("pastel", n_colors=5) #0,1,2,3,4
cmap = ListedColormap(sns.color_palette(current_palette).as_hex())  
#RGB   #FFFFFF     #0000FF   #0C1245

print(type(cmap))
# Initialize the data

data1 = np.random.randn(N)     
data2 = np.random.randn(N)   
# Assume that there are 5 possible labels
colors = np.random.randint(0,5,N)
# =============================================================================
# x=[10,20,30]
# y=[25,26,67]
# c=[2,3]
# =============================================================================

# Create a scatter plot
#cmap is optional but if given it will be used only
# if list assign to c is float numbers
plt.scatter(data1, data2, c=colors, cmap=cmap)
#plt.scatter(x, y, c=c)
#plt.scatter(data1, data2)
# Add a color bar
plt.colorbar()

# Show the plot
plt.show()
