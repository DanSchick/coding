################
# Danny Schik
# Lab #1
# MPG calculator
################

miles = int(input("How many miles?: "))
gallons = float(input("How many gallons of gas?: "))
print("You drove", miles, "miles and used", format(gallons, '.1f'), "gallons")
mpg = miles / gallons
print("Your miles per gallon was", format(mpg, '.1f'))
