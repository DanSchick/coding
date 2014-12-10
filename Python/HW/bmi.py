weight = float(input("What is your weight in lbs?: "))
height = float(input("What is your height in inches?: "))
bmi = weight * (730/(height*height))
print(bmi)
if bmi < 18.5:
    print("You are underweight")
elif bmi > 25:
    print("You are overweight")
else:
    print("You are optimal weight.")
