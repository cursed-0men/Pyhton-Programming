# Converting decimal to binary

n = int(input("Enter a number = "))
print("Binary = ", bin(n))  # verification for displayed answer.
while n > 0:
    r = n % 2
    n = n // 2
    print(r)
# Sequence of remainders shall be swapped from top to bottom.
