from turtle import Turtle
from bullet import Bullet

class Defender(Turtle):
    def __init__(self):
        '''Initialize defender'''
        super().__init__()
        self.shape('./images/defender.gif')
        self.penup()
        self.setpos((0,-180))
        self.setheading(90)
        self.lives = 3
        self.bullets = []

    def left(self):
        '''Move the defender to the left'''
        x = self.xcor()
        if x>=-320:
            self.setx(x-20)

    def right(self):
        '''Move the defender to the right'''
        x = self.xcor()
        if x<=320:
            self.setx(x+20)

    def shoot(self):
        '''Create a bullet'''
        bullet = Bullet(
            color = 'cyan',
            position = (self.xcor(), self.ycor()+12), 
            role = 'defender',
            shape = 'circle'
        )
        self.bullets.append(bullet)

    def move_bullets(self):
        '''Move bullets'''
        for bullet in self.bullets:
            if bullet.ycor()>=400:
                self.bullets.remove(bullet)
        for bullet in self.bullets:
            bullet.move()

    def reset(self):
        '''Reset everything'''
        for bullet in self.bullets:
            bullet.reset()
        self.bullets.clear()
        self.reset()