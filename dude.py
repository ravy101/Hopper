import pygame
import hopper

class Dude:
    def __init__(self):
        self.name = "dude"
        self.xpos = 50
        self.ypos = 50
        self.xvel = 2
        self.yvel = 0
        self.xacc = 0
        self.yacc = 0
        self.image = pygame.image.load("dude.png")
        self.gravity = .25
        self.grounded = True

    def update(self):
        self.xpos = self.xpos + self.xvel
        ##TODO move this to a player game object extension
        if self.xpos < 0:
            self.xpos = abs(self.xpos)
            self.xvel = abs(self.xvel)
        elif self.xpos > hopper.SCREEN_DIM[0]:
            self.xpos =  hopper.SCREEN_DIM[0] - (self.xpos -  hopper.SCREEN_DIM[0])
            self.xvel = -abs(self.xvel)
        self.ypos = self.ypos + self.yvel
        self.xvel = self.xvel + self.xacc
        self.yvel = self.yvel + self.yacc + self.gravity

    def jump(self):
        self.yvel = self.yvel - 25
    
    def move_left(self):
        if self.grounded:
            self.xvel = self.xvel - 6
        else:
            self.xacc = self.xvel - 2
    
    def move_right(self):
        if self.grounded:
            self.xvel = self.xvel + 5
        else:
            self.xacc = self.xvel + 2
