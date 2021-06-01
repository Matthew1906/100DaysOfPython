# Import Modules
from turtle import Turtle
from random import choice, randint

COLOR = ['red', 'blue','yellow','green','orange']

class Food(Turtle):
    def __init__(self):
        '''Food Constructor'''
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(choice(COLOR))
        self.speed("fastest")
        x = randint(-275,275)
        y = randint(-275,275)
        self.goto(x=x, y=y)

    def change_location(self):
        '''Change Food Location'''
        self.color(choice(COLOR))
        x = randint(-275,275)
        y = randint(-275,275)
        self.goto(x=x, y=y)