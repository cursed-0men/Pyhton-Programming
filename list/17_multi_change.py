# change more than a single item at once

'''
Just specify the index range over which 
you want to change the items.

'''

lang = ['c++','php','c','java']
print(lang) # ['c++', 'php', 'c', 'java']

lang[1:3] = ['python','javascript']
print(lang) # ['c++', 'python', 'javascript', 'java']

# NOTE : index "3" is non-inclusive
