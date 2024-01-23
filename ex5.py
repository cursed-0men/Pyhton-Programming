# Write a fizzBuzz() function with a single integer parameter named upTo. For the numbers 1

# up to and including upTo, the function prints one of four things:

# Prints 'FizzBuzz' if the number is divisible by 3 and 5.

# Prints 'Fizz' if the number is only divisible by 3.

# Prints 'Buzz' if the number is only divisible by 5.

# Prints the number if the number is neither divisible by 3 nor 5

def FizzBuzz(upto):
      count = 1
      while count <= upto:
            if((count % 3 == 0) and (count % 5 == 0)):
                  print(count,"FizzBuzz")
            
            elif(count % 3 == 0):
                  print(count,"Fizz")

            elif(count % 5 == 0):
                  print(count,"Buzz")

            else:
                  print(count)
            
            count += 1
      

upto = int(input("Enter number = "))     
FizzBuzz(upto)

