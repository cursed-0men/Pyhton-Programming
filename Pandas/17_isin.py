'''
the isin() conditional function returns 
a True for each row the values are in the 
provided list. To filter the rows based on 
such a function, use the conditional function 
inside the selection brackets [].
'''
import pandas as pd
data = pd.read_csv("titanic.csv")

# I’m interested in the Titanic passengers from cabin class 2 and 3.
# making subset for it

cabinclass23 = data[data["Pclass"].isin([2,3])]
# OR
# cabinclass23 = data[(data["Pclass"] == 2) | (data["Pclass"] == 3)]
print(cabinclass23.head())

# printing shape of subset
print(cabinclass23.shape)