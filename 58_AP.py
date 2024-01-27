# print n terms of AP(arithmetic progression)

# inputs : 
# n ==> first n terms of AP.
# a ==> first term of AP.
# d ==> common difference.

a = int(input("Enter first term of AP = "))
d = int(input("Enter common difference = "))
n = int(input("no. of terms to display = "))

# loop for displaying n terms of AP.

for term in range(a,a+(n)*d,d):
      print(term,end=" ")


# NOTE : here at upper limit of for loop, we have to write general term of AP.
# i.e : a+(n-1)*d;
# but for loop displays till (upper limit - 1).
# so we have to add 1 in n-1 = n.
# so new upper limit will be : a+(n*d)