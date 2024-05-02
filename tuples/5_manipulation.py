# Manipulating Tuples

'''
Tuples are immutable, hence if you want to add, 
remove or change tuple items, then first you must 
convert the tuple to a list. Then perform operation
 on that list and convert it back to tuple.

'''

fruits = ('apple','banana','cherry')
print(fruits)

tup = list(fruits)

tup.append('pineapple')
fruits = tuple(tup)

print(fruits)