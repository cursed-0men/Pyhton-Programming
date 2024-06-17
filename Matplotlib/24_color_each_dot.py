# Set your own color of the markers:

'''
You can even set a specific color for each 
dot by using an array of colors as value 
for the c argument:
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8])
y = np.array([99,86,87])
colors = np.array(["black","blue", "orange"])

plt.scatter(x,y,c = colors)
plt.show()

# NOTE : You cannot use the color argument for this, only the c argument.