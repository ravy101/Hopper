import pygame
import dude
import gameobject
import gamerect
import gamesettings
import numpy.random as rand
from hoppercore import *

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
    mydude = dude.Dude("Mr Duderstein", gamesettings.START_POS[0], gamesettings.START_POS[1], gamesettings.GRAVITY_ACC) 
    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        clock.tick(gamesettings.FPS)
        for r in game_platforms:
            clear_game_object(screen, r)
            r.update()
            if r.out_of_bounds:
                r = 
            draw_game_object(screen, r)
            
        clear_game_object(screen, mydude)
        mydude.playable_update(game_platforms)
        blit_game_object(screen, mydude)
        pygame.display.flip()
        
        
        if not mydude.alive:
            end_game()

        #CONTROLS
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_LEFT]:
            mydude.move_left()
        if keys[pygame.K_RIGHT]:
            mydude.move_right()

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mydude.jump()
                elif event.key == pygame.K_q:
                    end_game()
     
 
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()