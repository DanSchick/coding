p = float(input("Present value of the account?: "))
i = float(input("monthy interest rate (in decimal form)?: "))
t = float(input("Number of months?: "))


def future(p, i, t):
    num = p * (1+i)**t
    return num


print(future(p, i ,t))
