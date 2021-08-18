# Day 86 of 100 Days of Python
# Project name: Breakout Game
# Things I implemented: Breakout game logic, OOP, Turtle

# TODO:
# - Main screen
# - Paddle = move left and right
# - Ball = change direction
# - Blocks = positioning, and hide itself when hit (cause the ball to change direction)
# - Scoreboard = Keep track of score

# Import modules
from turtle import Screen, Turtle
from paddle import Paddle
from time import sleep
from ball import Ball
from blocks import BlockManager
from scoreboard import ScoreBoard

# Constants
FONT = ("Courier", 14, "normal")

# Config Screen
main_screen = Screen()
main_screen.title("Breakout Game")
main_screen.bgcolor(0,0,0)
main_screen.setup(width=800, height=550, startx= 250, starty=10)
main_screen.tracer(0)
main_screen.listen()

# Menu indicator
is_game = False

# Menu drawing
menu = Turtle()
menu.hideturtle()
menu.penup()
menu.color('white')

def draw_menu():
    menu.goto((0,45))
    menu.write(f"Breakout Game", align = "center", font = ("Arial",24,"bold"))
    menu.goto((0,0))
    menu.write(f"Press 'space' to start game", align = "center", font = ("Arial",12,"bold"))
    menu.goto((0,-35))
    menu.write(f"Press 'e' to quit game", align = "center", font = ("Arial",12,"bold")) 

def breakout_game():
    # Make sure that the game doesn't run multiple times
    menu.clear()
    global is_game
    if is_game:
        return
    is_game=True

    # Config game indicators
    running = True
    delay = 0.05

    # Objects
    paddle = Paddle()
    ball = Ball()
    block_manager = BlockManager()
    scoreboard = ScoreBoard()

    # Helper functions
    def clear_all():
        ball.reset()
        paddle.reset()
        block_manager.reset()
        scoreboard.clear()

    def back_to_menu():
        scoreboard.reset()
        draw_menu()

    # Config listener
    main_screen.onkeypress(key='Left', fun=paddle.left)
    main_screen.onkeypress(key='Right', fun=paddle.right)

    # start game
    while running:
        # Constant update of the main screen
        main_screen.update() 
        # Slight delay to prevent glitch
        sleep(delay)
        # Ball will always move, It'll just bounce according to collision
        ball.move()
        # Handling collision with wall
        if ball.xcor()<=-375 or ball.xcor()>=375 or ball.ycor()>=245:
            ball.bounce()
        # Handling collision with paddle
        elif paddle.should_bounce(ball):
            ball.bounce()
        # Handling collision with blocks
        elif block_manager.hit_block(ball):
            ball.bounce()
            scoreboard.update_score()
        # Game over condition
        if ball.ycor()<=-240 or scoreboard.score==1900:
            running=False
    clear_all()
    scoreboard.final_result()
    main_screen.ontimer(fun=back_to_menu, t=3000)
    is_game=False

draw_menu()
main_screen.onkey(key='space', fun=breakout_game)
main_screen.onkey(key='e', fun=main_screen.bye)
main_screen.mainloop()