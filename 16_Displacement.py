# Finding displacement
# (v^2 - u^2)*/(2a)
u = int(input("enter initial velocity = "))
v = int(input("enter final velocity = "))
a = int(input("enter acceleration = "))
s = (v**2 - u**2)/(2 * a)

print("displacement = ", s)
