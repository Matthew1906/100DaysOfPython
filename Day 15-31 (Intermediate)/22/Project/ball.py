from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.turtlesize(stretch_len = 0.8, stretch_wid = 0.8)
        self.penup()
        self.setheading(0)     

    def move(self):
        self.forward(15)

    def bounce(self):
        self.right(135)

    def reset_position(self):
        self.penup()
        self.goto((0,0))
        self.setheading(0)


    