# EXERCISE 2 : DRAW DASHED LINE

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black","green")

timmy.penup()
timmy.setposition((-300,0))
for i in range(50):
    if i%2==0:
        timmy.pendown()
    else:
        timmy.penup()
    timmy.forward(10)
    

canvas = Screen()
canvas.exitonclick()