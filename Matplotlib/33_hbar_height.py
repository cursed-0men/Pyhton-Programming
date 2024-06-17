# Draw 4 very thin horizontal bars:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A','B','C','D'])
y = np.random.randint(200, size=(4))

plt.barh(x, y, height=0.2, color = 'magenta', alpha = 0.5)
plt.show()
