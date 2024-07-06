# How do I select a subset of a DataFrame
# How do I select specific columns from a DataFrame?

import pandas as pd
data = pd.read_csv("titanic.csv")

age = data["Age"] # making a subset out of csv file
print(age.head())

'''
Each column in a DataFrame is a Series. 
As a single column is selected, the returned 
object is a pandas Series. We can verify this 
by checking the type of the output:
'''
print("\n\n")
# printing type of subset 
print(type(data["Age"]))

# printing shape of subset -> dimensions of displayed data
print(data["Age"].shape)

# NOTE : DataFrame.shape is an attribute
# do not use parentheses for attributes) of a pandas Series and DataFrame containing the number of rows and columns