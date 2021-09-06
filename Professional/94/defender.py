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
        self._lives = 3
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

    def lose_life(self):
        '''Decrement defender's life'''
        self._lives -=1

    def reset_bullets(self):
        '''Reset everything'''
        for bullet in self.bullets:
            bullet.reset()
            bullet.hideturtle()
        self.bullets.clear()

    def successful_shot(self, invaders:list):
        '''Check if defender's fired bullets successfully hit an invader'''
        for bullet in self.bullets:
            for invader in invaders:
                if bullet.distance(invader)<=10 and invader.isvisible():
                    bullet.hideturtle()
                    invader.hideturtle()
                    return True
        return False