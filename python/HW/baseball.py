#########################
# Danny Schick
# CS 21A
# World Series Winner
#########################

def main():
    infile = open('WorldSeriesWinners.txt','r')
    search = input("Enter the EXACT name of the team you are looking for: ")
    yearcount = 1902
    wins = 0
    for i in infile:
        yearcount += 1
        i = i.rstrip("\n")
        if i == search:
            wins += 1
    print(search, "has won", wins, "World Series.")

main()



