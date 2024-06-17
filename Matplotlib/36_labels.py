# Labels

# The labels parameter must be an array with one label for each wedge

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(50, size = (6))
names = np.array(['apple', 'banana', 'cherry', 'papaya', 'kiwi', 'mango'])

plt.pie(x, labels = names)
plt.show()

# NOTE : By default the plotting of the first wedge starts from the x-axis and moves counterclockwise.
