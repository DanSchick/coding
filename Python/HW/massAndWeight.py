mass = float(input("What is the object's mass in kg?: ")) # getting input
if mass < 0: # validate input
  print("that's an invalid mass.")
elif mass > 0:
  weight = mass * 9.8
  print("the object is", weight, "Newtons") # print weight
  if weight < 100:
    print("the object is too light")
  elif weight > 500:
    print("the object is too heavy")
