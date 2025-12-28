#right triangle
b=int(input("Enter the breadth  of the triangle:"))
h=int(input("Enter the height of the triangle:"))
area=0.5*b*h
print("The area of the triangle:",area)

#isoceless triangle
import math 

a=int(input("Enter the length  of the triangle:"))
b=int(input("Enter the length  of the triangle:"))
c=int(input("Enter the length  of the triangle:"))

s=(a+b+c)/2

area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)
