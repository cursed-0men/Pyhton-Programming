# What if the range of the index is more than the list of items provided?

'''
In this case, all the items within the index range of the 
original list are replaced by the items that are provided.

'''

colors = ['red','yellow','orange','green','blue']
print(colors)

colors[1:4] = ['cyan','violet']
print(colors)  # ['red', 'cyan', 'violet', 'blue']

