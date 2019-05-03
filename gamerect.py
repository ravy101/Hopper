import pygame
#import hopper
import gameobject
import gamesettings

# 
class GameRect(gameobject.GameObject):
    def __init__(self, name, x, y, width, height, points):
        super(GameRect, self).__init__(name, x, y, 0)
        self.fill_colour = gamesettings.WHITE
        self.yvel = gamesettings.SCROLL_SPEED
        self.points = points
        if self.points >= gamesettings.STAGE_ONE and self.points < gamesettings.STAGE_TWO :
            self.yvel = gamesettings.SCROLL_SPEED + gamesettings.SCROLL_INCREMENT
            self.fill_colour = gamesettings.ORANGE
            width = width * .8
        elif self.points >= gamesettings.STAGE_TWO :
            self.yvel = gamesettings.SCROLL_SPEED + 2 * gamesettings.SCROLL_INCREMENT
            self.fill_colour = gamesettings.RED
            width = width * .6

        self.rect = pygame.Rect(0,0,width,height)
        
        
        

    def get_surface_line(self):
        r = self.get_rect_loc()
        return r.topleft, r.topright
