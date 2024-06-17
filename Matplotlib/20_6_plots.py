# Draw 6 plots

import matplotlib.pyplot as plt
import numpy as np

# plot 1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,3,1)
plt.plot(x,y)
plt.title("Plot 1 ", family = "JetBrains Mono", size = '15')


# plot 2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2,3,2)
plt.plot(x,y)
plt.title("Plot 2 ", family = "JetBrains Mono", size = '15')


# plot 3
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,3,3)
plt.plot(x,y)
plt.title("Plot 3 ", family = "JetBrains Mono", size = '15')

# plot 4
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2,3,4)
plt.plot(x,y)
plt.title("Plot 4 ", family = "JetBrains Mono", size = '15')


# plot 5
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2,3,5)
plt.plot(x,y)
plt.title("Plot 5 ", family = "JetBrains Mono", size = '15')


# plot 6
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2,3,6)
plt.plot(x,y)
plt.title("Plot 6 ", family = "JetBrains Mono", size = '15')


plt.tight_layout()
plt.show()

# NOTE : Keep plt.title at last