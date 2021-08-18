# Import module
from turtle import Turtle
from ball import Ball

class Paddle(Turtle):
    def __init__(self):
        '''Initialize Paddle'''
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len = 5, stretch_wid = 0.75)
        self.penup()
        self.setpos((0, -235))

    def left(self):
        '''Move the paddle to the left'''
        x = self.xcor()
        if x>=-320:
            self.setx(x-20)

    def right(self):
        '''Move the paddle to the right'''
        x = self.xcor()
        if x<=320:
            self.setx(x+20)
    
    def should_bounce(self, ball:Ball):
        paddle_x = self.xcor()
        paddle_y = self.ycor()
        if abs(paddle_y-ball.ycor())<30 and abs(paddle_x-ball.xcor())<=50:
            return True
        return False