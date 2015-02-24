# CS 21 HW
# Danny Schick
# Excersize 9 | Celsuis to Fahrenheit

####### DEFINING INITIAL VARIABLES #####
convertFactor = 9/5 # conversion constant from C to F

####### GETTING INPUT ######
degC = float(input("Enter the degrees in C you wish to confert to F: "))

####### CONVERTING TO F ######
degF = (convertFactor * degC) + 32

####### PRINTING RESULT ######
print( "\n\n", degC, "deg C is",end=' ')
print("{:.2f}".format(degF),end=' ') # format deg F to two decimal places
print("deg F")
