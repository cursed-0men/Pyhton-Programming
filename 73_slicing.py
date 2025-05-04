# string slicing
# s1[start : end : step]
# the end is similar to that of for loop

# if we wish to print whole string then we can skip writing start and end


s = "hello"
print(s[0:5:1])

print("\n")
print(s[::1])
# we can also avoid writing 1 as step up

# printing reverse of string
print("\n")
print(s[-1:-len(s)-1:-1])
#OR
print(print(s[-1::-1]))





# NOTE
#  0   1    2   3   4 -->(printing string normally)
#  H   e    l   l   o
# -5  -4   -3  -2  -1 <--(printing string in reverse)    