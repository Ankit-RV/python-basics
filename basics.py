welcome to python basics
#Assignment 1

#1. write a python script to add two numbers(integer) taken from user through keyboard.
x = int(input("enter first value: "))
y = int(input("enter second value: "))
z = x+y
print("sum of %d and %d is %d"%(x,y,z))


#2. write a python script to calculate area of circle, radius is taken from user.
import math
r = float(input("radius of circle: "))
A = math.pi*math.pow(r,2)
print("area of circle is",A)


#3. write a script to calculate volume of cubiod, dimensions(float values)taken from user.
l = float(input("length of cubiod: "))
b = float(input("breath of cubiod: "))
h = float(input("height of cubiod: "))
v = l*b*h
print("volume of cubiod is:",v)


#4. python script for calculating simple interest, data required should be taken from user.
p = int(input("principal: "))
r = float(input("rate of interest: "))
t = float(input("period: "))
si = (p*r*t)/100
print("simple interest is:",si)


#5. python code for calculating square of a number.
import math
sq = float(input('enter number: '))
print("square of number is",int(math.pow(sq,2)))


#6. write a python script to calculate area of triangle. length of side are given by user
import math
a = float(input("first side of triangle: "))
b = float(input("second side of triangle: "))
c = float(input("third side of triangle: "))
s = (a+b+c)/2
print('area of triangle is:',float(math.sqrt(s*(s-a)*(s-b)*(s-c))))
exit()






