import random

rice_price = 45
sugar_price = 40
oil_price = 130

rice_quantity = 3
sugar_quantity = 2.5
oil_quantity = 1.8

rice_cost = rice_price * rice_quantity
sugar_cost = sugar_price * sugar_quantity
oil_cost = oil_price * oil_quantity

total_cost = rice_cost + sugar_cost + oil_cost
print("rice cost:", rice_cost)
print("sugar cost:", sugar_cost)
print("oil cost:", oil_cost)
print("total cost:", total_cost)

total_cost_integer = int(total_cost)
print("total cost as integer:", total_cost_integer)

total_cost_string = str(total_cost)
print("The total cost of items purchased is " + total_cost_string + " rupees")

delivery_charge = random.randint(5, 10)\

final_total_cost = total_cost + delivery_charge
print("Delivery charge:", delivery_charge)
print("Final total cost:", final_total_cost)