# Import Modules and Classes
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time 

# Initialize Canvas
main_screen = Screen()
main_screen.setup(width=800, height=600)
main_screen.title("Pong Game")
main_screen.bgcolor((0,0,0))
main_screen.listen()
main_screen.tracer(0)

# The Pong Game Driver Program 
def pong_game():
    player_right = Paddle(350) # Right Paddle (using Arrow Up and Arrow Down)
    player_left = Paddle(-350) # Left Paddle (using W S)
    ball = Ball()
    scoreboard = Scoreboard()

    main_screen.onkey(key="Up", fun=player_right.up)
    main_screen.onkey(key="Down", fun=player_right.down)
    main_screen.onkey(key="w", fun=player_left.up)
    main_screen.onkey(key="s", fun=player_left.down)

    def clear_all():
        scoreboard.reset()
        ball.reset()
        player_left.reset()
        player_right.reset()

    running = True
    delay = 0.05
    while running:
        main_screen.update()
        time.sleep(delay)
        ball.move()
        if player_right.distance(ball)<=50:
            scoreboard.right_score()
            ball.bounce()
            if delay<=0.01:
                delay = delay*0.95
        elif player_left.distance(ball)<=50:
            scoreboard.left_score()
            ball.bounce()
            if delay<=0.01:
                delay = delay*0.95
        elif ball.ycor()<=-300 or ball.ycor()>=300:
            ball.bounce()
        elif ball.xcor()<=-380 or ball.xcor()>=380:
            scoreboard.end_game(ball.xcor())
            running = False
    main_screen.ontimer(fun=clear_all, t=3000)

prompt = Turtle()
prompt.hideturtle()
prompt.penup()
prompt.color("white")

# This is the main menu, after the user plays the game, it will redirect back to the main menu
def game():
    prompt.goto((0,45))
    prompt.write(f"Pong Game", align = "center", font = ("Arial",24,"bold"))
    prompt.goto((0,0))
    prompt.write(f"Press 'space' to start game", align = "center", font = ("Arial",12,"bold"))
    prompt.goto((0,-35))
    prompt.write(f"Press 'e' to quit game", align = "center", font = ("Arial",12,"bold")) 
    
    def start_game():
        prompt.clear()
        pong_game()
        main_screen.ontimer(fun=game, t=3000)

    def stop_game():
        prompt.goto(0,-75)
        prompt.write(f"Right click to close window...", align = "center", font = ("Arial",12,"bold"))
        main_screen.exitonclick()

    main_screen.onkey(key="space", fun = start_game)
    main_screen.onkey(key="e", fun = stop_game)  
    main_screen.mainloop()

game()