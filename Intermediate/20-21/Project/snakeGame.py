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

def snake_game():
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
        
    def clear_all():
        scoreboard.clear()
        food.reset()
        snake.delete()

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
            scoreboard.game_over()
            running = False
            
    canvas.ontimer(fun=clear_all, t=3000)

prompt = Turtle()
prompt.hideturtle()
prompt.penup()
prompt.color("white")

# This is the main menu, after the user plays the game, it will redirect back to the main menu
def game():
    prompt.goto((0,45))
    prompt.write(f"Snake Game", align = "center", font = ("Arial",24,"bold"))
    prompt.goto((0,0))
    prompt.write(f"Press 'space' to start game", align = "center", font = ("Arial",12,"bold"))
    prompt.goto((0,-35))
    prompt.write(f"Press 'e' to quit game", align = "center", font = ("Arial",12,"bold")) 
    
    def start_game():
        prompt.clear()
        snake_game()
        canvas.ontimer(fun=game, t=3000)

    def stop_game():
        prompt.goto(0,-75)
        prompt.write(f"Right click to close window...", align = "center", font = ("Arial",12,"bold"))
        canvas.exitonclick()

    canvas.onkey(key="space", fun = start_game)
    canvas.onkey(key="e", fun = stop_game)  
    canvas.mainloop()

game()