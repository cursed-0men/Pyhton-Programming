# Shadow
# Add a shadow to the pie chart by setting the shadows parameter to True

import matplotlib.pyplot as plt
import numpy as np

x = np.array([35,25,25,15])
label = ["Apples", "Bananas", "Cherries", "Kiwi"]
colorss = ['red','Yellow','magenta','green']
explosion = [0.01,0.01,0.1,0.01]

plt.pie(x,explode=explosion, labels=label, colors=colorss, startangle=60, shadow = False)
plt.show()