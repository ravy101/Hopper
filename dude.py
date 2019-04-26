import pygame
import hoppercore
import gameobject
import gamesettings


class Dude(gameobject.GameObject):
    def __init__(self, name, x, y, gravity):
        super(Dude, self).__init__(name, x, y, gravity)
        self.on_ground = False
        self.standing_on = None
        self.image = pygame.image.load("dude.png")
        self.rect = self.image.get_rect()
        self.alive = True



    def playable_update(self, platforms):
        
        #bounce off the walls
        if self.xpos < 0:
            self.xpos = abs(self.xpos)
            self.xvel = abs(self.xvel)
        elif self.xpos > gamesettings.SCREEN_DIM[0]:
            self.xpos =  gamesettings.SCREEN_DIM[0] - (self.xpos -  gamesettings.SCREEN_DIM[0])
            self.xvel = -abs(self.xvel)

        if self.yvel > 0:
            my_rect = self.get_rect_loc()
            left_side_line = (my_rect.bottomleft, (my_rect.bottomleft[0] + self.xvel, my_rect.bottomleft[1] + self.yvel))
            right_side_line = (my_rect.bottomright, (my_rect.bottomright[0] + self.xvel, my_rect.bottomright[1] + self.yvel))
            #my_rect.bottomright
            self.on_ground = False
            for p in platforms:
                platform_intersection = hoppercore.intersection(left_side_line, p.get_surface_line())
                    
                if platform_intersection is not None:
                    self.xpos = platform_intersection[0]
                else:
                    platform_intersection = hoppercore.intersection(right_side_line, p.get_surface_line())
                    if platform_intersection is not None:
                        self.xpos = platform_intersection[0] - self.rect.width

                    
                if platform_intersection is not None:
                    self.ypos = platform_intersection[1] - self.rect.height
                    self.yvel = gamesettings.SCROLL_SPEED
                    self.on_ground = True
                    self.standing_on = p


        if self.on_ground == False:
            self.ypos = self.ypos + self.yvel
        else:
            #slow down if walking
            if self.xvel > gamesettings.WALK_SLOW:
                self.xvel = self.xvel - gamesettings.WALK_SLOW
            elif self.xvel < - gamesettings.WALK_SLOW:
                self.xvel = self.xvel + gamesettings.WALK_SLOW
            else:
                self.xvel = 0
        
        self.xpos = self.xpos + self.xvel
        self.xvel = self.xvel + self.xacc
        self.yvel = self.yvel + self.yacc + self.gravity
        

            

        #check if out of bounds
        if self.ypos > gamesettings.SCREEN_DIM[1]:
            self.alive = False 

    def jump(self):
        if self.on_ground:
            self.on_ground = False
            self.standing_on = None
            self.yvel = self.yvel - gamesettings.JUMP_SPEED
    
    def move_left(self):
        if self.on_ground:
            self.xvel = self.xvel - gamesettings.WALK_ACC
        else:
            self.xvel = self.xvel - gamesettings.WALK_ACC/3
    
    def move_right(self):
        if self.on_ground:
            self.xvel = self.xvel + gamesettings.WALK_ACC
        else:
            self.xvel = self.xvel + gamesettings.WALK_ACC/3


