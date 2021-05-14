# DAY 3 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: TREASURE ISLAND
# THINGS I LEARNT: IF ELSE, LOGICAL OPERATORS, MULTILINE STRING, RAW STRING

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# UNLIKE THE EXAMPLE, AFTER EVERY CHOICES, THE MESSAGE WILL BE PRINTED WITH AN ADDED PADDING TO THE RIGHT
direction = input('''
    You're at a cross road. Where do you want to go? 
    Type "left" or "right"
    >> ''').lower()
if direction == 'left':
    go_to_island = input('''
        You come to a lake. There is an island in the middle of the lake. 
        Type "wait" to wait for a boat. Type "swim" to swim across.
        >> ''').lower()
    if go_to_island =='wait':
        color = input('''
            You arrive at the island unharmed. There is a house with 3 doors. 
            One red, one yellow, and one blue. Which colour do you choose?
            >> ''').lower()
        if color == 'red':
            print('''
            You entered the Great Dragon's Chamber. 
            You disturbed its slumber, The Great Dragon burns you.
            You Died! Game Over!
            ''')
        elif color == 'yellow':
            print('''
            You have chosen the treasure vault. 
            You are eligible to take as much treasure as you want!
            Congratulations! You win the game!!
            ''')
        elif color == 'blue':
            print('''
            You entered the domain of the Monarch of Shadows. 
            The Lord decided to curse you to become his shadow soldier.
            You lost! Game Over!
            ''')
    else:
        print('''
        No one can swim across the Lake of Frozen Mist.
        The Frozen mist freezes your body. You can no longer move.
        You died! Game Over! 
        ''')
else:
    print('''
    You took the wrong turn, you met the king of the north and he thinks you're a spy!
    You're executed by the kingdom of the north. Game Over..
    ''')
