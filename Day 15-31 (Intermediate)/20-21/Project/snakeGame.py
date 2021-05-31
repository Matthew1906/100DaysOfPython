from turtle import Screen
from snake import Snake
import time

canvas = Screen()
canvas.setup(width = 600, height = 600)
canvas.bgcolor((0,0,0))
canvas.title("Snake Game")
canvas.tracer(0)
canvas.listen()

# 1. Create Snake
snake = Snake()

# 2. Move and Control the Snake
running = True
while running:
    time.sleep(0.1)
    canvas.update()
    snake.move()
    canvas.onkey(key = 'Left', fun = snake.left)
    canvas.onkey(key = 'Right', fun = snake.right)
    canvas.onkey(key = 'Up', fun = snake.up)
    canvas.onkey(key = 'Down', fun = snake.down)

# 3. Eat Food
# 4. Scoreboard
# 5. Collision with Wall
# 6. Collision with Tail

canvas.exitonclick()