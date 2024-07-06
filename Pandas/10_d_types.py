# When asking for the dtypes, no brackets are used!
# dtypes is an attribute of a DataFrame and Series
'''
A check on how pandas interpreted each 
of the column data types can be done by 
requesting the pandas dtypes 'attribute'
'''

import pandas as pd
data = pd.read_csv("titanic.csv")

print(data)
print("\n\n")
print("datatypes...\n")
print(data.dtypes)

'''
PassengerId      int64
Survived         int64
Pclass           int64
Name            object
Sex             object
Age            float64
SibSp            int64
Parch            int64
Ticket          object
Fare           float64
Cabin           object
Embarked        object
dtype: object
'''