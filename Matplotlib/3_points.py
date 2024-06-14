'''
Draw two points in the diagram, one at 
position (1, 3) and one in position (8, 10):
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,8])
y = np.array([3,10])

plt.plot(x,y,'o') # places dots at (1,3) and (8,10)
plt.show()