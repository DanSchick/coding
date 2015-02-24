#######################
# CHARACTER READER
# DANNY SCHICK
# CS 21A
#######################

def main():
    filename = input("Enter name of file in 'example.txt' format: ")
    try:
        infile = open(filename,'r') #in case user specifies a nonreal file
    except FileNotFoundError:
        print("No such file found. Make sure you spell it right.\n")
        main()
    infile = open(filename,'r')
    upper = 0 # declaring various counters
    lower = 0
    digits = 0
    whitespaces = 0
    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    alph = alphabet.split(' ', len(alphabet)) # create a list of individual letters
    ALPH = alphabet.upper().split(' ', len(alphabet)) # CREATES A LIST OF CAPITILIZED LETTERS
    for line in infile:
        for word in line:
            for ch in word:
                if ch in ALPH: # check if uppercase
                    upper += 1
                elif ch in alph: # check if lowercase
                    lower += 1
                if ch.isdigit():
                    digits += 1
                if ch.isspace():
                    whitespaces += 1
    print("\nUppwercase letters: ", upper, "\nLowercase letters: ", lower, "\nDigits: ", digits, "\nWhitespaces: ", whitespaces)



main()
