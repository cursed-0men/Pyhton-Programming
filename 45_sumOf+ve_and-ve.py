# Sum of +ve and -ve numbers.
p_sum = 0
n_sum = 0

num_of_numbers = int(input("Enter number of numbers = "))
i = 0

while i < num_of_numbers:
    n = int(input("enter number = "))
    if n >= 0:
        p_sum += n
    else:
        n_sum += n
    i += 1

print(p_sum, n_sum)
