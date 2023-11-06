# Nested Else - if
a = int(input("enter a = "))
b = int(input("enter b = "))
c = int(input("enter c = "))

if (a > b) and (a > c):
    print("max =", a)
elif c > a:
    print("max =", c)
else:
    print("max =", b)

