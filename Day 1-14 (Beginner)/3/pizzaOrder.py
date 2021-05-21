# EXERCISE 4 = PIZZA ORDER

print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want to add pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

price = 0
if size=='S':
    if add_pepperoni =='Y':
        price+=17
    else:
        price+=15
else:
    if add_pepperoni =='Y':
        price+=3
    if size=='M':
        price+=20
    else:
        price+=25
if extra_cheese=='Y':
    price+=1

print(f"Your final bill is: ${price}")