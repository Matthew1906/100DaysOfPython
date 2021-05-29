# EXERCISE 1 : DRAW SQUARE

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black","green")

for _ in range(4):
    timmy.right(90)
    timmy.forward(100)

canvas = Screen()
canvas.exitonclick()