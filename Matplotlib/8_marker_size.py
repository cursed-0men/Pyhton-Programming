'''
You can use the keyword argument markersize 
or the shorter version, ms to set the size 
of the markers:
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.array([8,5,3,7])
y = np.array([4,3,2,8])

plt.plot(x,y,'o--k',ms = 20)
plt.show()