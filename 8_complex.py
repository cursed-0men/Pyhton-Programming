# complex datatype
# real + imaginary part
# python provides complex datatypes in form of : a+bj
# here j is iota, a is real part and b is imaginary part.

a = 3.5 + 6.6j
print(type(a))
print(a)
print(a.real)  # here variable_name.real is syntax for displaying real part of complex number.
print(a.imag)  # here variable_name.imag is syntax for displaying imaginary part of complex number.
# if we write this : complex(a,b) then, it means =
# a+bj
# Eg.
print('\n')
b = complex(13, 8)  # also a syntax for declaring a complex number.
     # real(a)  imaginary(b)
print(b)
