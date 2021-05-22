# DAY 11 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: BLACKJACK
# THINGS I IMPLEMENTED: Random Module, Functions, Recursion, Selection, Blackjack concept

# import necessary libraries
import random, art

def clear():
    '''simple clear function to maybe improve readability'''
    for _ in range(35):
        print()

def count_total(cards):
    '''count the total amount of cards'''
    total = 0
    for i in range(len(cards)):
        total+=cards[i]
    return total

# deal cards to the player or the computer
def deal_cards(cards):
    new_card = random.randint(2,14)
    # condition for ace
    if new_card==11 and new_card+count_total(cards)>21:
        new_card = 1
    # instead of randomizing from lists, i made an extra condition that will result the same
    elif new_card>=12:
        new_card = 10
    cards.append(new_card)

def checkBlackjack(cards):
    '''Check if current cards are blackjack'''
    if len(cards)==2 and count_total(cards)==21:
        return True
    return False

def finalResult(computer_cards, player_cards):
    '''Find the result of the game (Win|Draw|Lose)'''
    # if the computer achieves blackjack
    if checkBlackjack(computer_cards):
        return "You Lose"
    # player's and computer's total are in range, but player's total is bigger
    # This condition also works for if the user gets blackjack because it will definitely fulfill this condition
    elif count_total(computer_cards)<count_total(player_cards)<=21:
        return "You Win"
    # computer's total are out of range, and player's total is in range
    elif count_total(computer_cards)>21 and count_total(player_cards)<=21:
        return "You Win"
    # player's total are not in range
    elif count_total(player_cards)>21:
        return "You Lose"
    # player's and computer's total are in range, and computer's total is bigger 
    elif count_total(player_cards)<count_total(computer_cards)<=21:
        return "You Lose"
    else:
        return "It's a Draw"

def get_string(cards):
    '''Convert the integer list into string'''
    player_string = list(map(str,cards))
    return ', '.join(player_string)

def blackjack():
    '''Blackjack Game'''
    player_cards = []
    computer_cards = []
    # Deal the first 2 cards
    for _ in range(2):
        deal_cards(player_cards)
        deal_cards(computer_cards)
    print(f"Your cards: [{get_string(player_cards)}]")
    print(f"Computer's first card: {str(computer_cards[0])}")
    # if the first deals result in blackjack, there is no need for any additional draws
    if count_total(player_cards)!=21 and count_total(computer_cards)!=21:
        # user can deal more cards while the total is less than to 21
        # since 21 means its at a limit, i don't see any purpose in dealing again
        while count_total(player_cards)<21:
            if input("Type 'y' to deal more cards, type 'n' to pass\n>> ") == 'y':
                deal_cards(player_cards)
                print(f"Your cards: [{get_string(player_cards)}]")
            else:
                break
        # the computer can get more cards while the total is <= 16
        while count_total(computer_cards)<=16:
            deal_cards(computer_cards)
    clear()
    print(art.logo)
    print(f"Your final hand: [{get_string(player_cards)}]")
    print(f"Computer's final hand: [{get_string(computer_cards)}]")
    print(finalResult(computer_cards, player_cards))
    play_again = input("Do you want to play again? Type 'y' or 'n'!\n>> ")
    if play_again == 'y':
        clear()
        print(art.logo)
        blackjack()
    return
    
def start_game():
    '''Driver Program to start the Blackjack'''
    print(art.logo)
    start = input("Do you want to play a game of blackjack? Type 'y' or 'n'!\n>> ")
    if start == 'y':
        blackjack()   
    return
start_game()