# printing n terms of fibonacci series.

# fibonacci series : 0,1,1,2,3,5,8,13...
# 3rd term = 1st term + 2nd term

# input:
# c -> a + b
# n -> number of terms


n = int(input("enter number of terms to display = "))
a = 0
b = 1

for i in range(n):
      print(a,end=" ")
      c = a + b
      a = b
      b = c