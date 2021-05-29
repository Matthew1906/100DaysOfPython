# EXERCISE 5 : Spyrograph

from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
canvas = Screen()
canvas.colormode(255)
timmy.shape("turtle")
timmy.color("green","green")

# timmy.pensize(8)
timmy.speed("fastest")

for i in range(37):
    timmy.pencolor(randint(0,255), randint(0,255), randint(0,255))
    timmy.setheading(i*10)
    timmy.circle(100)
    
canvas.exitonclick()
