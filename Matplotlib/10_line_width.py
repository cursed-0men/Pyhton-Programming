'''
You can use the keyword argument 
linewidth or the shorter lw to 
change the width of the line.
'''

import matplotlib.pyplot as plt
import numpy as np

y = np.array([3, 8, 1, 10])

plt.plot(y,'o-m', lw = 10) #plots the graph
plt.show() # shows the plotted graph
