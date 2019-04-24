import pygame

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

    def update(self):
        self.xpos = self.xpos + self.xvel
        self.ypos = self.ypos + self.yvel
        self.xvel = self.xvel + self.xacc
        self.yvel = self.yvel + self.yacc