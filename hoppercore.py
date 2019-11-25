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

# End the game and save scores
def end_game(dudes):
    print("YOU ARE DEAD")
    pygame.event.post(pygame.event.Event(pygame.QUIT))
    results = []
    for d in dudes:
        results.append((d.get_score(), d.control.genome))

    return(results)

# Create a block that is close to a given, previous block
def make_block(last_block = None):
    if last_block is not None: 
        # Position and score depends on the previous block
        x_loc = last_block.xpos + gamesettings.MAX_BLOCK_X_DELT * rand.uniform(.3,1) * rand.choice([-1,1], 1)
        y_loc = last_block.ypos + gamesettings.MAX_BLOCK_Y_DELT * rand.uniform(-.7,-.7)
        points = last_block.points + 1
    else:
        # This is the first block
        x_loc = gamesettings.START_POS[0]
        y_loc = gamesettings.START_POS[1]
        points = 0

    # Keep the blocks inside the screen
    if x_loc < 0:
        x_loc = abs(x_loc)
    elif x_loc > gamesettings.SCREEN_DIM[0] - gamesettings.BLOCK_WIDTH:
        x_loc =  gamesettings.SCREEN_DIM[0] - gamesettings.BLOCK_WIDTH - (x_loc % (gamesettings.SCREEN_DIM[0] - gamesettings.BLOCK_WIDTH))

    block = gamerect.GameRect("block", x_loc, y_loc, gamesettings.BLOCK_WIDTH, gamesettings.BLOCK_HEIGHT, points)
    return block

# Generate all the starting blocks
def generate_start_blocks():
    new_block = make_block()
    y_val = new_block.ypos
    blocks =[new_block]
    #rand.seed(10)
   
    while y_val  > -300:
        new_block = make_block(new_block)
        y_val = new_block.ypos
        blocks.append(new_block)
    return(blocks)

# Detects the intersection between a line and a horizontal surface and returns the points of intersection
def intersection(path, surface):
    intersection = None
    # Since our surfaces are horizontal, and our player only collides downward our intersection check is simplified    
    # First we will check if our player path is crossing the surface's height
    if surface[0][1] >= path[0][1] and surface[0][1] <= path[1][1]:
        # Now we will calculate the x location of the player path when it is at the correct height
        surface_height = surface[0][1]
        v_dist = surface_height - path[0][1]
        path_v_dist = path[1][1] - path[0][1] 
        path_x_dist = path[1][0] - path[0][0]
        intersect_x = path[0][0] + path_x_dist * (v_dist/path_v_dist)
        if intersect_x >= min(surface[0][0], surface[1][0]) and intersect_x <= max(surface[0][0], surface[1][0]):
            # Then we have an intersection
            intersection = (intersect_x, surface_height)       
    return(intersection)
