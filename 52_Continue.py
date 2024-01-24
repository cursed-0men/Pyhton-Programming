# Continue Statement
# it will skip the statements after 'continue' and will go at starting point of loop.

# eg. print numbers from 1-10 except multiples of 3 i.e 3, 6, 9.

count = 0
while count < 10:
    n = int(input("enter a number = "))
    if n % 3 == 0:
        continue
    print(n)
    count += 1
# In this case, iterations with number divisible by 3, will not be considered.
