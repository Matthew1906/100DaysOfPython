# TURTLE: DRAW GRAPHICS
# TURTLE WITH A PEN ON ITS BACK

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black","green")
# Turtle -> derived from tkinter

canvas = Screen()
canvas.exitonclick()

# import module
# from module import thing(s) -> if u used the thing many times
# import module as alias -> to make it simpler

# generate random colors -> done in exercise 4 using randint and colormode