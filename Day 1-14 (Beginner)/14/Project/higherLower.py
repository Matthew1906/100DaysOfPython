# DAY 14 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: HIGHER LOWER 
# THINGS I IMPLEMENTED: Random Module, Functions and Recursions, System Module, F-Strings

from game_data import data
from art import logo,vs 
from random import randint
from os import system,name

def clear():
    '''Library Way to clear screen'''
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def compare(a,b):
    '''Compare the followers count between 2 accounts'''
    if a['follower_count']>b['follower_count']:
        return 'a'
    else:
        return 'b'

def higher_lower():
    '''Higher Lower Game'''
    wins = 0
    print(logo)
    indexA = randint(0,len(data)-1)
    while True:
        # randomize index    
        indexB = randint(0,len(data)-1)
        while indexA == indexB:
            indexB = randint(0,len(data)-1)
        a = data[indexA]
        b = data[indexB]
        # prompt
        print(f" Compare A: {a['name'].title()}, a {a['description']}, from {a['country'].title()}.")
        print(vs)
        print(f" Against B: {b['name'].title()}, a {b['description']}, from {b['country'].title()}.") 
        answer = compare(a,b)
        more_follower = input(" Who has more followers? Type 'A' or 'B': ").lower()
        clear()
        print(logo)
        if more_follower == answer:
            wins+=1
            print(f" You're correct!, Current score: {wins}")
            if answer == 'b':
                indexA = indexB
        else:
            print(f" Sorry that's wrong. Final score: {wins}")
            if input(" Do you want to play again? Type 'Y' or 'N': ").lower() == 'y':
                clear()
                higher_lower()
            break
higher_lower()