# DAY 15 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: COFFEE MACHINE 
# THINGS I IMPLEMENTED: Dictionaries, Scoping, Functions and Recursions, System Module, F-Strings

# import necessary libraries
from recipes import resources, MENU
from os import system,name

income = 0.0

def clear():
    '''Library Way to clear screen'''
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def init():
    '''Initialize the resources and income'''
    global income #must be global, so it can be initialized
    income = 0.0
    resources["water"]= 300
    resources["milk"]= 200
    resources["coffee"]= 100

def check_resources(order):
    '''Check if the resources are sufficient'''
    if resources['water']< MENU[order]['ingredients']['water']:
        return '  Not enough Water'
    elif resources['milk']< MENU[order]['ingredients']['milk']:
        return '  Not enough Milk'
    elif resources['coffee']< MENU[order]['ingredients']['coffee']:
        return '  Not enough Coffee'
    else:
        return 'available'

def check_order(order):
    '''Check what order is given'''
    if order == 'off':
        return False
    elif order == 'report':
        print(f"  Water: {resources['water']}ml")
        print(f"  Milk: {resources['milk']}ml")
        print(f"  Coffee: {resources['coffee']}gr")
        print(f"  Money: ${income}")
        return True
    elif order == 'restock':
        resources["water"]= 300
        resources["milk"]= 200
        resources["coffee"]= 100
        print("  All resources are restocked!")
        return True
    elif order == 'espresso' or order == 'latte' or order == 'cappuccino':
        enough_resources = check_resources(order)
        if enough_resources=='available':
            return "get Price"
        else:
            print(f" {enough_resources}")
            return True
    else:
        print("  Invalid Order")
        return True

def calc_stock(order):
    '''Recalculate stock'''
    resources["water"]-=MENU[order]['ingredients']['water']
    resources["milk"] -= MENU[order]['ingredients']['milk']
    resources["coffee"] -= MENU[order]['ingredients']['coffee']

def transaction(order):
    '''Transaction'''
    print("  Please insert coins!")
    price = MENU[order]['cost']
    quarters = int(input("  How many quarters? "))*0.25
    dimes = int(input("  How many dimes? "))*0.1
    nickels = int(input("  How many nickels? "))*0.05
    pennies = int(input("  How many pennies? "))*0.01
    if price> quarters+dimes+nickels+pennies:
        print("  Not enough money!")
    else:
        global income
        income+=price
        print(f"  Here is ${round(quarters+dimes+nickels+pennies-price,2)} in change.")
        print(f"  Here is your {order} ☕️ Enjoy!")
        calc_stock(order)

def coffee_machine():
    '''Coffee Machine'''
    order = input(" What do would you like? (espresso/latte/cappuccino): ").lower()
    todo = check_order(order)
    if not todo:
        return
    elif todo == 'get Price':
        transaction(order)
    coffee_machine()

def start_machine():
    '''Driver Program'''
    init()
    coffee_machine()
    if input(" Type 'y' to restart machine, 'n' to exit: ").lower() == 'y':
        clear()
        start_machine()

start_machine()