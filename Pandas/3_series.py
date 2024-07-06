# Pandas Series
# A Pandas Series is like a column in a table.
# Each column in a DataFrame is a Series

import pandas as pd

age = [5,6,7]
d = pd.Series(age)
print(d)
print(max(d)) # To print maximum value in age 
