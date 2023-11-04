# Roots of Quadratic equation
import math
a = int(input("enter coefficient of x^2 = "))
b = int(input("enter coefficient of x = "))
c = int(input("enter constant term = "))

root1 = (-b + math.sqrt(b**2 - 4*a*c))/(2 * a)
root2 = (-b - math.sqrt(b**2 - 4*a*c))/(2 * a)

print("1st =", root1)
print("2nd =", root2)
# b^2-4ac must be > 0.
# it will show error in case of imaginary roots.

