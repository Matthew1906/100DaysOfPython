from turtle import Turtle

class Bullet(Turtle):
    def __init__(self, **kwargs):
        '''Initialize Bullet'''
        super().__init__()
        self.shape(kwargs['shape'])
        self.setheading(90)
        self.shapesize(stretch_len=0.25, stretch_wid=0.25)
        self.color(kwargs['color'])
        self.penup()
        self.setpos(kwargs['position'])
        self.direction = kwargs['role']

    def move(self):
        '''Move the bullet'''
        y = self.ycor()
        if self.direction == 'defender' and y<=400:
            self.sety(y+10)
        elif y>=-400:
            self.sety(y-10)
