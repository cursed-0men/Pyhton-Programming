# Counting number of digits in a number.

n = int(input("Enter number = "))
digit_counter = 0

while n > 0:
    r = n % 10
    n = n // 10
    print(r)
    digit_counter += 1

print("number of digits =", digit_counter)
