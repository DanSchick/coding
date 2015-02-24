#########
# Danny Schick
# CS21A
# Biggest Number HW
#########

# Get numbers from user (this assumes the input is given as an integer)
num1 = int(input("First number? "))
num2 = int(input("Second number? "))
num3 = int(input("Third number?"))
# make calculations to find descending order
sortednums = sorted([num1, num2, num3], reverse=True) # this function returns given numbers in descending order because the reverse flag is true
# print sorted list
print("sorted list:", sortednums)
