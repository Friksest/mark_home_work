#     LIFT APP
# --------------------
#   7 |[   ]|
#   6 |     |
#   5 |     |
#   4 |     |  H
#   3 |     |
#   2 |     |
#   1 |     |
#--------------------
#   1. call
#   2. destination
#   3. enter
#   4. exit


#   * input
#   * list
#   * functions
#   * file
##############################
from os import system
from time import sleep

floor_max = 7
floor_min = 1

lift_floor  = 1 
human_floor = 6

human_in_lift = False

def printFloors():
    print("-" * 20)
    for floor in range(floor_max, floor_min-1, -1):
        if human_in_lift and floor == lift_floor:
            print(f"{floor} | [H] |")
        elif floor == lift_floor and floor == human_floor and not human_in_lift:
            print(f"{floor} | [ ] |  H")
        elif floor == human_floor and not human_in_lift:
            print(f"{floor} |     |  H")
        elif floor == lift_floor:
            print(f"{floor} | [ ] |")
        else:
            print(f"{floor} |     |")
    print("-" * 20)

def printMenu():
    print("1. call")
    print("2. destination")
    print("3. enter")
    print("4. exit")
    option = int(input(">>> "))
    return option

def call():
    # call work only DOWN v  - DONE
    # HW1 :if / else  -->  DOWN / UP
    global lift_floor
    while lift_floor != human_floor:
        if lift_floor > human_floor:
            sleep(0.5)
            lift_floor -= 1
            system("clear")
            printFloors()
        elif lift_floor < human_floor:
            sleep(0.5)
            lift_floor += 1
            system("clear")
            printFloors()
        elif lift_floor == human_floor:
            pass
            printFloors()
            
def destination():
    # destination work only DOWN v  - DONE
    # HW2 :if / else  -->  DOWN / UP
    global lift_floor
    where_to = int(input("which floor: "))
    while lift_floor != where_to:
        if lift_floor > where_to:
            sleep(0.5)
            lift_floor -= 1
            system("clear")
            printFloors()
        elif lift_floor < where_to:
            sleep(0.5)
            lift_floor += 1
            system("clear")
            printFloors()
        elif lift_floor == where_to:
            print("You have arrived")
            printFloors()

def enter():
    global human_in_lift
    if lift_floor == human_floor:
        human_in_lift = True
    else:
        print("WARNING you can fall!!!")

def exit():
    global human_in_lift
    global human_floor
    if human_in_lift:
        human_in_lift = False
        human_floor = lift_floor
    else:
        print("WARNING human not in lift!!!")

##############################

while True:
    system("clear")
    printFloors()
    option = printMenu()
    if option == 1:
        call()
    elif option == 2:
        destination()
    elif option == 3:
        enter()
    elif option == 4:
        exit()












