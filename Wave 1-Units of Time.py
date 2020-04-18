import math

# input

# read the time from the user
day = input("Enter days: ")
day = int(day)
hour = input("Enter hours: ")
hour = int(hour)
minute = input("Enter minutes: ")
minute = int(minute)
second = input("Enter seconds: ")
second = int(second)

# calculate them to seconds
total = day*86400 + hour*3600 + minute*601 + second
total = int(total)

# display the total second to user
print("It can be calculated to " + str(total) + " seconds")
