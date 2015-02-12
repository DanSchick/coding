##################
# Leap Year Calculator by Danny Schick
##################

print("Welcome to my leap year Calculator")
print("If you give me a year, I can tell you if it is a leap year or not") # introduction

year = int(input("What year? ")) # ask for input

# leap year formulaa

if year < 0: # input validation
    print("Invalid year.")
elif year % 4 != 0:
    print("The year", year, "is not a leap year")
elif year % 100 != 0:
    print("The year", year, "is a leap year")
elif year % 400 != 0:
    print("The year", year, "is not a leap year")
else:
    print("The year", year, "is a leap year")
