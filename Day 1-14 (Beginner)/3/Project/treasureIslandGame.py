from os import system, name

def clear():
  '''Library Way to Clear Screen'''
  if name == 'nt':
    _ = system("cls")
  else:
    _ = system("clear")

def treasure_island():
  '''Treasure Island Game'''
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
  try:
    direction = input('''
        You're at a cross road. Where do you want to go? 
        Type "left" or "right"
        >> ''').lower()
    if not direction == 'left' and not direction =='right':
      raise ValueError("Wrong Direction!")
  except ValueError as error_message:
    print(error_message)
    input("Press enter to continue")
    clear()
    treasure_island()
  else:
    if direction == 'left':
      try:
        go_to_island = input('''
            You come to a lake. There is an island in the middle of the lake. 
            Type "wait" to wait for a boat. Type "swim" to swim across.
            >> ''').lower()
        if not go_to_island == 'wait' and not direction =='swim':
          raise ValueError("Wrong Choice")
      except ValueError as error_message:
        print(error_message)
        input("Press enter to continue")
        clear()
        treasure_island()
      else:
        if go_to_island =='wait':
          try:
            color = input('''
                You arrive at the island unharmed. You entered a large castle.
                Inside the castle there are 3 large doors with different colors. 
                One red, one yellow, and one blue. Which colour do you choose?
                >> ''').lower()
            if color not in ['red','yellow','blue']:
              raise ValueError("Wrong Color")
          except ValueError as error_message:
            print(error_message)
            input("Press enter to continue")
            clear()
            treasure_island()
          else:
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
        elif go_to_island == 'swim':
            print('''
                No one can swim across the Lake of Frozen Mist.
                The frozen mist freezes your body. You can no longer move.
                You died! Game Over! 
            ''')
    elif direction == 'right':
        print('''
            You took the wrong turn, you met the King of the East and he thinks you're a spy!
            You're executed by the kingdom of the East. Game Over..
        ''')
  if input("Type y to play again: ") == 'y':
    input("Press enter to continue")
    clear()
    treasure_island()
treasure_island()