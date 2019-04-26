import pygame
import gamesettings
#import hopper

class GameObject:
    def __init__(self, name, x, y, gravity):
        self.name = name
        self.xpos = x
        self.ypos = y
        self.xvel = 0
        self.yvel = 0
        self.xacc = 0
        self.yacc = 0
        self.image = pygame.image.load("dude.png")
        self.gravity = gravity
        self.rect = None
        self.out_of_bounds = False

    def update(self):
        self.xpos = self.xpos + self.xvel
        self.ypos = self.ypos + self.yvel
        self.xvel = self.xvel + self.xacc
        self.yvel = self.yvel + self.yacc + self.gravity
        if self.ypos > gamesettings.SCREEN_DIM[1]:
            self.out_of_bounds = True

    def get_rect_loc(self):
        return self.rect.move(self.xpos, self.ypos)