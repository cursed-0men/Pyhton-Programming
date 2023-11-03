# TYPE CONVERSION Function
# 2 types : 1.implicit(done by python itself), 2.explicit
# converting one data type to other.
# 1. int()
# 2. float()
# 3. complex()
# 4. bool()
# 5. str()

i = 15
f = 16.59
b = True
c = 10 + 6j
s1 = 'Lucifer'
s2 = '125'
s3 = '0b1111'

# converting float to int
x = int(f)
print(x)

# converting boolean to int
y = int(b)
print(y)

# converting complex to int... not possible

# converting complex to float... not possible
# converting string to float ... not possible generally. only possible if string contains digits.

# converting string to int ... not possible generally. only possible if string contains digits.

# converting string to int
o = int(s2)
print(o)

# converting string(containing binary number) to int
t = int(s3, 2)
# 2 is the base, we are passing it as parameter to convert binary to decimal and then convert string to int .
print(t)

# complex number will work on all datatypes(except for string not containing digits)
# boolean will show true for all datatypes.(except strings containing nothing)
# string will work on every data-type.
# TABLE

# type casting   int   float   complex   bool   string
#    int()        Y      Y        N       Y       Y (if string contains digits)
#    float()      Y      Y        N       Y       Y (if string contains digits)
#    complex()    Y      Y        Y       Y       Y (if string contains digits)
#    bool()       Y      Y        Y       Y       Y (if string is not null)
#    str()        Y      Y        Y       Y       Y
