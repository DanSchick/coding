################
# Danny Schick
# CS21A
# Distance Calculator
###############

def main(): # function to accept input
    speed = int(input("what is the speed in mph?: "))
    hours = int(input("how many hours of traveling?: "))
    show_travel(speed, hours) # calculate and print data

def show_travel(speed, hours): # calculate function
    totaldistance = 0
    hourcount = 0
    print("hours   |   distance") # print table headers
    while hourcount != hours: # loop through the amount of hours, printing as we go
        hourcount += 1
        distance = hourcount * speed
        totaldistance += distance
        print(hourcount, "    |   ", distance)

main()
