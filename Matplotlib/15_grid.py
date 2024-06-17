# Add Grid Lines to a Plot

'''
With Pyplot, you can use the grid() 
function to add grid lines to the plot.
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array([4,5,6,8])
y = np.array([1,5,9,6])

plt.title("Random data", loc='right')
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.grid()
plt.plot(x,y,'o-',ms = 10,color = 'orange', mfc = 'black', mec = 'black')
plt.show()