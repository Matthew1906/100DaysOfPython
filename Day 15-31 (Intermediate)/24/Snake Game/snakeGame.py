# This is similar with day 20-21 Project
# Added Highscore

# Import Modules and Classes
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Initialize the Canvas
canvas = Screen()
canvas.setup(width = 600, height = 600)
canvas.bgcolor((0,0,0))
canvas.title("Snake Game")
canvas.tracer(0)
canvas.listen()

# Create Snake and Set Movement Control
snake = Snake()
canvas.onkey(key = 'Left', fun = snake.left)
canvas.onkey(key = 'Right', fun = snake.right)
canvas.onkey(key = 'Up', fun = snake.up)
canvas.onkey(key = 'Down', fun = snake.down)

# Initialize Food, Scoreboard, Delay, and Start Game
food = Food()
scoreboard = Scoreboard()
running = True
delay = 0.1

# Check for Collision
def hit_wall():
    '''Check if hit wall'''
    if snake.body[0].xcor()>=290 or snake.body[0].xcor()<=-290 or snake.body[0].ycor()>=290 or snake.body[0].ycor()<=-290:
        return True
    return False

def hit_body():
    '''Check if hit snake body'''
    for parts in snake.body[1:]:
        if snake.body[0].distance(parts)<10:
            return True
    return False

# Start Game
while running:
    time.sleep(delay)
    canvas.update()
    snake.move()
    # Eat Food, Update Score, Speed up the game, and Extend Snake Length
    if snake.body[0].distance(food)<=15:
        snake.extend()
        scoreboard.update()
        food.change_location()
        delay-= delay*0.01
    # collision with wall or body
    if hit_wall() or hit_body():
        scoreboard.reset()
        snake.reset()
        # food.reset()

canvas.exitonclick()
