#######################
# MOST FREQUENT CHARACTER
# DANNY SCHICK
# CS 21A
#######################


def main(): # ask for input, evaluate, print
    string = input("Enter a string: ")
    maxOccur = 0
    for i in string: # loop through every letter
        if i.isdigit() is True or i.isspace() is True:
           pass
        else:
            occur = string.count(i)
            if occur > maxOccur:
                maxOccur = occur
                maxLetter = i
    print("\n", maxLetter, "is the most common letter with", maxOccur, "occurences.") # final print




main()
