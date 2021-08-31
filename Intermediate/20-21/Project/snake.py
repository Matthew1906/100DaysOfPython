# Import Modules
from turtle import Turtle

# Directions
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270
class Snake:
    def __init__(self):
        '''Snake Constructor'''
        self.body = []
        for pos in [(0,0),(-20,0),(-40,0)]:
            self.add_segment(pos)        

    def add_segment(self, pos):
        '''Add a new segment'''
        parts = Turtle()
        parts.shape("square")
        parts.color("white")
        parts.penup()
        parts.goto(pos)
        self.body.append(parts)
    
    def extend(self):
        '''Extend the snake's body'''
        self.add_segment(self.body[-1].position())
        
    def delete(self):
        '''Remove all segments'''
        for parts in self.body:
            parts.reset()
    
    def right(self):
        '''Change direction to Right/East'''
        if self.body[0].heading()!=LEFT:
            self.body[0].setheading(RIGHT)

    def left(self):
        '''Change direction to Left/West'''
        if self.body[0].heading()!=RIGHT:
            self.body[0].setheading(LEFT)

    def up(self):
        '''Change direction to Up/North'''
        if self.body[0].heading()!=DOWN:
            self.body[0].setheading(UP)

    def down(self):
        '''Change direction to Down/South'''
        if self.body[0].heading()!=UP:
            self.body[0].setheading(DOWN)
        
    def move(self):
        '''Move the Snake'''
        for i in range(len(self.body)-1, 0, -1):
            x = self.body[i-1].xcor()
            y = self.body[i-1].ycor()
            self.body[i].goto(x,y)
        self.body[0].forward(20)