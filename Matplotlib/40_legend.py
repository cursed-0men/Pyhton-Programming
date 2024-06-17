# Legend and with header
# To add a list of explanation for each wedge, use the legend() function.

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(200, size = (5))
fruits = ['apple','banana','cherry','kiwi','watermelon']

plt.pie(x,labels=fruits)
# without header 
# plt.legend()

# with header
plt.legend(title = 'Fruits')
plt.show()