# Read CSV Files
# CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

'''
pandas provides the read_csv() function to read data 
stored as a csv file into a pandas DataFrame. pandas 
supports many different file formats or data sources 
out of the box (csv, excel, sql, json, parquet, …), 
each of them with the prefix read_*.
'''

import pandas as pd
# we have sample csv file named titanic
data = pd.read_csv("titanic.csv")

print(data)
# When displaying a DataFrame, the first and last 5 rows will be shown by default

'''
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q

'''

# I want to see the first 8 rows of a pandas DataFrame.
print(data.head(8))
# To see the first N rows of a DataFrame, use the head() method with the required number of rows (in this case 8) as argument.
'''
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S
5            6         0       3  ...   8.4583   NaN         Q
6            7         0       1  ...  51.8625   E46         S
7            8         0       3  ...  21.0750   NaN         S

[8 rows x 12 columns]
'''





# pandas also provides a tail() method. For example, titanic.tail(10) will return the last 10 rows of the DataFrame.
print("\n\n")
print(data.tail(10))
'''
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
881          882         0       3  ...   7.8958   NaN         S
882          883         0       3  ...  10.5167   NaN         S
883          884         0       2  ...  10.5000   NaN         S
884          885         0       3  ...   7.0500   NaN         S
885          886         0       3  ...  29.1250   NaN         Q
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q

[10 rows x 12 columns]
'''      

print("\n\n\n")
print("+++++++++++++++++++++++++++++++++++++++++++++")
print(data.to_string())
# Tip: use to_string() to print the entire DataFrame.