# DAY 12 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: GUESS THE NUMBER 
# THINGS I IMPLEMENTED: Random Module, Functions

# import necessary libraries
import random, art

def get_num_of_attempts(difficulty):
    '''Set number of attempts'''
    # you can also use global variables
    if difficulty == 'easy':
        return 10
    return 5

def check_guesses(guess, answer):
    '''Check the player's guess'''
    if guess==answer:
        print(f" You got it!", end = " ")
        return True
    elif guess>answer:
        print(" Too High.")
        return False
    else:
        print(" Too Low.")
        return False

print(art.logo)
print(" Welcome to the Number Guessing Game!")
print(" I'm thinking of a number between 1 and 100.")
# Initialize answer and number of attempts
answer = random.randint(1,100)
difficulty = input(" Choose a difficulty. Type 'easy' or 'hard'!: ")
attempts = get_num_of_attempts(difficulty)
while attempts!=0: # Game Loop
    print(f" You have {attempts} remaining to guess the number.")
    guess = int(input(" Make a guess: ")) # Player's guess
    if check_guesses(guess, answer):
        break # If the answer is correct, just break the loop
    else:
        attempts-=1
        if attempts>0:
            print(" Guess Again.")
        else:
            print(f" You Lost!", end= " ")
print(f"The answer is {answer}")