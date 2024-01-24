# Break statement.
# it is used to exit/stop the loop when the desired output is received.

# Eg.
while True:
    n = int(input("Enter a number = "))
    if n > 0:
        print("positive")
    elif n < 0:
        print("negative")
    else:
        break
# it will exit the loop when zero or any other datatype is entered as input format.
