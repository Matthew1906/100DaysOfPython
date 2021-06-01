# Import Module
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        '''Scoreboard Constructor'''
        super().__init__()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(x=0, y=275)
        self.pendown()
        self.hideturtle()
        self.score = 0
        self.write(f"Score: {self.score}", align = "center", font = ("Arial",14,"bold"))
    
    def update(self):
        '''Update Scoreboard'''
        self.clear()
        self.score+=10
        self.write(f"Score: {self.score}", align = "center", font = ("Arial",14,"bold"))

    def game_over(self):
        '''Game Over Screen'''
        self.clear()
        self.goto(x=0, y=10)
        self.write(f"Game Over!", align = "center", font = ("Arial",14,"normal"))
        # Display Final Score
        self.goto(x=0, y=-15)
        self.write(f"Final Score: {self.score}", align = "center", font = ("Arial",14,"normal"))
        # Tells the user to wait and not to press anything
        self.goto(x=0, y=-45)
        self.write(f"We'll go back to the main menu shortly...", align = "center", font = ("Arial",14,"normal"))
        self.goto(x=0, y=-70)
        self.write(f"Please wait for a while", align = "center", font = ("Arial",14,"normal"))