# Expressions.
# Instructions that we write using operators are called Expressions.
# Each operation has its own precedence(priority order) and according to that, operations are performed.
# ARITHMETIC OPERATIONS PRECEDENCE.
# 1.  ()
# 2.  **
# 3.  * , / , %
# 4.  + , -
# In case of same precedence, operations are performed from left to right.
# NOTE = In case of same precedence of "power" operator, operations are performed from right to left.

a = 2 * 3 + 8 / 2
print(a)  # 1. 2*3  2. 8/2  3. 6+4

b = 3 * 4 * 5 / 4
print(b)   # 1. 3*4  2. 12*5  3. 60/4

c = 2 ** 3 ** 2
print(c)  # 1. 2^3  2. 3^2  => 3^2=9  => 2^9=512

d = (2 ** 3) ** 2
print(d)  # 1. 2^3=8    2. 8^2=64


