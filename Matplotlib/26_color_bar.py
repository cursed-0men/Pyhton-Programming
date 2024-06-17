# showing colorbar alongside plot
'''
You can include the colormap in the drawing 
by including the plt.colorbar() statement
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2])
y = np.array([99,86,87,88,111])
colors = np.array([56,22,72,10,20])

plt.scatter(x,y,c = colors, cmap='viridis')
plt.colorbar()
plt.show()

# NOTE : Some Cmaps names : viridis, Accent, Greens, Blues, Binary, Set1, Set2, Set3, flag, hot, jet, winter, nipy_spectral