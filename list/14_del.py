# del

'''
del is not a method, rather it is a keyword which 
deletes item at specific from the list, or deletes 
the list entirely.

'''
veg = ["carrot", "potato", "cabbage", "tomato",]
# print(veg)

del veg[2]
print(veg)

del veg
print(veg) # NameError: name 'veg' is not defined 