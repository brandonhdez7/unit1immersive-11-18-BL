import pygame
from pygame.sprite import Sprite

class Hero(Sprite):
    # Classes always contain two parts:
    # 1. the __init__ = runs only once
    # 2. the methods = run whenever you call them
    def __init__(self):
        super(Hero,self).__init__()
        self.x = 100
        self.y = 400
        self.speed = 10
        self.should_move_right = False
        self.should_move_left = False
        self.should_move_up = False
        self.should_move_down = False
        self.rect = pygame.Rect(0,0,32,32)
        self.rect.centerx = self.x
        self.rect.top = self.y 
    def shouldMove(self,direction,start = True):
        if direction == 'right':
            self.should_move_right = start
        if direction == 'left':
            self.should_move_left = start
        if direction == 'up':
            self.should_move_up = start
        if direction == 'down':
            self.should_move_down = start
    def draw_me(self):
        if self.should_move_right:
            if self.x < 448:
                self.x += self.speed
        elif self.should_move_left:
            if self.x > 32:
                self.x -= self.speed
        if self.should_move_up:
            if self.y > 32:
                self.y -= self.speed
        elif self.should_move_down:
            if self.y < 416:
                self.y += self.speed
    def update_me(self):
        self.rect.x = self.x
        self.rect.y = self.y