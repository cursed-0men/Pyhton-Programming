# checking if the entered year is a leap year.

year = int(input("enter year = "))

if (year % 400 == 0) and (year % 100 == 0):
    print("Leap year")
if (year % 4 == 0) and (year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year.")
