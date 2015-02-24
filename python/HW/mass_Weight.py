############
# Danny Schick
# CS21A
# Mass to weight calculator
###########

# Get mass as a float
mass = float(input("What is the object's mass in kg?: ")) # getting input
# Validate input
if mass < 0:
  print("that's an invalid mass.")
# if input is valid
elif mass > 0:
  weight = mass * 9.8 # make calculation
  print("the object is", format(weight, '.1f'), "Newtons") # print weight
  # Determine whether object is too light or too heavy
  if weight < 10:
    print("the object is too light") # print results
  elif weight > 1000:
    print("the object is too heavy")
