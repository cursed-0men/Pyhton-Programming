# Horizontal Bars
'''
If you want the bars to be displayed 
horizontally instead of vertically, use the barh()

'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A','B','C','D'])
y = np.random.randint(100, size=(4)) # generated random values

plt.barh(x,y, color = 'green', alpha = 0.85)
plt.show()