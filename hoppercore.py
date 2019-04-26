import pygame
import numpy.random as rand
import gamesettings
import gameobject
import dude
import gamerect

def clear_game_object(screen, game_object):
    pygame.draw.rect(screen, gamesettings.BLACK, game_object.get_rect_loc())

def draw_game_object(screen, game_object):
    pygame.draw.rect(screen, game_object.fill_colour, game_object.get_rect_loc())

def blit_game_object(screen, game_object):
    screen.blit(game_object.image, (game_object.xpos, game_object.ypos))   

def end_game():
    print("YOU ARE DEAD")
    pygame.event.post(pygame.event.Event(pygame.QUIT))




def make_block(last_block_x, last_block_y, add_random = True):
    x_loc = last_block_x
    y_loc = last_block_y
    
    if add_random:
        x_loc = x_loc + gamesettings.MAX_BLOCK_X_DELT * rand.uniform(-1,1)
        y_loc = y_loc + gamesettings.MAX_BLOCK_Y_DELT * rand.uniform(-.5,-1)

    if x_loc < 0:
        x_loc = abs(x_loc)
    elif x_loc > gamesettings.SCREEN_DIM[0] - gamesettings.BLOCK_WIDTH:
        x_loc =  gamesettings.SCREEN_DIM[0] - gamesettings.BLOCK_WIDTH - (x_loc % (gamesettings.SCREEN_DIM[0] - gamesettings.BLOCK_WIDTH))

    block = gamerect.GameRect("block", x_loc, y_loc, gamesettings.BLOCK_WIDTH, gamesettings.BLOCK_HEIGHT)
    return block

def generate_start_blocks():
    
    new_block = make_block(gamesettings.START_POS[0] - 10, gamesettings.START_POS[1] + 60, add_random = False)
    y_val = new_block.ypos
    x_val = new_block.xpos
    blocks =[new_block]

     
    while y_val  > 0:
        new_block = make_block(x_val, y_val)
        y_val = new_block.ypos
        x_val = new_block.xpos
        blocks.append(new_block)
    return(blocks)

def intersection(path, surface):
    intersection = None
    #since our surfaces are horizontal, and our player only collides downward our intersection check is simplified    
    #first we will check if our player path is crossing the surface's height
    if surface[0][1] >= path[0][1] and surface[0][1] <= path[1][1]:
        #now we will calculate the x location of the player path when it is at the correct height
        surface_height = surface[0][1]
        v_dist = surface_height - path[0][1]
        path_v_dist = path[1][1] - path[0][1] 
        path_x_dist = path[1][0] - path[0][0]
        intersect_x = path[0][0] + path_x_dist * (v_dist/path_v_dist)
        if intersect_x > min(surface[0][0], surface[1][0]) and intersect_x < max(surface[0][0], surface[1][0]):
            #then we have an intersection
            intersection = (intersect_x, surface_height)       
    return(intersection)
