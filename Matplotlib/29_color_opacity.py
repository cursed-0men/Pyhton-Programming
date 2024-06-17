# Combine Color Size and Alpha

# Create random arrays with 100 values for x-points, y-points, colors and sizes:

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
size = 10 * np.random.randint(100, size=(100))

'''100: This is the upper limit (exclusive) for the 
random integers. The function will generate integers 
in the range [0, 100), which means from 0 to 99 inclusive.'''

'''Size (100): This specifies the shape of the 
output array. In this case, size=(100) means 
the function will generate an array of 100 random integers.'''

plt.scatter(x,y,c = colors, s = size, alpha = 0.5, cmap = 'nipy_spectral')
plt.show()