# checking if entered number is palindrome.
# Palindrome condition:
# Palindrome is the number which remains the same even if it is reversed.
# eg: 121, 1331 etc.
n = int(input("Enter a number = "))
rev = 0  # declaring reverse of number as zero.
temp = n  # assigning n to the variable temp for comparison purpose.
while n > 0:
    r = n % 10
    n = n // 10
    rev = (rev * 10) + r
    print(r)  # code block of reversing the number.


print("**********")
print(rev)
if temp == rev:
    print("is a Palindrome number")
else:
    print("Not a Palindrome number")
