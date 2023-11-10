# Sum of given numbers as input.

num_of_numbers = int(input("enter number of numbers = "))  # taking number of numbers as zero
total = 0  # sum is zero
i = 0  # 'i' is count i.e zero

while i < num_of_numbers:
    n = int(input("enter number = "))  # taking numbers form user and storing it in 'n'.
    total += n  # adding numbers to the total.
    i += 1  # also count needs to be increased, or else it'll be an infinite loop.

print("sum =", total)  # printing sum of numbers.

