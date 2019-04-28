import pygame
#import hopper
import gameobject
import gamesettings

class GameRect(gameobject.GameObject):
    def __init__(self, name, x, y, width, height, points):
        super(GameRect, self).__init__(name, x, y, 0)
        self.rect = pygame.Rect(0,0,width,height)
        self.fill_colour = gamesettings.WHITE
        self.yvel = gamesettings.SCROLL_SPEED
        self.points = points

    def get_surface_line(self):
        r = self.get_rect_loc()
        return r.topleft, r.topright
