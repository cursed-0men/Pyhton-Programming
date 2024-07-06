# Selecting multiple columns

import pandas as pd
data = pd.read_csv('titanic.csv')

# I’m interested in the age and sex of the Titanic passengers.
# creating subset for it
data_age_sex = data[["Age","Sex"]]
# NOTE : To select multiple columns, use a list of column names within the selection brackets [].

print(data_age_sex.head())

# printing type of subset
print(type(data[["Age","Sex"]]))

# printing shape of subset
print(data[["Age","Sex"]].shape)