from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len = 1, stretch_wid = 5)
        self.penup()
        self.setpos((x,0))
    
    def up(self):
        x = self.xcor()
        y = self.ycor()
        if y<=225:
            self.setpos((x,y+30))
    
    def down(self):
        x = self.xcor()
        y = self.ycor()
        if y>=-205:
            self.setpos((x,y-30))
    