'''
The describe() method provides a quick overview
of the numerical data in a DataFrame.
'''
import pandas as pd

data = {
      'Name' : ['Ironman','Hulk','B.Widow','S.witch','Panther'],
      'Age' : [35,41,25,27,30],
      'Gender' : ["male","male","female","female","male"]
}

d = pd.DataFrame(data)
print(d)
print(d.describe())