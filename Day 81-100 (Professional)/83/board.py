class Board():
    # Initialize Board
    def __init__(self):
        '''Initialize the tiles with private attributes'''
        self.__tiles = list(map(str, range(9)))
    
    # Get tile value
    def get_tile(self, index:int):
        '''Getter for the tile'''
        if self.__tiles[index] not in list(map(str, range(9))):
            return self.__tiles[index]
        else:
            return str(int(self.__tiles[index])+1)

    # Add symbol
    def set_tile(self, symbol, coordinate:int):
        '''Setter for the tile'''
        if self.__tiles[coordinate] not in list(map(str, range(9))):
            return False
        self.__tiles[coordinate] = symbol
        return True

    # Print board
    def possible_moves(self):
        '''Returns a list of unoccupied tiles in the board'''
        return [ index+1 for index in range(len(self.__tiles)) if self.__tiles[index] in list(map(str, range(9)))]

    # Win condition
    def check_board(self, symbol):
        '''Check if the player won, cause a draw, or doesn't cause either'''
        possible_combination = [
            self.__tiles[:3], self.__tiles[3:6], self.__tiles[6:], 
            self.__tiles[::3],self.__tiles[1::3], self.__tiles[2::3],
            self.__tiles[0::4], self.__tiles[2:8:2]
        ]
        if len(list(filter(lambda x: x==[symbol]*3, possible_combination)))>0:
            return symbol 
        elif not len(list(filter(lambda x: x in list(map(str, range(9))),self.__tiles))):
            return 'DRAW'
        else:
            return False    