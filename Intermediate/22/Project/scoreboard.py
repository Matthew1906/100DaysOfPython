from turtle import Turtle

# Scoreboard class to show score and game over message
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1 = 0
        self.player2 = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,180)
        self.write(f"{self.player1} | {self.player2}", align="center", font=['Courier', 40, 'bold'])

    def left_score(self):
        self.clear()
        self.player1+=1
        self.goto(0,180)
        self.write(f"{self.player1} | {self.player2}", align="center", font=['Courier', 40, 'bold'])

    def right_score(self):
        self.clear()
        self.player2+=1
        self.goto(0,180)
        self.write(f"{self.player1} | {self.player2}", align="center", font=['Courier', 40, 'bold'])

    def end_game(self,coor):
        self.goto(0,240)
        if coor>=380:
            self.write(f"Left Player Wins", align="center", font=['Courier', 25, 'bold'])
        elif coor<=-380:
            self.write(f"Right Player Wins", align="center", font=['Courier', 25, 'bold'])
        self.goto(0,140)
        self.write(f"We'll go back to the main menu shortly...", align = "center", font = ("Courier",15,"bold"))
        self.goto(0,110)
        self.write(f"Please wait for a while", align = "center", font = ("Courier",15,"bold"))
    
    def reset_score(self):
        self.player1 = 0
        self.player2 = 0
        self.goto(0,180)
        self.write(f"{self.player1} | {self.player2}", align="center", font=['Courier', 40, 'bold']) 