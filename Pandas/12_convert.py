# My colleague requested the Titanic data as a spreadsheet.

import pandas as pd
data = pd.read_csv("titanic.csv")
# print(data)

# converting to excel sheet
# variable_name.to_excel("csv_file_name.csv",sheet_name = "new_name", index = False)
data.to_excel("titanic.xlsx", sheet_name="passengers",index=False)

# By setting index=False the row index labels are not saved in the spreadsheet.
# The equivalent read function read_excel() will reload the data to a DataFrame:
data = pd.read_excel("titanic.xlsx",sheet_name="passengers")
print(data.head())

# the to_* methods are used to store data.