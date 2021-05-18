# DAY 7 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: HANGMAN
# THINGS I LEARNT:RANDOM, SELECTION, REPETITION, LISTS, STRING FUNCTIONS, GAME LOGIC, IMPORTING MODULES

# 1. Import necessary libraries (in this case: random)
import random
from art import logo, symbol
from answerkey import answers

# 2. Create ASCII Art for decoration purposes (in art.py)

# 3. Set the answer and initial values needed
# create list of answers (in answerkey.py)

# you can use this, or you can use random.choice
answer = list(answers[random.randint(0,len(answers)-1)].lower())

# 4. Set the initial values for the game value
current_answer = ["_"]*len(answer)
guessed_letters = [] # store guessed letters -> improve user experience i guess
num_of_guesses = 7 # Different ASCII art -> different lives :)
guess_counter = 0
win = False

# 5. Create helper functions
def clear(): # clear screen functions -> no module style
    i = 0
    while i<50:
        print("")
        i+=1
# clear function is only for decorative purposes

def checkLetter(letter):
    if letter not in answer:
        guessed_letters.append(letter)
        print("You guessed wrong!")
        return 1
    elif letter in current_answer:
        print("You've already guessed it!")
    else:
        guessed_letters.append(letter)
        for i in range(len(answer)):
            if answer[i]==letter:
                current_answer[i] = answer[i]
    return 0

def checkAnswer():
    if "".join(answer) == "".join(current_answer):
        return True
    return False

# 6. Main program
print(logo)
input("Start Game".center(45," "))
clear()
while guess_counter<num_of_guesses and not win:
    print("\nCurrent Answer: "+ " ".join(current_answer))
    print("Guessed Letters: ["+", ".join(guessed_letters)+"]")
    print(symbol[guess_counter])
    guess = input("Guess a letter: ")
    if len(guess)!=1:
        clear()
        continue
    guess_counter+= checkLetter(guess.lower())
    input("Press enter to continue..")
    win = checkAnswer()
    clear()

# 7. End of Game
answer = "".join(answer)
if guess_counter==num_of_guesses:
    print(symbol[guess_counter])
    print(f"You lost! The answer is {answer}")
else:
    print(symbol[8])
    print(f"You Win! The answer is {answer}")