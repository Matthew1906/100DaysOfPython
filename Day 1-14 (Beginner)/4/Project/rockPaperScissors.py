# DAY 4 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: ROCK PAPER SCISSORS
# THINGS I LEARNT: LISTS, RANDOM NUMBERS, MULTILINE STRINGS INSIDE LISTS, INPUT VALIDATION

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

#prompt the player to choose
playerMove = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# check if the player move is in range (there are no typeError checker, since it hasn't been covered yet)
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

