# Create a simple Pandas Series from a dictionary:

import pandas as pd
import matplotlib.pyplot as plt
temperature = {'day_1':35,'day_2':40,'day_3':38}

var = pd.Series(temperature)
print(var)

plt.plot(var.index,var.values, marker = 'o', ls = 'solid')

plt.xlabel("Days")
plt.ylabel("Temperature(in C)")

plt.show()
# day_1    35
# day_2    40
# day_3    38
# dtype: int64
# NOTE: The keys of the dictionary become the labels.