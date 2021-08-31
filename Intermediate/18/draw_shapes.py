# EXERCISE 3 : DRAW TRIANGLE, SQUARE, PENTAGON, HEXAGON. HEPTAGON,OCTAGON, NONAGON, DECAGON

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black","green")

colors = ['red', 'orange', 'yellow','green','blue', 'pink', 'purple', 'gray']
timmy.penup()
timmy.setposition((0,100))
timmy.pendown()
for i in range(3,11):
    timmy.pencolor(colors[i-3])
    for j in range(i):
        timmy.forward(100)
        timmy.right(360/i)

canvas = Screen()
canvas.exitonclick()