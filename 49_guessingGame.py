# guessing number form 1-10.
# i.e. Binary Search.
# NOTE :READ COMMENTS🙏.
import random
n = random.randint(1, 10)
# this will generate random number selected from 1-10.
low = 1
high = 10
while low <= high:
    guess = int(input(f"Guess a number b/w {low} and {high} = "))
    # The f before the string indicates an f-string.
    #  In this case, it's used to dynamically insert the values of the variables low and high into the string.
    if guess < n:
        print("your guess is smaller, enter larger number")  # so we have to enter larger number
        low = guess + 1
    elif guess > n:
        print("your guess is larger, enter smaller number")  # so we have to enter smaller number
        high = guess - 1
    else:
        print("Guess is correct.")
        break
