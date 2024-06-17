# Matplotlib Bars
# you can use the bar() function to draw bar graphs.

import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A', 'B' ,'C', 'D'])
y = np.random.randint(4,size=(4)) # generates random values

plt.bar(x,y,color = 'Orange')
plt.show()