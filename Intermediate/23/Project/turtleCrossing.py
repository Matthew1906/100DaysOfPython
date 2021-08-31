# DAY 23 CAPSTONE PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: TURTLE CROSSING GAME
# THINGS I IMPLEMENTED: TURTLE, INHERITANCE, TURTLE CROSSING GAME LOGIC, RANDOM
# The Game is different from the course, since i added a main menu and probably different logic in the game

# Import Modules and Classes
import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initialize Screen
screen = Screen()
screen.title("Turtle Crossing")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Driver Code
def turtle_crossing():
    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    screen.onkey(key="Up", fun=player.move)
    
    def clear_all():
        scoreboard.reset()
        player.reset()
        car_manager.delete()
    
    game_is_on = True
    delay = 0.1
    while game_is_on:
        time.sleep(delay)
        screen.update()
        car_manager.move_cars()
        if player.cross_finish():
            scoreboard.increment()
            if delay>=0.03:
                delay*=0.95
        elif car_manager.check_hit(player):
            scoreboard.game_over()
            game_is_on = False
    screen.ontimer(fun=clear_all, t=3000)

# This is similar to what happens in Pong Game and Snake Game
# I literally copy pasted it (It works similarly anyway)

prompt = Turtle()
prompt.hideturtle()
prompt.penup()
prompt.color("white")

# This is the main menu, after the user plays the game, it will redirect back to the main menu
def game():
    prompt.hideturtle()
    prompt.penup()
    prompt.goto((0,45))
    prompt.write(f"Turtle Crossing Game", align = "center", font = ("Arial",24,"bold"))
    prompt.goto((0,0))
    prompt.write(f"Press 'space' to start game", align = "center", font = ("Arial",12,"bold"))
    prompt.goto((0,-35))
    prompt.write(f"Press 'e' to quit game", align = "center", font = ("Arial",12,"bold")) 
    
    def start_game():
        prompt.clear()
        turtle_crossing()
        screen.ontimer(fun=game, t=3000)

    def stop_game():
        prompt.goto(0,-75)
        prompt.write(f"Right click to close window...", align = "center", font = ("Arial",12,"bold"))
        screen.exitonclick()

    screen.onkey(key="space", fun = start_game)
    screen.onkey(key="e", fun = stop_game)  
    screen.mainloop()
game()