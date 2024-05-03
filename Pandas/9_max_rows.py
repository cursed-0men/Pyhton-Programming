# max_rows
# The number of rows returned is defined in Pandas option settings.

# You can check your system's maximum rows with the pd.options.display.max_rows statement

import pandas as pd
var = pd.read_csv('data.csv')
print(var)

print("max rows =",pd.options.display.max_rows)