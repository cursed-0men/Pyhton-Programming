# Finding Largest number from user given numbers.

num_of_numbers = int(input("Enter number of numbers = "))
i = 0
Max = 0
while i < num_of_numbers:
    n = int(input("enter number = "))
    if n > Max:
        Max = n
    i += 1
print("maximum =", Max)
# NOTE :
# this code won't work for all -ve numbers input, as Max is already assigned 0 and 'if' condition won't be executed.
# So, Max won't be updated and will remain zero. Hence, it will print '0' as maximum.
