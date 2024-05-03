# Creating Labels
# With the index argument, you can name your own labels.

import pandas as pd

a = [4,9,5]

var = pd.Series(a,index = ["x","y","z"])

print(var)
print(var["y"])

# x    4
# y    9
# z    5
# dtype: int64