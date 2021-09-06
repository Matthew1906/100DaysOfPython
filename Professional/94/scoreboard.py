from turtle import Turtle

FONT = ("Courier", 14, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        '''Initialize Scoreboard'''
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.lives = 3
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        '''Update Scoreboard'''
        self.clear()
        self.goto(x=250,y=225)
        self.write(f'Score: {self.score}', font=FONT)
        self.goto(x=-350, y=-225)
        self.write(f'Lives: {self.lives}', font=FONT)

    def update_score(self):
        '''Update Score'''
        self.score+=20
        self.update_scoreboard()

    def update_lives(self):
        '''Reduce defender's lives'''
        self.lives-=1
        self.update_scoreboard()

    def final_result(self):
        '''Show Final Result'''
        if self.lives>0:
            self.goto((0,45))
            self.write(f"You win!", align = "center", font = ("Arial",24,"bold"))    
        else:
            self.goto((0,45))
            self.write(f"Game over!", align = "center", font = ("Arial",24,"bold"))    
        self.goto((0,0))
        self.write(f"Final score: {self.score}", align = "center", font = ("Arial",12,"bold"))
        self.goto((0,-35))
        self.write(f"Please wait for a while...", align = "center", font = ("Arial",12,"bold")) 

