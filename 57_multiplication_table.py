# multiplication table using for loop

n = int(input("n = "))

for i in range(1,11):
      print(f"{n} * {i} = {n*i}")

# we use f to dynamically replace value in each iteration .
# we can also compare curly brackets {} with "%d","%f","%c"... of C language.
