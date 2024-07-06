# How do I select specific rows and columns from a DataFrame?

'''
a subset of both rows and columns is made in one go and 
just using selection brackets [] is not sufficient anymore. 
The loc/iloc operators are required in front of the 
selection brackets []. When using loc/iloc, the part 
before the comma is the rows you want, and the part after 
the comma is the columns you want to select.
'''

# loc/iloc[rows we want, columns we want]


'''
When using the column names, row labels or a condition 
expression, use the loc operator in front of the selection 
brackets []. For both the part before and after the comma, 
you can use a single label, a list of labels, a slice of 
labels, a conditional expression or a colon. Using a colon 
specifies you want to select all rows or columns.
'''

import pandas as pd
data = pd.read_csv("titanic.csv")
# I’m interested in the names of the passengers older than 35 years.
# creating subset for it
name_over_35 = data.loc[data["Age"]>35, "Name"]
print(name_over_35.head())