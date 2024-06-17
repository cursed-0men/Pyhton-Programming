# Histogram

# A histogram is a graph showing frequency distributions.
# It is a graph showing the number of observations within each given interval.

# In Matplotlib, we use the hist() function to create histograms.

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170,10,250)
'''here 
170 -> Mean
10 -> Standard Deviation
250 -> Total entries/Observstions
'''

plt.hist(x)
plt.title("Normal distribution", size = 15)
plt.show()