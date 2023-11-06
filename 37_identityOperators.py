# identity operators
# 1. is (referring to same memory location)
# 2. is not
a = 10
b = 10
print(a is b)  # returns true
# function to determine memory address of a variable.
print(id(a))
print(id(b))
# they both have same memory address hence "a is b" returns true.
print("-----------------------------------")
c = 10
d = 20
print(c is d)  # returns false
print(c is not d)  # returns true
print(id(c))
print(id(d))
print("-----------------------------------")
e = int(input("enter e = "))
f = int(input("enter f = "))
print(id(e))
print(id(f))

# typecasting with same datatypes of same number will make the memory address of both number same.


