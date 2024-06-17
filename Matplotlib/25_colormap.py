# ColorMap
'''
This colormap is called 'viridis' and as 
you can see it ranges from 0, which is a 
purple color, up to 100, which is a yellow color.
'''

'''
You can specify the colormap with the keyword 
argument cmap with the value of the colormap, 
in this case 'viridis' which is one of the built-in 
colormaps available in Matplotlib.
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2])
y = np.array([99,86,87,88,111])
colors = np.array([0,22,56,89,45])

plt.scatter(x,y,c = colors, cmap = 'viridis')
plt.show()