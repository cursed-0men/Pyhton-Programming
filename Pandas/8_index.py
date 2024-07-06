# Named Indexes
# With the index argument, you can name your own indexes.

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]      
}

d = pd.DataFrame(data, index = ["day_1","day_2","day_3"])
print(d)

# Locate Named Indexes
print("\n\n")
print(d.loc["day_1"])