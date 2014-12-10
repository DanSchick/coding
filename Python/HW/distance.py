speed = int(input("what is the speed in mph?: "))
hours = int(input("how many hours of traveling?: "))
totaldistance = 0
hourcount = 0
print("hours   |   distance")
while hourcount != hours:
    hourcount += 1
    distance = hourcount * speed
    totaldistance += distance
    print(hourcount, "    |   ", distance)
