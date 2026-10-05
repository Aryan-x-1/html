import random

applejuice=15.5
orangejuice=20.0
grapejuice=10.25

total= applejuice + orangejuice + grapejuice

print("Total volume of juice is:", total)

total_integer = int(total)
print("total as integer:", total_integer)

total_string = str(total)
print("The total volume of juice sold is " + total_string + " liters")

bonus = random.randint(5, 10)

final_total = total + bonus

print("Bonus liters:", bonus)
print("Final total:", final_total)