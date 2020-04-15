import math

# input

# read the money from the user and the price of the item
money = input("Enter your money for purchase the item: ")
money = int(money)
price = input("Enter the price of the item: ")
price = float(price)

# calculate the change
change = money - price
change = float(change)

# calculate the number of coins for change
if (money - price) < 0:
    print("Not enough money entered, please add more")

else:
    toonies = change // 2
    loonies = (change - toonies*2) // 1
    quarters = (change - toonies*2 - loonies) // 0.25
    dimes = (change - toonies*2 - loonies - quarters*0.25) // 0.1
    nickels = (change - toonies*2 - loonies - quarters*0.25 - dimes*0.1) // 0.05
    pennies = (change - toonies*2 - loonies - quarters*0.25 - dimes*0.1 - nickels*0.05) / 0.01
    print("The number of toonies the machine will give change is :" + str(toonies))
    print("The number of loonies the machine will give change is :" + str(loonies))
    print("The number of quarters the machine will give change is :" + str(quarters))
    print("The number of dimes the machine will give change is :" + str(dimes))
    print("The number of nickels the machine will give change is :" + str(nickels))
    print("The number of pennies the machine will give change is :" + str(round(pennies, 1)))
