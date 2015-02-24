#############
# Danny Schick
# CS21A
# Chapter 4 Lab
#############

import random # to make random number

# set constants
minimum = 1
maximum = 100

game = True # condidition to play another game

while game is True:
    # create the random number
    num = random.randint(minimum, maximum)

    # initialize loop variables
    guess = 0
    count = 0
    MAX_TRIES = 5

    # begin loop
    while guess != num and count < 5:
        guess = int(input("Enter your integer guess: "))

        # validate input
        if guess > 100:
            print("The number can't be above 100. Please try again")
        elif guess < 0:
            print("The number can't be less than 0. Please try agian.")
        else: # if valid input
            count += 1 # incremement count because input is valid

            # check to see if guess is too high or low
            if guess > num:
                print("Too high")
            elif guess < num:
                print("Too low")
            elif guess == num:
                print("Correct!")

    # print game verdict
    if guess == num: # check to see why loop was exited
        print("You got the number after", count, "guesses!")
    elif count == 5:
        print("You didn't get it in 5 tries. The number was", num)

    # play again?
    choice = input("Would you like to play again? (Y/N): ")
    if choice == 'n' or 'N' or 'no':
        print("Okay, thanks for playing!")
        game = False




