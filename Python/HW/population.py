#############
# Danny Schick
# CS21A
# Population Estimator
#############

# define current population and year
currentPop = 320387104
currentYear = 2015

# define rates
birth = 8 # 1 birth every 8 seconds
death = 11
immigrant = 30

# find rates per year
secondsInYear = 60 * 60 * 24 * 365 # find how many seconds are in one year
birthYear = secondsInYear / birth
deathYear = secondsInYear / death
immigrantYear = secondsInYear / immigrant

# find out how many years to predict
# set inputLoop to true for validation
inputLoop = True
while inputLoop == True:
    years = int(input("How many years would you like to predict?: "))

    # validate input
    if years < 0:
        print("Invalid number of years. Years must be positive")
    elif years == 0:
        print("The current population is", currentPop)
    else: # if input is valid
        inputLoop = False


# define a variable for the population to be changed
population = currentPop

# to make output look nice
print("\n\n##### Results ###########")
# use a for loop to estimate and print
for i in range(1, years + 1):
    population += birthYear # for every year, add the number of births per year
    population -= deathYear
    population += immigrantYear

    year = currentYear + i # for the purposes of printing the table

    print(year, "       ", format(population, ',.0f'))
