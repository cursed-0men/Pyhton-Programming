# But what if we have more number of items then the variables?
'''
You can add an * to one of the variables and depending 
upon the position of variable and number of items, 
python matches variables to values and assigns it to 
the variables.

'''

wildlife = ('lion','tiger','cobra','eagle','shark')
(*animals, birds, fish) = wildlife

print(animals)
print(birds)
print(fish)