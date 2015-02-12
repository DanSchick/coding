##############
# Danny Schick
# CS21A
# Chapter 4 Lab
#############
while True: # loop in case of invalid input
    num = int(input("Enter an integer >= 0: ")) # Get input
    if num == 0: # check for special case
        print(num, "! = 1")
        break # break loop because of valid input
    elif num < 0: # validate input
        print("Invalid number, please try again") # no break because invalid input
    else:
        total = 1
        for i in range(1,num+1):
            total *= i
        print(num, "! = ", total)
        break # break loop because of valid input


