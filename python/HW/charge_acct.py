#########################
# Danny Schick
# CS 21A
# Charge Accounts
##########################

def numCheck(accounts, number): # check to see in number in accounts
    for i in accounts:
        if i == number:
            return True
        else:
            return False


def main():
    infile = open('charge_accounts.txt','r')
    accounts = []
    for i in infile:
        i = i.rstrip("\n")
        accounts.append(i)
    number = input("What is the account number?: ")
    if numCheck(accounts, number):
        print("The number is valid")
    else:
        print("The number is invalid")



main()
