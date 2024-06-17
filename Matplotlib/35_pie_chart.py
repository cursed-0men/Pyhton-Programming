# Matplotlib Pie Charts
# With Pyplot, you can use the pie() function to draw pie charts:

import matplotlib.pyplot as plt
import numpy as np

x = np.array([10,20,30,40])
# x = np.random.randint(100, size=(4))

plt.pie(x)
plt.show()


# NOTE : 
'''
The size of each wedge is determined by 
comparing the value with all the other values, 
by using this formula:

The value divided by the sum of all values: x/sum(x)

'''