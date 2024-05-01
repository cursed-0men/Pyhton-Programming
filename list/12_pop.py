# Remove List Items

# To remove items from the list: pop(), remove(), del(), clear()


# pop()

'''
This method removes the last item of the list 
if no index is provided

'''
colors = ["red","blue","white","yellow","green","violet"]
print(colors)

colors.pop()  # Removes the last item of the list
print(colors)

colors.pop(2)
print(colors)