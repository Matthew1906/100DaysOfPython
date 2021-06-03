from turtle import Turtle

FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.level = 1
        self.goto(x=-275,y=260)
        self.write(f"Level: {self.level}", font = FONT)
    
    def increment(self):
        self.level+=1
        self.clear()
        self.goto(x=-275,y=260)
        self.write(f"Level: {self.level}", font = FONT)

    def game_over(self):
        self.goto(x=0,y=0)
        self.write(f"Game Over!", align = "center", font = FONT)
        self.goto(x=0,y=-30)
        self.write(f"Please wait for a moment", align = "center", font = FONT)