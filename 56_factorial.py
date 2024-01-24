# factorial of a number using for loop.

n = int(input("n = "))
factorial = 1

for i in range(n,1,-1):
      factorial = factorial * i

print(factorial)



# short trick(using math library)

# import math
# n = int(input("n = "))
# answer = math.factorial(n)
# print(answer)
