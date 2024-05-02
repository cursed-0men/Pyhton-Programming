# Accessing single values

'''
Values in a dictionary can be accessed using keys. 
We can access dictionary values by mentioning keys 
either in square brackets or by using get method.
'''

info = {'name':'Dhyey', 'age':19, 'eligible':True}
print(info['name'])

# we can also use
print(info.get('name'))