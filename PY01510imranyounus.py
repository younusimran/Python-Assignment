
#! usr/bin/env python
import sys
from datetime import datetime
from math import pi

# Python Assignment 1
# Question 1
print("Twinkle, twinkle, little star,\n\t\
How I wonder what your!\n\t\t\
Up above the world so high,\n\t\t\
Like a diamond in the sky,\n\
Twinkle, twinkle, little star,\n\t\
How I wonder what you are")

# Question 2
print(sys.version)

#Question 3
today = datetime.now()
print(today.strftime("Date = %B %d, %Y\nTime =  %H:%M:%S"))

#Question 4
radius = float(input("enter a radius to compute area of the circle: "))
area = pi*pow(radius,2)
print("Area of a circle for a radius of ",radius," is: ",area)

#Question 5
Fname = input("enter your first name: ")
Lname = input("enter your last name: ")
print(Lname,"",Fname)

#Question 6
num1 = float(input("Enter a first number: "))
num2 = float(input("Enter a second number: "))
print("Addition of ",num1," & ",num2," is ",num1+num2)