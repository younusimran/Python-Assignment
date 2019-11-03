#!/usr/bin/env python

# marksheet programm

per = int(input("Enter percentage obtained: "))
if per >= 80 and per <=100:
    print("A+ Grade")
elif per >=70 and per < 80:
    print("A Grade")
elif per >=60 and per < 70:
    print("B Grade")
elif per >=50 and per < 60:
    print("C Grade")
elif per >=40 and per < 50:
    print("D Grade")
elif per >=33 and per < 40:
    print("E Grade")
elif per < 33:
    print("Failed")
else:
    print("You have entered inappropriate percentage")