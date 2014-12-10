budget = float(input("How much have you budgeted for this month?: "))
loop = True
spent = 0
while loop is True:
    expense = float(input("Enter an Expense (0 to exit): "))
    if expense == 0:
        loop = False
    elif expense < 0:
        print("invalid number, try again")
    else:
        spent += expense

print("Your budget was", budget, "dollars.\nYou spent", spent, "dollars.")
profit = budget - spent
lost = spent - budget
if budget > spent:
    print("You saved", profit, "dollars")
elif budget < spent:
    print("You went over-budget by", lost, "dollars")

