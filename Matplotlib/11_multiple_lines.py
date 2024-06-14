'''
You can plot as many lines as you like 
by simply adding more plt.plot() functions:
'''

import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([100, 50, 70, 20])

plt.plot(y1,'o:',color = 'Orange')
plt.plot(y2,'o--',color = 'Black')
plt.plot(y3,'o-', color = 'Blue')

plt.show()