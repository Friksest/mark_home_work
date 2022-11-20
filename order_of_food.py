food_1_name      = 'Pizza'
food_2_name      = 'Rolls'
food_1_price     = 100   
food_2_price     = 300   
food_1_available = 5
food_2_available = 10
free_delivery_cost = 3000
print("You may order up to ", food_1_available, food_1_name, "and up to ", food_2_available, food_2_name)
food_1_quantity  = int(input('How many ' + food_1_name + ' do you want ?'))
food_2_quantity  = int(input('How many ' + food_2_name + ' do you want ?'))


if food_1_quantity <= food_1_available and food_1_quantity > 0:
    food_1_cost = food_1_quantity * food_1_price
else: print("You have choose unable quantity of ", food_1_name)

if food_2_quantity <= food_2_available and food_2_quantity > 0:
    food_2_cost = food_2_quantity * food_2_price
else: print("You have choose unable quantity of ", food_2_name)

print('You have ordered ', food_1_quantity, ' x ',  food_1_name, ' = ',food_1_cost)      
print('You have ordered ', food_2_quantity, ' x ',  food_2_name, ' = ',food_2_cost) 

want_delivery = str(input("Do you want a delivey? (yes/no)"))
if want_delivery == 'yes':
    total_cost_ordered = food_1_cost + food_2_cost
    if total_cost_ordered >= free_delivery_cost:
        print('You have free delivery')
    else: print("Your delivery cost is 200")
else:
    print("Have a nice day")