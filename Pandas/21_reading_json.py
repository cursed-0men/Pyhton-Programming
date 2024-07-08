# Reading JSON file

'''
JSON is plain text, but has the format of an 
object, and is well known in the world of 
programming, including Pandas.
'''

import pandas as pd
temp = pd.read_json('data.json')

print(temp.head().to_string())