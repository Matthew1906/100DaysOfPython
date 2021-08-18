# Import modules
from turtle import Turtle
from random import shuffle

# Set colors
COLORS = ['red', 'blue', 'yellow', 'green', 'purple', 
'orange', 'lime', 'hot pink', 'cyan', 'plum']

class BlockManager():
    def __init__(self):
        '''Initialize the blocks'''
        self.blocks = []
        # Reorder colors
        shuffle(COLORS)
        # Block rows
        for i in range(0, 200, 20):
            # Block columns
            for j in range(-380, 380, 40):
                block = Turtle(shape='square')
                block.penup()
                block.turtlesize(stretch_len=1.5,stretch_wid=0.75)
                block.color(COLORS[i//20])
                block.setpos(j,i)
                self.blocks.append(block)

    def hit_block(self, ball):
        '''Remove any blocks that hits the ball'''
        for block in self.blocks:
            if block.isvisible() and block.distance(ball)<30:
                block.hideturtle()
                return True
        return False

    def reset(self):
        '''Reset all contents of the blocks'''
        for block in self.blocks:
            block.reset()
        self.blocks.clear()
