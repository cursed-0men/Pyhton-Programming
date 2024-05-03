# Pandas is a Python library used for working with data sets.

# It has functions for analyzing, cleaning, exploring, and manipulating data.

# Allows us to analyze big data and make conclusions.

import pandas as pd
dataset = {
      'cars':['BMW','Ford','Corvette'],
      'passings':[3,7,2]
}

var = pd.DataFrame(dataset)

print(var)