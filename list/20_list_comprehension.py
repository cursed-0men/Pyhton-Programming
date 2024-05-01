# List Comprehension

'''
List comprehensions are used for creating new lists from
lists, tuples, dictionaries, sets, and even in arrays and strings.

'''

# List = [expression(item) for item in iterable if condition]

# expression: it is the item which is being iterated.

# iterable: it can be list, tuples, dictionaries, sets, and even in arrays and strings.

# condition: condition checks if the item should be added to the new list or not. 



# Accepts items with the small letter “o” in the new list 
fruits = ['apple','avocado','orange','cherry','banana']
print(fruits)

name_with_o = [item for item in fruits if 'o' in item]
print(name_with_o)