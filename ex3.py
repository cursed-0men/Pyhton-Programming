# odd/even

number = int(input("Enter a number = "))

def odd(number):
      if number%2!=0:
            print(f"{number} is ODD")

def even(number):
      if number%2==0:
            print(f"{number} is EVEN")

odd(number)
even(number)
