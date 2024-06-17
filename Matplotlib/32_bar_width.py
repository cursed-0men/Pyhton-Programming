# Bar Width
# The bar() takes the keyword argument width to set the width of the bars

import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A','B','C','D'])
y = np.random.randint(100, size=(4))

plt.bar(x,y,width = 0.25)
plt.show()

# NOTE : For horizontal bars, use height instead of width.