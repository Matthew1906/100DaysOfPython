# Import modules
from turtle import Turtle, Screen
from random import randint

colors = ['red','purple','yellow','green','blue', 'black']

def init_turtle(index, y):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(colors[index])
    turtle.penup()
    turtle.goto(x=-230,y=y)
    return turtle

canvas = Screen()
canvas.setup(width = 500, height = 400)
color_choice = canvas.textinput(title = "Make your bet", prompt="Enter a color: ")

turtles = []
for i in range(6):
    turtle = init_turtle(i, 100 -((i+1)*30))
    turtles.append(turtle)
    
running = True
while running:
    for turtle in turtles:
        distance = randint(1,30)
        turtle.forward(distance)
        if turtle.xcor()>=220:
            running = False
            print(f"The {turtle.pencolor().capitalize()} Turtle won the race!")
            if turtle.pencolor() == color_choice.lower():
                print("You won the game!")
            else:
                print("You lost!")
            break

canvas.exitonclick()