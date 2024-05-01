fruits = ['apple','avocado','cherry','orange','cherry']
print(fruits)
print(len(fruits))



# accepts items which have greater than or equal to 6 letters
more_than_six = [item for item in fruits if (len(item) >= 6)]

print(more_than_six)