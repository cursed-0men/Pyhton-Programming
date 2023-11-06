# Relational Operators

#               <    <=    >    >=    ==    !=
# int ------->  Y    Y     Y     Y    Y      Y
# float ----->  Y    Y     Y     Y    Y      Y
# bool ------>  Y    Y     Y     Y    Y      Y
# complex --->  N    N     N     N    Y      Y
# str ------->  Y    Y     Y     Y    Y      Y

# For complex comparison both real and imaginary parts are used, hence we can only use == and != operators.

# String Comparison
# we compare each alphabet of string till it is different, and then we determine that which comes first.
# alphabet which comes first is smaller.
# Also uppercase letters are smaller so it come first.
s1 = 'brazil'
s2 = 'bracket'

if s1 < s2:
    print("true")
else:
    print("false")

s3 = 'Brazil'
if s1 < s3:
    print("true")
else:
    print("false")
