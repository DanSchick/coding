1  p = float(input("Present value of the account?: "))
2  i = float(input("monthy interest rate (in decimal form)?: "))
3  t = float(input("Number of months?: "))
4  
5  
6  def future(p, i, t):
7      num = p * (1+i)**t
8      return num
9  
10  
11  print(future(p, i ,t))
