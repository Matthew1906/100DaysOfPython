# Import module
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        '''Initialize Ball'''
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.turtlesize(stretch_len=0.75, stretch_wid=0.75)
        self.penup()
        self.setpos((0,-220))
        self.setheading(90)

    def move(self):
        '''Move the ball'''
        self.forward(15)

    def bounce(self):
        '''Bounce the ball -> changing the direction of the ball'''
        self.right(135)