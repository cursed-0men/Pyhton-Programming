# find factors of a number


n = int(input("enter number = "))

print(f"Factors of {n}->")
for i in range(1,n+1):
      if (n%i==0):
            print(i)
      
