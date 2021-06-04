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
        score_file = open("Snake Game/score.txt")
        score_str = score_file.read()
        if score_str=="":
            self.highscore = 0
        else:   
            self.highscore = int(score_str)
        self.write(f"Score: {self.score} High Score:{self.highscore}", align = "center", font = ("Arial",14,"bold"))
    
    def update(self):
        '''Update Scoreboard'''
        self.clear()
        self.score+=10
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Snake Game/score.txt","w") as score_file:
                score_file.write(str(self.highscore))
        self.write(f"Score: {self.score} High Score: {self.highscore}", align = "center", font = ("Arial",14,"bold"))

    def reset(self):
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align = "center", font = ("Arial",14,"bold"))