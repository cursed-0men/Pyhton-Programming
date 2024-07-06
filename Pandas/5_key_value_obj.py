# Key/Value Objects as Series
# You can also use a key/value object, like a dictionary, when creating a Series.

import pandas as pd

calories = {"day 1" : 500, "day 2" : 600, "day 3" : 700}
data = pd.Series(calories)
print(data)

# NOTE : The keys of the dictionary become the labels.

'''
To select only some of the items in the dictionary, 
use the index argument and specify only the items you
want to include in the Series.
'''

print("\n")
data2 = pd.Series(calories, index = ["day 1", "day 2"])
print(data2)