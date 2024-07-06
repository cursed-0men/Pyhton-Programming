'''
The notna() conditional function returns a 
True for each row the values are not a Null value.
'''

import pandas as pd
data = pd.read_csv('titanic.csv')

# I want to work with passenger data for which the age is known.
# creating subset for it

known_age = data[data["Age"].notna()]

print(known_age.head())

# printing shape of subset
print(known_age.shape)

# printing type of subset
print(type(known_age))