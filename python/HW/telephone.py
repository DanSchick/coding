#######################
# TELEPHONE
# DANNY SCHICK
# CS 21A
#######################
def convert(letter): # convert letter to number
    if letter in ['a', 'b', 'c']:
        return 2
    elif letter in ['d', 'e', 'f']:
        return 3
    elif letter in ['g', 'h', 'i']:
        return 4
    elif letter in ['j', 'k', 'l']:
        return 5
    elif letter in ['m', 'n', 'o']:
        return 6
    elif letter in ['p', 'q', 'r', 's']:
        return 7
    elif letter in ['t', 'u', 'v']:
        return 8
    elif letter in ['w', 'x', 'y', 'z']:
        return 9
    else:
        return letter


def main(): # main function
    num = input("Enter the telephone number in the format XXX-XXX-XXXX: ")
    if len(num) != 12:
        print("You have to enter a valid number.")
        main()
    convertNum = ""
    for i in num: # building converted number
        if i.isalpha():
            letter = i.lower()
            letter = str(convert(letter))
            i = letter
        else:
            i = str(i)
        convertNum += i
    print("The phone number is ", convertNum) # final print

main()
