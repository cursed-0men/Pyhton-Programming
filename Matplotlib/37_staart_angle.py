# Start Angle
'''
As mentioned the default start angle 
is at the x-axis, but you can change 
the start angle by specifying a startangle parameter.

The startangle parameter is defined with 
an angle in degrees, default angle is 0.

'''

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(40, size = (5))
labelz = np.array(["Apples", "Bananas", "Cherries", "Dates", "Kiwis"])

plt.pie(x, labels = labelz, startangle = 135)
plt.show()