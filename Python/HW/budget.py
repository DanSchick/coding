###########
# Danny Schick
# CS21A
# Budget Calculator
############

# Determine monthly budget
budget = float(input("How much have you budgeted for this month?: "))

# set loop variables
loop = True
spent = 0
count = 0 # variable for number of expenses

# execute loop
while loop is True:
    # prompt for expense
    expense = float(input("Enter an Expense (0 to exit): "))
    if expense == 0: # exit condition
        loop = False
    elif expense < 0: # validate input
        print("invalid number, try again")
    else: # if valid input
        count += 1
        spent += expense

# print results
print("\n\n############# Results ################")
print("Your budget was", format(budget, '.2f'), "dollars.\nYou spent", format(spent, '.2f'), "dollars.")
print("You spent money on", count, "different items")

# calculate profit and lost
profit = budget - spent
lost = spent - budget

# print profit/loss
if budget > spent:
    print("You saved", format(profit, '.2f'), "dollars")
    if profit > budget / 2:
        print("You saved over half of your budget this month! Go buy yourself something nice.")
    elif profit < 50:
        print("You came withing $50 of going over budget")
elif budget < spent:
    print("You went over-budget by", format(lost, '.2f'), "dollars")
    if lost < 100:
        print("You came withing $100 of staying in budget. You almost made it.")



