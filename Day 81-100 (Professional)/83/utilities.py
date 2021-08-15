from board import Board
from os import system, name

logo = \
'''
  _______ _        _______           _______         
 |__   __(_)      |__   __|         |__   __|        
    | |   _  ___     | | __ _  ___     | | ___   ___ 
    | |  | |/ __|    | |/ _` |/ __|    | |/ _ \\ / _ \\
    | |  | | (__     | | (_| | (__     | | (_) |  __/
    |_|  |_|\\___|    |_|\\__,_|\\___|    |_|\\___/ \\___|

                      1. Play
                      2. Exit'''

def clear():
    '''Library Way to clear screen'''
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def print_board(board:Board):
  '''Print Tic Tac Toe Board'''
  print(\
f'''
  TIC TAC TOE
  ___________
 |   |   |   |
 | {board.get_tile(0)} | {board.get_tile(1)} | {board.get_tile(2)} |
 |___|___|___|
 |   |   |   |
 | {board.get_tile(3)} | {board.get_tile(4)} | {board.get_tile(5)} |
 |___|___|___|
 |   |   |   |
 | {board.get_tile(6)} | {board.get_tile(7)} | {board.get_tile(8)} |
 |___|___|___|
''')

def prompt(possible_moves:list, player:str, board:Board):
  '''Prompt player's move'''
  while True:
    clear()
    print_board(board)
    print(f" It's {player}'s turn!")
    print(f' Possible moves: {possible_moves}')
    coordinate = int(input(" Insert the coordinate for your next move: "))
    if coordinate in possible_moves:
      return coordinate
