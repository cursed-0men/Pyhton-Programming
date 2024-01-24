# Pass Statement
# Literally means 'do nothing'.

# eg. print numbers from 1-10 except multiples of 3 i.e 3, 6, 9.
count = 0
while count < 10:
    n = int(input("Enter a number = "))
    if n % 3 == 0:
        pass  # we wish to do nothing when if block executes.
    else:
        print(n)
    count += 1
# In this case, iterations with number divisible by 3, will be considered but won't be printed.
        