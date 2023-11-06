# Bitwise Operators.

# 1. & (AND)
# 2. | (OR)
# 3. ^ (XOR)
# 4. ~ (Complement)
# 5. >> (Right shift)
# 6. << (Left shift)

# Function to see binary values of a number.
a = 50
print(format(a, 'b'))
# Also
print(bin(a))

# left shift (<<)
# left shift by 1, gives the double of number as a result.
# left shift by 2, gives the quadruple of number as a result.
print(a << 1)  # will print 100.

# right shift (>>)
# right shift by 1, gives the half of number as a result.
# right shift by 2, gives the one-fourth of number as a result.
print(a >> 1)  # will print 25.
