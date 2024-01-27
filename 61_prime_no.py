# checking if a number is prime or not.

n = int(input("n = "));


count = 0

for i in range(1,n+1):
      if(n%i==0):
            count += 1

if count==2:
      print(f"{n} is prime")
else:
      print(f"{n} is not prime")