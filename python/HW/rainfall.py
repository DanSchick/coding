totalYears = int(input("How many years?: "))
totalRain = 0
for year in range(1,totalYears+1):
    for month in range(1,13):
        rain = int(input("monthly rainfall?: "))
        totalRain += rain
totalMonths = totalYears * 12
mean = totalRain / totalMonths
print("Total months: ", totalMonths)
print("Total inches of rain: ", totalRain)
print("Average rainfall per month: ", mean)
