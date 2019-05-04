import pygame
import hoppercore
import gameobject
import gamesettings
import control

class Dude(gameobject.GameObject):
    def __init__(self, name, x, y, genome = None, config= None):
        super(Dude, self).__init__(name, x, y, gamesettings.GRAVITY_ACC)
        self.on_ground = False
        self.standing_on = None
        self.image = pygame.image.load("Assets/dude.png")
        self.rect = self.image.get_rect()
        self.xpos = self.xpos + self.rect.width
        self.ypos = self.ypos - self.rect.height
        self.alive = True
        self.score = 0
        self.is_ai = True
        self.highest_block = 1
        if genome is None:
            self.control = control.KeyboardControl()
            self.is_ai = False
        else:
            self.control = control.AgentControl(genome, config)
            self.is_ai = True



    def playable_update(self, platforms):
        
        #bounce off the walls
        if gamesettings.WALL_BOUNCE == True:
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
                    if p.points > self.highest_block:
                        self.highest_block = p.points


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
            self.score = self.score + 100 * self.highest_block

        #get input
        if self.is_ai:
            control_input = self.control.get_input(sensors = self.get_sensors(platforms))
        else:
            control_input = self.control.get_input()

        if control_input[0]:
            self.move_left()
        if control_input[1]:
            self.move_right()
        if control_input[2]:
            self.jump()



    def jump(self):
        if self.on_ground:
            self.on_ground = False
            self.yvel = self.yvel - gamesettings.JUMP_SPEED
    
    def move_left(self):
        if self.on_ground:
            self.xvel = self.xvel - gamesettings.WALK_ACC
        else:
            self.xvel = self.xvel - gamesettings.WALK_ACC
        
        if self.xvel < -gamesettings.SPEED_LIMIT:
            self.xvel = - gamesettings.SPEED_LIMIT
    
    def move_right(self):
        if self.on_ground:
            self.xvel = self.xvel + gamesettings.WALK_ACC
        else:
            self.xvel = self.xvel + gamesettings.WALK_ACC
        
        if self.xvel > gamesettings.SPEED_LIMIT:
            self.xvel = gamesettings.SPEED_LIMIT
        



    def get_sensors(self,blocks):
        my_rect = self.get_rect_loc()

        current_rect = blocks[-3].get_rect_loc()
        next_rect = blocks[-2].get_rect_loc()
        rect_after_next = blocks[-1].get_rect_loc()
    
        for b in blocks:
            ydist =  b.ypos - self.ypos
            
            #set current and next rect to some default values to avoid passing nones

            if ydist < gamesettings.MAX_BLOCK_Y_DELT and ydist >= 0:
                #this is the closes block underneath
                current_rect = b.get_rect_loc()
            elif ydist <0 and ydist >= - gamesettings.MAX_BLOCK_Y_DELT:
                #this is the next block above
                next_rect = b.get_rect_loc()
            elif ydist < -gamesettings.MAX_BLOCK_Y_DELT and ydist >= -gamesettings.MAX_BLOCK_Y_DELT * 2:
                #this is the block after next
                rect_after_next = b.get_rect_loc()
                
        sensors = [
            #grounded
            int(self.on_ground),
            self.xvel,
            self.yvel,
            current_rect.top - my_rect.bottom,
            #x distance between current block left edge and agent right foot
            current_rect.topleft[0] - (my_rect.bottomright[0]),
            #x distance between current block right edge and agent right foot
            current_rect.topright[0] - (my_rect.bottomleft[0]),
            #y dist between this and next
            next_rect.top - my_rect.bottom,
            next_rect.topleft[0] - (my_rect.bottomright[0]),
            next_rect.topright[0] - (my_rect.bottomleft[0]),
            rect_after_next.top - my_rect.bottom,
            rect_after_next.topleft[0] - (my_rect.bottomright[0]),
            rect_after_next.topright[0] - (my_rect.bottomleft[0])
        ]

        for i in range(len(sensors)):
            sensors[i] =  10000*sensors[i]
        
        return(sensors)
