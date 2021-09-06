from turtle import Turtle
from bullet import Bullet
from random import randint

class Invaders():
    def __init__(self):
        '''Initialize invaders'''
        self.invaders = []
        self.bullets = []
        self.direction = 'right'
        for i in range(180, -240, -60):
            for j in range(200, 0, -50):
                invader = Turtle()
                invader.shape('./images/invader.gif')
                invader.penup()
                invader.setheading(270)
                invader.setpos((i,j))
                self.invaders.append(invader)

    def get_possibility(self):
        living_invaders = len(list(filter(lambda x: x.isvisible(), self.invaders)))
        return living_invaders*5

    def move_invaders(self):
        '''Move the invaders left and right, and shoot something'''
        if self.direction =='right' and self.invaders[0].xcor()<=320:
            # move all invaders into the right
            for invader in self.invaders:
                x = invader.xcor()
                invader.setx(x+5)
        elif self.direction == 'right':
            self.direction = 'left'
        if self.direction == 'left' and self.invaders[-1].xcor()>=-320:
            # move all invaders to the left
            for invader in self.invaders:
                x = invader.xcor()
                invader.setx(x-5)
        elif self.direction =='left':
            self.direction = 'right'
        for invader in self.invaders:
            shoot_indicator = randint(1,1000)
            possibility_count = self.get_possibility()
            if shoot_indicator%possibility_count==0 and invader.isvisible():
                enemy_bullet = Bullet(
                    color = 'red',
                    position = (invader.xcor(), invader.ycor()-12), 
                    role = 'enemy',
                    shape = 'circle'
                )
                self.bullets.append(enemy_bullet)
    
    def move_bullets(self):
        '''Move each invader's bullets'''
        for bullet in self.bullets:
            if bullet.ycor()>=400:
                self.bullets.remove(bullet)
        for bullet in self.bullets:
            bullet.move()

    def check_collision(self, defender):
        '''Check if any invader's bullets hit the defender'''
        for bullet in self.bullets:
            if bullet.distance(defender) <= 15 and bullet.isvisible():
                bullet.hideturtle()
                return True
        return False

    def reset(self):
        '''Remove all invaders and bullets'''
        for bullet in self.bullets:
            bullet.reset()
            bullet.hideturtle()
        self.bullets.clear()
        for invader in self.invaders:
            invader.reset()
            invader.hideturtle()
        self.invaders.clear()
