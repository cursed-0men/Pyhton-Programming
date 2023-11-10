# Displaying, multiplication table of the number entered by user.

count = 1
n = int(input("Enter number = "))

while count <= 10:
    print(n, "x ", count, "=", n * count)
    count += 1
