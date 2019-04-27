import pygame
import dude
import gameobject
import gamerect
import gamesettings
import numpy.random as rand
from hoppercore import *

def create_players(n = 10):
    dudes = []
    for i in range(n):
        dudes.append(dude.Dude("Mr Duderstein {}".format(i), gamesettings.START_POS[0], gamesettings.START_POS[1]))
    return(dudes)

# define a main function
def main():   
    # initialize the pygame module
    pygame.init()
    clock = pygame.time.Clock()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("ITS HOPPER!")

    # create a surface on screen
    screen = pygame.display.set_mode(gamesettings.SCREEN_DIM)
    game_platforms = generate_start_blocks()
    live_dudes = create_players(5)
    dead_dudes = []
    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        clock.tick(gamesettings.FPS)
        replace_blocks = 0
        for r in game_platforms:
            clear_game_object(screen, r)
            r.update()
            if r.out_of_bounds:
                game_platforms.remove(r)
                replace_blocks = replace_blocks + 1
                continue
            draw_game_object(screen, r)
        
        if replace_blocks > 0:
            new_block = make_block(game_platforms[len(game_platforms) -1].xpos, game_platforms[len(game_platforms) -1].ypos, add_random=True)
            game_platforms.append(new_block)
            replace_blocks = 0
        
        for mydude in live_dudes:
            clear_game_object(screen, mydude)
            mydude.playable_update(game_platforms)
            blit_game_object(screen, mydude)
            if not mydude.alive:
                live_dudes.remove(mydude)
                dead_dudes.append(mydude)


        if len(live_dudes) == 0:
            end_game(dead_dudes)
        pygame.display.flip()
        
        
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

     
 
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()