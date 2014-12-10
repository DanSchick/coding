############
# Danny Schick
# CS 21
# Decoder
############

def encrypt(codes):
    infile = input("enter exact name of input file (in example.txt format): ")
    try: # make sure filename is valid
        infile = open(infile, 'r')
    except FileNotFoundError:
        print("That isn't a valid file. Please enter it again.")
        encrypt(codes)
    outfile = input("enter the name of the output file (in example.txt format): ")
    outfile = open(outfile, 'w')
    for line in infile:
        for char in line: # read file character by character
            if char == ' ': # make sure spaces don't crash program
                outfile.write(' ')
            elif char == '\n': # make sure newlines don't crash program
                outfile.write('\n')
            else:
                char = codes[char] # encode or decode character
                outfile.write(char)


def main():
    codeFile = open('codes.txt', 'r') # open the coder file
    codes = {}
    for line in codeFile: # read line from codefile and add to dictionary
        line = line.split()
        codes[line[0]] = line[1]
    ## This choice doesn't matter because encrypt() already can go back and forth. I guess this makes it easier to use?
    choice = input("(1) Encrypt a file | (2) Decrypt a file: ")
    if choice == '1':
        encrypt(codes)
    elif choice == '2':
        encrypt(codes)




main()

