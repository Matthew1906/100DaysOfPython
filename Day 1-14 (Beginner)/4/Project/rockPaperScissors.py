from os import system, name

def clear():
  '''Library Way to Clear Screen'''
  if name == 'nt':
    _ = system("cls")
  else:
    _ = system("clear")

# ascii art for rock, paper, scissors
symbols = [
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
,
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
,
'''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

# import the random module
import random

def rock_paper_scissors():
  '''Rock Paper Scissors Game'''
  #prompt the player to choose
  try:
    playerMove = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
  except ValueError:
    print("Value Error")
    input("Press enter to continue...")
    clear()
    rock_paper_scissors()
  else:
    # check if the player move is in range
    if playerMove<0 or playerMove>2:
        print("Wrong input! You lose!")
    else:
        # print the player's move
        print(symbols[playerMove])
        print("Computer chose:")
        computerMove = random.randint(0,2)
        print(symbols[computerMove])
        if playerMove==computerMove:
            print("It's a draw!")
        elif playerMove>computerMove or computerMove-playerMove==2:
            print("You Win!")
        else:
            print("You Lose!")
        # 0>2, 0<1
        # 1>0, 1<2
        # 2>1, 2<0
    if input("Type y to play again: ") == 'y':
      clear()
      rock_paper_scissors()

rock_paper_scissors()