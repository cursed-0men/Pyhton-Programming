'''
You can use the keyword argument 
markeredgecolor or the shorter mec 
to set the color of the edge of the markers:
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array([4,5,6,8,9])
y = np.array([100,456,82,2,99])

plt.plot(x,y,'o:m',ms = 20, mec = 'k')
plt.show()