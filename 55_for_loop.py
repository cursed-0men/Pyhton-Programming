# for loop : also called for each loop.

# SYNTAX :       
#                 for i in range(0,10):
#                       print(i)


# RANGE is a function.
# EG. range(10) means : 0,1,2,...9
# EG. range(5,10) means : 5,6,7,8,9

# NOTE
# range(1,10,2) means :1,3,5,7,9
#  here 2 is step(or i=i+2)

# range(10,0,-1) : 10,9,8,7...1



name = "dhyey"

for x in name:  # here x is variable
      print(x)

print("\n-----------------")

for i in range(1,10):
      print(i,end=" ") # to print output in single line.

print("\n-----------------")

for j in range(1,10,2):
      print(j,end=" ")

print("\n-----------------")

for k in range(10,0,-1):
      print(k,end=" ")

