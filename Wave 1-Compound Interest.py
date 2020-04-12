import math

# Inputs

# input the money user deposited into the account
money = input("Enter the money you deposited into your account: ")
money = float(money)

# calculate the first year interest
first_year_interest = money*0.04
first_year_interest = float(first_year_interest)

# calculate the second year interest
second_year_interest = (money + first_year_interest)*0.04
second_year_interest = float(second_year_interest)

# calculate the third year interest
third_year_interest = (money + first_year_interest + second_year_interest)*0.04
third_year_interest = float(third_year_interest)

# calculate money in account after each year
one_year_money = money + first_year_interest
one_year_money = float(one_year_money)
one_year_money = round(one_year_money, 2)
two_years_money = money + first_year_interest + second_year_interest
two_years_money = float(two_years_money)
two_years_money = round(two_years_money, 2)
final_money = money + first_year_interest + second_year_interest + third_year_interest
final_money = float(final_money)
final_money = round(final_money, 2)

# concatenation
print("The money after first year in your account is: $" + str(one_year_money))
print("The money after second year in your account is: $" + str(two_years_money))
print("The money will finally present in your account after three years with: $" + str(final_money))
