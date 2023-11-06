# Conditional statements
# 1. if
# 2. else
# 3. elif

# For writing conditions we use relational and logical operators.

# Relational             Conditionals
# -----------------------------------
#     <                       AND
#     <=                      OR
#     >=                      NOT
#     >
#     ==
#     !=


# Checking if entered number is positive, negative, or Zero.

a = int(input("enter a number = "))
if a < 0:
    print(a, "is negative")
elif a == 0:
    print(" number is equal to 0")
else:
    print(a, "is positive")
