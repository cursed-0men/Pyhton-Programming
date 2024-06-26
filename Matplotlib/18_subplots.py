# Display Multiple Plots
# With the subplot() function you can draw multiple plots in one figure:

'''
plt.subplot(1, 2, 1)
#the figure has 1 row, 2 columns, and 
this plot is the first plot.

plt.subplot(1, 2, 2)
#the figure has 1 row, 2 columns, and 
this plot is the second plot.

'''

import matplotlib.pyplot as plt
import numpy as np

# plot 1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(1,2,1)
plt.plot(x,y,color = 'blue')



# plot 2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(1,2,2)
plt.plot(x,y,color = 'orange')


plt.tight_layout()
plt.show()