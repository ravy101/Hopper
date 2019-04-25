import pygame
import hopper
import gameobject

class Dude(gameobject.GameObject):
    def __init__(self, name, x, y, gravity):
        super(Dude, self).__init__(name, x, y, gravity)
        self.grounded = True
        self.image = pygame.image.load("dude.png")


    def playable_update(self):
        if self.xpos < 0:
            self.xpos = abs(self.xpos)
            self.xvel = abs(self.xvel)
        elif self.xpos > hopper.SCREEN_DIM[0]:
            self.xpos =  hopper.SCREEN_DIM[0] - (self.xpos -  hopper.SCREEN_DIM[0])
            self.xvel = -abs(self.xvel)

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
