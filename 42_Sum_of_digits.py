# sum of digits of a number.
addition = 0
n = int(input("Enter number = "))

while n > 0:
    r = n % 10
    n = n // 10
    print(r)
    addition += r

print("Sum =", addition)
    