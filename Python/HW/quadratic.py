#############
# Quadratic Formula Calculator
# By Danny Schick
#############

import math # for the sqrt() function
print("The Quadratic Equation Solver")
print("Enter the values of a, b, and c as integers") # gather values
a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

radical = (b*b)-4*a*c # find value of discriminate

if radical == 0: # case 1
    root = -b/(2*a)
    print("The root of the equation is", format(root, '.1f')) # print result formatted to 1 decimal place
elif radical < 0: # case 2
    print("there are no real roots")
elif radical > 0: # case 3
    root1 = (-b-(math.sqrt(radical)))/(2*a) # find the two possible roots
    root2 = (-b+(math.sqrt(radical)))/(2*a)
    print("The two roots of the function are", format(root1, '.1f'), "and", format(root2, '.1f'))
else:
    print("There is some error. Please try again") # validate input
