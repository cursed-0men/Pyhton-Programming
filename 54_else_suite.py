# else suite
# else with while loop

count = 0

while count <= 10:
      print(count)
      count += 1
      if count > 5:  # it will print numbers till 5,and it will stop.
            break   # so while loop stops without completing successfully, it is breaking in b/w...else block won't execute.                                               
else:                   # because if condition never became false.
      print("Printed all 10 numbers")

print("end of code...")
