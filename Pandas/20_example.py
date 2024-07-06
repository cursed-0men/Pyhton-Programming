# I’m interested in rows 10 till 25 and columns 3 to 5.
import pandas as pd
data = pd.read_csv("titanic.csv")

# we'll usse slicing in subset
new_data = data.iloc[9:25,2:5]
print(new_data)
print("shape =",new_data.shape)

'''
Select specific rows and/or columns using loc 
when using the row and column names.

Select specific rows and/or columns using iloc 
when using the positions in the table.

'''