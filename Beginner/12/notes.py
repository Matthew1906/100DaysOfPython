# SCOPE
enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function : {enemies}")
increase_enemies()
print(f"enemies outside function : {enemies}")

# global scope = exists outside functions
player_health = 10

def drink_potion():
    # local scope = exists within functions
    potion_strength = 2
    print(player_health)
# drink_potion()
# the 'potion_strength' is in a local scope, instead of global scope

# CONCEPT = NAMESPACE -> valid in certain scopes

# THERE ARE NO BLOCK SCOPES

# example

game_level = 3
enemies = ["Skeleton","Zombie","Alien"]
if game_level<5:
    new_enemy = enemies[0]
print(new_enemy)


# modifying global scope
enemies = 1
def increase_enemies_1():
    global enemies # not suggested
    # define that the enemies is a global variable
    enemies+=1
    print(f"enemies inside function : {enemies}")

def increase_enemies_2():
    return enemies+1

enemies = increase_enemies_2()
print(f"enemies outside function : {enemies}")

# global constants -> useful for constants

PI = 3.1459
URL = 'https://www.google.com/'
# naming conventions

