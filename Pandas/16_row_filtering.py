# How do I filter specific rows from a DataFrame?

import pandas as pd
data = pd.read_csv("titanic.csv")

# I’m interested in the passengers older than 35 years.
# creating subet for it
above35 = data[data["Age"] > 35]

print(above35.head()) # filter out rows
'''
    PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
1             2         1       1  ...  71.2833   C85         C
6             7         0       1  ...  51.8625   E46         S
11           12         1       1  ...  26.5500  C103         S
13           14         0       3  ...  31.2750   NaN         S
15           16         1       2  ...  16.0000   NaN         S

[5 rows x 12 columns]
'''
print(type(above35))

# printing shape of subset
print(above35.shape)


print("\n\n\n")
print(data["Age"].head() > 35) # prints columns
'''
0    False
1     True
2    False
3    False
4    False
Name: Age, dtype: bool
'''