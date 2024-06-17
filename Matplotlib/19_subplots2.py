# Draw 2 plots on top of each other

import matplotlib.pyplot as plt
import numpy as np
 
# plot 1
x = np.array([1,5,9,7])
y = np.array([5,6,8,7])

plt.subplot(2,1,1)
plt.plot(x,y,'o-', color = 'blue', mec = 'Black', mfc = 'Black')
plt.grid(ls = '--')

# plot 2
x = np.array([4,7,1,2])
y = np.array([1,8,2,3])

plt.subplot(2,1,2)
plt.plot(x,y,'o-', color = 'orange', mec = 'Blue', mfc = 'Blue')
plt.grid(ls = '--')


plt.show()
