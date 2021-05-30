# DAY 19 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: ETCH A SKETCH
# THINGS I IMPLEMENTED: TURTLE, EVENT LISTENERS

from turtle import Turtle, Screen

timmy = Turtle()
canvas = Screen()
canvas.listen()

# move functions
def move_forward():
    '''Move Forward'''
    timmy.forward(10)

def move_backward():
    '''Move Backward'''
    timmy.backward(10)

def turn_right():
    '''Turn Right'''
    timmy.right(10)

def turn_left():
    '''Turn Left'''
    timmy.left(10)

def clear():
    '''Clear Canvas, and Reset to New Screen'''
    canvas.reset()

# i'll use keypress because it fits the goal of the application
canvas.onkeypress(key = "w", fun=move_forward)
canvas.onkeypress(key = "s", fun=move_backward)
canvas.onkeypress(key = "a", fun=turn_left)
canvas.onkeypress(key = "d", fun=turn_right)
canvas.onkeypress(key = "c", fun=clear)

# exit on click function
canvas.exitonclick()