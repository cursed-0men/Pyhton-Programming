# Finding largest among all i.e +ve and -ve both.
# i.e. Linear Search
num_of_numbers = int(input("Enter number of numbers = "))
i = 0
Max = float('-inf')  # initializing Max as -ve infinite.
while i < num_of_numbers:
    n = int(input("enter number = "))
    if n > Max:
        Max = n
    i += 1
print("maximum =", Max)
