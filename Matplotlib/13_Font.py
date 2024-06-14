'''
You can use the fontdict parameter in 
xlabel(), ylabel(), and title() to set 
font properties for the title and labels.
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'JetBrains Mono', 'color':'Blue', 'size':'20'}
font2 = {'family':'JetBrains Mono', 'color':'Orange', 'size':'20'}

plt.title("Sports Watch Data", fontdict=font1)
plt.xlabel("Average Pulse", fontdict=font2)
plt.ylabel("Calorie Burnage", fontdict=font2)

plt.plot(x, y, 'o-', color = 'Blue')
plt.show()