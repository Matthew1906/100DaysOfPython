# DAY 18 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: HIRST SPOT PAINTING SPOT GENERATOR
# THINGS I IMPLEMENTED: TURTLE, COLORGRAM, AND RANDOM MODULE
# DIFFERENT FROM THE COURSE EXPLANATION

from turtle import Turtle, Screen
from random import choice
import colorgram

# EXTRACT COLORS
colors = colorgram.extract('Project/spots.jpg', 100)

# INITIALIZE TURTLE
timmy = Turtle()
canvas = Screen()
canvas.colormode(255)
timmy.shape("circle")
timmy.color(choice(colors).rgb)
timmy.pensize(5)
timmy.speed("fastest")
timmy.penup()
timmy.setposition(-300,250)
# START DRAWING
for i in range(0,501,30):
    # ROW
    timmy.setposition(-300,250-i)
    for j in range(0,580,30):
        # COLUMN
        timmy.pendown()
        timmy.stamp()
        timmy.color(choice(colors).rgb)
        timmy.penup()
        timmy.forward(30)
timmy.color("white")
canvas.exitonclick()