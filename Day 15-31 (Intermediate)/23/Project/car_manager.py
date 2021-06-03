from turtle import Turtle
from random import choice,randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5

class CarManager():
    def __init__(self):
        self.cars = []
        for i in range(-260,260,STARTING_MOVE_DISTANCE):
            car = Turtle(shape="square")
            car.color(choice(COLORS))
            car.shapesize(stretch_wid=0.75, stretch_len=2)
            car.penup()
            car.goto(x=320,y=i)
            car.setheading(180)
            self.cars.append(car)
    
    def move_cars(self):
        for car in self.cars:
            if car.xcor()<=-320:
                car.goto(x=320,y=car.ycor())
            elif car.xcor()<320:
                car.forward(MOVE_INCREMENT)
            else:
                should_i_move = randint(1,1000)
                if should_i_move%333==0:
                    car.forward(MOVE_INCREMENT)

    def check_hit(self, turtle):
        for car in self.cars:
            if turtle.distance(car)<=20:
                return True
        return False

    def delete(self):
        for car in self.cars:
            car.reset()
        self.cars.clear()