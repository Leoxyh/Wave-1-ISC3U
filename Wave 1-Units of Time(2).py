import math

# input

# read the second from the user
total = input("Enter the second: ")
total = int(total)

# calculate the second to days, hours, minutes, seconds
day = total // 86400
day = int(day)
hour = (total - day*86400) // 3600
hour = int(hour)
minute = (total - day*86400 - hour*3600) // 60
minute = int(minute)
second = total - day*86400 - hour*3600 - minute*60

# display total days, hours, minutes, seconds

print("It can be calculated to: " + str(day) + " days " + str(hour) + " hours " + str(minute) + " minutes " + str(second) + " seconds ")
