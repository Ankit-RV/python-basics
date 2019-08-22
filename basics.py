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




# ASSIGNMENT 2

# 1.write a python script to check whether a given number is even or odd.
a = int(input("enter a number: "))
if a%2==0:
    print("{} is even".format(a))
else:
    print("{} is odd".format(a))

# 2.write a python script to check whether a given number is divisible by 5 or not.
b = float(input("enter a number: "))
if b%5==0:
    print("{} is dividible by five".format(b))
else:
    print("{} is not divisible by five".format(b))
    
# 3. write a python script to check whether a given number is positive negative or zero.
a = int(input("enter a number: "))
if a>0:
    print("%d is positive"%a)
elif a==0:
        print("zero")
else:
    print("%d is negative"%a)

# 4. write a python script to find greatest among three numbers.
num1 = float(input("enter first value: "))
num2 = float(input("enter second value: "))
num3 = float(input("enter third value: "))
if (num1>num2)and(num1>num3):
    print("greatest number is ",num1)
elif(num2>num1)and(num2>num3):
    print("greatest number is ",num2)
elif(num1==num2)and(num2==num3)and(num3==num1):
    print("numbers are same or equal")
else:
    print("greatest number is ",num3)
    

# 5. write a python script to check if a year is leap year or not.
y=int(input("enter year: "))
if(y%4==0 and (y%100!=0 or y%400==0)):
   print("leap year")
else:
   print("not leap year")
    
"""single line if else approcj"""
x=int(input("enter an year"))
result = "leap year" if x%400==0 else "leap year" if x%4==0 and x%100!=0 else "non leap year"
print(result)

exit()


# 6. write a python script to take month value in numaric formate and display number of days in it.
print("list of months: january, february, march, april, may, june, july, august, september, october, november, december")
month_name=input("input the name of month: ")
if month_name=="february":
    print("no of days: 28/29")
elif month_name in ("april","september","june","november"):
    print("no of days: 30")
elif month_name in ("january","march","may","july","august","october","november","december"):
    print("no of days: 31")
else:
    print("wrong month name")
    
    

# 7. write a python script to check nature of roots of a given quadratic equation.
a=float(input("enter value of a: "))
b=float(input("enter value of b: " ))
c=float(input("enter value of c: "))
r=(b**2)-(4*a*c)
if r>0:
    print("roots are real")
elif r==0:
    print("roots are zero")
else:
    print("roots are imaginary")
        

# 8. write a python script to print a set of three words in dictonary order. words are given by user.
print("enter three words")
a,b,c=input(),input(),input()
if a<b<c:
    print(a,b,c)
elif a<c<b:
    print(a,c,b)
elif b<a<c:
    print(b,a,c)
elif b<c<a:
    print(b,c,a)
elif c<a<b:
    print(c,a,b)
else:
    print(c,b,a)
#2nd method
print("enter three words")
a,b,c=input(),input(),input()
x=min(a,b,c)
print(x)
if x==a:
    print(min(b,c),max(b,c))
elif x==b:
          print(min(a,c),max(a,c))
else:
    print(min(a,b),max(a,b))
#3rd method
[x for x in sorted(input("enter coma separated three word ").split(',')) if print(x,end=',')]




#9. write a python script to accept one complex number from user and display the greatest number between real part and imaginay part.
x=int(input("enter a value: "))
y=int(input("enter another value: "))
z=complex(x,y)
print("complex number is:",end="")
print(z)
print (" and the real part of complex number is:",end="")
print(z.real)
print ("and the imaginary part of complex number is:",end="")
print(z.imag)


""" 10. write a python script to accept marks of five subjects from user (assuming maximum marks is 100).
Display student's result as pass or fail. if the student is pass then also display his percentage and division
"""
a=float(input("a "))
b=float(input("b "))
c=float(input("c "))
d=float(input("d "))
e=float(input("e "))
if (a<35 or b<35 or c<35 or d<35 or e<35):
     print("fail")

x=(a+b+c+d+e)/5
if x>35:
      
    print("pass")
    
else:
    print("faill")

if x>=65:
    print("first division")
elif x>=45:
    print("second division")
elif x<45:
    print("third division")
print("percentage of student is ",end="")
print(x)











