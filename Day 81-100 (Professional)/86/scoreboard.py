# Import modules
from turtle import Turtle

# Font
FONT = ("Courier", 14, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        '''Initialize Scoreboard'''
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.score = 0
        self.goto(x=240, y=240)
        self.write(f"Score: {self.score}", font=FONT)

    def update_score(self):
        '''Update Score'''
        self.score+=10
        self.clear()
        self.goto(x=240, y=240)
        self.write(f"Score: {self.score}", font=FONT)

    def final_result(self):
        if self.score == 1900:
            self.goto((0,45))
            self.write(f"You won!", align = "center", font = ("Arial",24,"bold"))    
        else:
            self.goto((0,45))
            self.write(f"Game over!", align = "center", font = ("Arial",24,"bold"))    
        self.goto((0,0))
        self.write(f"Final score {self.score}", align = "center", font = ("Arial",12,"bold"))
        self.goto((0,-35))
        self.write(f"Please wait for a while...", align = "center", font = ("Arial",12,"bold")) 