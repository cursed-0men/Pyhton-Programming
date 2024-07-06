# Labels
# If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

# This label can be used to access a specified value.

import pandas as pd

data_series = [7,8,9]
ds = pd.Series(data_series, index=["i1","i2","i3"])

print(ds)

# When you have created labels, you can access an item by referring to the label.

print(ds['i2'])