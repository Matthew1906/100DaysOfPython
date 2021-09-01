# Modules
from board import Board
from utilities import logo, print_board, prompt, clear

# Constants
PLAYER1 = 'X'
PLAYER2 = 'O'

# Functions
def tictactoe():
    '''Tic Tac Toe Gameplay'''
    print("\n Let's play Tic Tac Toe!")
    player1 = input(f" Insert player 1 ({PLAYER1}) name: ")
    player2 = input(f" Insert player 2 ({PLAYER2}) name: ")
    board = Board()
    while True:
        move = prompt(board.possible_moves(), player1, board)-1
        board.set_tile(PLAYER1, move)
        check = board.check_board(PLAYER1) 
        if check != False:
            break
        move = prompt(board.possible_moves(), player2, board)-1
        board.set_tile(PLAYER2, move)
        check = board.check_board(PLAYER2) 
        if check != False:
            break
    clear()
    print_board(board)
    if check == 'DRAW':
        print(" It's a Draw!")
    elif check == PLAYER1:
        print(f" {player1} ({PLAYER1}) wins!")
    elif check == PLAYER2:
        print(f" {player2} ({PLAYER2}) wins!")
    input(" Press enter to continue... ")
    
while True:
    clear()
    print(logo)
    menu = input('                      >> ')
    if menu == '1':
        tictactoe()
    elif menu == '2':
        break