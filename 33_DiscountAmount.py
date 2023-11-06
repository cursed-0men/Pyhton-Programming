# calculating discounted amount.
# DATA =>
# amount<=1000
# 1000 < amount <= 5000
# 5000 < amount <= 10000
# 10000 < amount

amount = int(input("enter amount = "))

if amount <= 1000:
    print("10% discount!!!")
    print("price after discount = ", amount-(amount * 0.1))
elif (amount > 1000) and (amount <= 5000):
    print("20% discount!!!")
    print("price after discount = ", amount - (amount * 0.2))
elif (amount > 5000) and (amount <= 10000):
    print("30% discount!!!")
    print("price after discount = ", amount - (amount * 0.3))
elif amount > 10000:
    print("50% discount!!!")
    print("price after discount = ", amount - (amount * 0.5))


