# Event Listeners => keypress, click, etc.

from turtle import Turtle, Screen

timmy = Turtle()
canvas = Screen()
# adding event listener
canvas.listen()

def move_forward():
    timmy.forward(100)
# event listener
canvas.onkey(key = "space", fun=move_forward())

tommy = Turtle()
# we can create different objects, objects have different states


canvas.exitonclick()