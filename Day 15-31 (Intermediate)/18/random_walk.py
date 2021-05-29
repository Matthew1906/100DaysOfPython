# EXERCISE 4 : Random Walk

from turtle import Turtle, Screen
from random import choice, randint

timmy = Turtle()
canvas = Screen()
canvas.colormode(255)
timmy.shape("turtle")
timmy.color("green","green")

# colors = ['red', 'orange', 'yellow','green','blue', 'pink', 'purple', 'gray']
direction = [0,90,180,270]
timmy.pensize(8)
timmy.speed("fastest")

for i in range(100):
    timmy.pencolor(randint(0,255), randint(0,255), randint(0,255))
    timmy.right(choice(direction))
    timmy.forward(20)
    
canvas.exitonclick()
