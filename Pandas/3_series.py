# What is a Series?
# It is a one-dimensional array holding data of any type.

import pandas as pd
a = [5,4,2,3]

var = pd.Series(a)
print(var)


# 0    5
# 1    4
# 2    2
# 3    3
# dtype: int64

# here 0,1,2,3 are indices


# Return the first value of the Series:
# print(myvar[0]) for 