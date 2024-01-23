# In English, ordinal numerals have suffixes such as the ―th‖ in ―30th‖ or ―nd‖ in ―2nd‖. Write an

# ordinalSuffix() function with an integer parameter named number and returns a string of the

# number with its ordinal suffix. For example, ordinalSuffix(42) should return the string

# '42nd'.



n = int(input("enter number = "))
remainder = n%10

# function to find last digit of an entered number
def last_digit(n):
      print("last digit =",remainder)


# assigning suffix
def ordinalSuffix(remainder):
      if remainder == 1:
            suffix = "st"
      elif remainder == 2:
            suffix = "nd"
      elif remainder == 3:
            suffix = "rd"
      else:
            suffix = "th"

      print(n,suffix)


last_digit(n)
ordinalSuffix(remainder)



      



      