'''
A DataFrame is a 2-dimensional data structure 
that can store data of different types 
(including characters, integers, floating 
point values, categorical data and more) in columns.
'''

import pandas as pd
data = {
      "day" : [1,2,3],
      "calories" : [500,600,550]
} 

# Load data into a DataFrame object:
d = pd.DataFrame(data)
print(d)
print("\n")


'''
When selecting a single column of a pandas 
DataFrame, the result is a pandas Series. 
To select the column, use the column label 
in between square brackets [].
'''

print("only calories...........")
print(d["calories"])

# printing max and min of calories
print("displaying max and min")
print(d["calories"].max()," ",d["calories"].min())

# Pandas use the loc attribute to return one or more specified row(s)
print("\n\n")
print(d.loc[1])
print("\n\n")
print(d.loc[[1,2]]) # use a list of indexes:
# Return row 1 and 2:

print(d.loc[[1,2,3]])