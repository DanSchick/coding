# CS 21 lab 2
# 9/3/14
# Danny Schick

# chapter 2 ex 6 | Sate and county sales tax calculation

# DEFINING CONSTANTS AND VARIABLES
STATE_TAX_RATE = .05
COUNTY_TAX_RATE = .025
purchase_price = 0
state_tax = 0
county_tax = 0
total_tax = 0
total_sale = 0


# GET INPUT
purchase_price = float(input("Enter the amount of purchase: "))


# CALCULATE
state_tax = STATE_TAX_RATE * purchase_price
county_tax = COUNTY_TAX_RATE * purchase_price

total_tax = state_tax + county_tax


total_sale = total_tax + purchase_price

# PRINT RESULTS
print('\nYour Receipt: \n*----------------------*')
print("Purchase amount: $", format(purchase_price, '.2f'), sep='')
print("State tax: $", format(state_tax, '.2f'), sep='')
print("County tax: $", format(county_tax, '.2f'), sep='')
print("Total Tax: $", format(total_tax, '.2f'), sep='')
print("Total Sale: $", format(total_sale, '.2f'), sep='')
