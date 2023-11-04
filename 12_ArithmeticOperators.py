# Arithmetic Operators
# 1. + Add
# 2. - Subtract
# 3. * Multiply
# 4. ** Power
# 5. / Divide(float)
# 6. // Divide(floor)
# 7. % Modulus


# 1.Add
a = int(input("enter a = "))  # we have to mention int for interpreter to fixate datatype for user entered data.
b = int(input("enter b = "))
add = a + b  # will add a and b
print("sum =", add)

diff = a - b  # will subtract b form a
print("difference =", diff)

pro = a * b  # will multiply a and b
print("Product =", pro)

power = a ** b  # a raise to power b (a^b)
print("Power =", power)

flt = a / b  # will divide a with b and, prints quotient as it is(also if it is fraction).
print("float div' =", flt)

flr = a // b  # will divide a with b and, prints quotient in integral form.
print("floor div =", flr)

mod = a % b  # will print remainder of division a/b.
print("remainder = ", mod)
