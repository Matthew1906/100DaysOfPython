# DAY 16 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: COFFEE MACHINE (OOP) 
# THINGS I IMPLEMENTED: Classes and Objects, Functions and Recursions, System Module

# import all necessary modules
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system,name

# declare all objects
coffee_shop = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

def clear():
    '''Library Way to clear screen'''
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def start_machine(coffee_machine):   
    ''' coffee machine'''
    order = input(f" What do would you like? ({coffee_shop.get_items()[:len(coffee_shop.get_items())-1]}): ").lower()
    if order=='off':
        clear()
        return coffee_machine
    elif order == 'report':
        coffee_machine.report()
        money_machine.report()
    elif order == 'restock':
        coffee_machine = CoffeeMaker()
        print(f"All resources have been restocked!")
    elif coffee_shop.find_drink(order)!= None:
        drink = coffee_shop.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
    input()
    clear()
    start_machine(coffee_machine)

'''Driver Program'''
coffee_machine = start_machine(coffee_machine)