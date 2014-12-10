#Group Projects

def main():

    selected = False #variable to check if a menu item has been selected

    while selected == False:
        #ask the user what they want to do
        choice = input("What would you like to do? 1 Create Account, 2 Login, 3 Quit: ")

        #execute a function depending on their answer
        if choice == '1':
            selected = True
            createAccount()
        if choice == '2':
            selected = True
            useAccount()
        if choice == '3':
            selected = True
            quitProgram()
        else:
            selected = False


def options(fileName):
        choice = input("Display All Entries (1) | Search (2) | Add Entry (3) | Delete Entry (4) | Log Out (5): ")
        if choice == '1':
            displayAll(fileName)
        elif choice == '2':
            search(fileName)
        elif choice == '3':
            addEntry(fileName)
        elif choice == '4':
            deleteEntry(fileName)
        elif choice == '5':
            logOut()
        else:
            print("Invalid input. Try again please.")
            options(fileName)


####################################
#Make an account
def createAccount():
    username = input('Enter a username here: ')
    fileName = username + '.txt'
    account = open(fileName, 'w')
    print('Account succesfully made!')

###################################
#use the account
def useAccount():
    username = input('Enter your username here: ')
    fileName = username + '.txt'
    options(fileName)

def displayAll(fileName):
    infile = open(fileName, 'r')
    name = infile.readline()
    while name != '':
        calories = infile.readline()
        style = infile.readline()
        cost = infile.readline()

        name = name.rstrip('\n')
        calories = calories.rstrip('\n')
        style = style.rstrip('\n')
        cost = cost.rstrip('\n')

        print('Name:', name)
        print('Calories:', calories)
        print('Style:', style)
        print('Cost:', cost)
        print()

        name = infile.readline()

    infile.close()
    options(fileName)


def search(fileName):
    infile = open(fileName, 'r')
    search = input("Enter the exact name of item: ")
    options(fileName)




def addEntry(fileName):
    fileName = open(fileName, 'a')
    try:
        numItems = int(input('How many items would you like to add?'))
        for count in range(1, numItems+1):
            print('Enter data for item #', count, sep='')
            name = input('Name: ')
            calories = input('Calories: ')
            style = input('Style: ')
            cost = input('Cost: ')

            fileName.write(name + '\n')
            fileName.write(calories + '\n')
            fileName.write(style + '\n')
            fileName.write(cost + '\n')
    except BaseException:
        print("Invalid answer. Please log in again.")
        useAccount()

        print()
    fileName.close()
    print('Items have been written to your account.')
    print('Please log in to perform additional operations.')
    useAccount()

def deleteEntry(fileName):
    f = open(fileName, 'r')
    entryToDelete = input("Enter the name of the item you want to delete: ")
    f.seek(0)
    lineNumber = 0
    for line in f:
        lineNumber += 1
        if line == entryToDelete:
            f.close()
            f = open(fileName, 'w')
            f.seek(lineNumber)

def logOut():
    main()

###################################
#quit the program
def quitProgram():
    pass
main()
