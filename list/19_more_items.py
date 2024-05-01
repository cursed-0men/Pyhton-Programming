# What if we have more items to be replaced than the index range provided?

'''
In this case, the original items within the 
range are replaced by the new items and the 
remaining items move to the right of the list 
accordingly.

'''

colors = ['red','blue','green','orange']
print(colors)

colors[1:3] = ['violet','indigo','cyan','black','crimson']
print(colors)