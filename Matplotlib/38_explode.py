# Explode
# The explode parameter, if specified, and not None, must be an array with one value for each wedge.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([35,25,25,15])
labelzz = ["Apples", "Bananas", "Cherries", "Dates"]
explosion = [0.1,0,0,0]

plt.pie(x,labels=labelzz, startangle=90, explode=explosion)
plt.show()