# Finding absolute difference between 2 numbers.
a = int(input("enter 1st number = "))
b = int(input("enter 2nd number = "))

if a > b:
    print("Difference = ", a-b)
elif a < b:
    print("Difference = ", b-a)
else:
    print("Difference = 0")
