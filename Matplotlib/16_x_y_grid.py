# Add Grid Lines for x axis only


import matplotlib.pyplot as plt
import numpy as np

x = np.array([4,5,6,8])
y = np.array([1,5,9,6])

plt.title("Random data", loc='right')
plt.xlabel("X axis",color = 'blue', family = 'JetBrains Mono')
plt.ylabel("Y axis",color = 'blue', family = 'JetBrains Mono')

plt.grid(axis = 'x') # we write the axis parameter
plt.plot(x,y,'o-',ms = 10,color = 'orange', mfc = 'black', mec = 'black')
plt.show()

# NOTE : Same for Y axis.