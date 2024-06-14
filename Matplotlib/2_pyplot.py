'''
Most of the Matplotlib utilities lies under 
the pyplot submodule, and are usually imported 
under the plt alias:
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,5])
y = np.array([0,1000])

plt.plot(x,y) #plots the graph
plt.show() # shows the plotted graph