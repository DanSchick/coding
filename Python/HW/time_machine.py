###########
# Danny Schick
# CS21A
# Time machine HW
###########

# Get number of seconds from user
seconds = int(input("Enter the number of seconds: "))
# validate input
if seconds < 0:
    print("Invalid input. Seconds must be a positive integer.")
else: # If input is valid
    # Make calculations for days, hours, minutes
    total_sec = seconds # set total as seconds will be subracted
    days = seconds // 86400 # 60 * 60 * 24
    days_rem = seconds % 86400 # days_rem is the seconds remaining from the days calculation
    hours = days_rem // 3600 # 60 * 60
    hours_rem = days_rem % 3600 # find remanining seconds after hours
    minutes = hours_rem // 60
    minutes_rem = hours_rem % 60 # find remaining seconds after minutes
    sec = minutes_rem # seconds is equal to remaining seconds after minutes
    # print the ansewr
    print(total_sec, "seconds =", days, "days,", hours, "hours,", minutes, "minutes", sec, "seconds") # already formatted because input is taken as an integer
