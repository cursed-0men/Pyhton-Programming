# You will write four functions for this exercise. The functions area() and perimeter() have
# length and width parameters and the functions volume() and surfaceArea() have length,
# width, and height parameters. These functions return the area, perimeter, volume, and surface
# area, respectively.

l = int(input("Enter length = "))
w = int(input("Enter width = "))
h = int(input("Enter height = "))

print("\n")
# area function
def area(l,w):
      print("area =",l*w)

area(l,w)

# perimeter function
def perimeter(l,w):
      print("perimeter =",2*(l+w))

perimeter(l,w)

#volume function
def volume(l,w,h):
      print("volume =",l*w*h)

volume(l,w,h)

# surface area function
def surface_area(l,w,h):
      print("surface area =",2*((l*w)+(w*h)+(l*h)))

surface_area(l,w,h)
print("\n")