#Program to find solutions of a quadratic equations
import math
print("Enter a,b,c :")
a = int(input())
b = int(input())
c = int(input())
d = b*b-4*a*c
print(d)
sqrt = d**0.5
print("Discriminant of a equatioin :",sqrt)

r1 =  ((-b+sqrt)/(2*a))
r2 =  ((-b-sqrt)/(2*a))
print("first root of equation :",r1)
print("second root of equation :",r2)
