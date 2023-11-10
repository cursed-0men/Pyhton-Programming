# Reversing a number(using while loop)

n = int(input("Enter number = "))

# while loop for reversing the digits.
while n > 0:
    r = n % 10
    n = n // 10
    print(r)
