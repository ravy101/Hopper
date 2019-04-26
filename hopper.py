import pygame
import dude
import gameobject
import gamerect
import gamesettings

def clear_game_object(screen, game_object):
    pygame.draw.rect(screen, gamesettings.BLACK, game_object.get_rect_loc())

def draw_game_object(screen, game_object):
    pygame.draw.rect(screen, game_object.fill_colour, game_object.get_rect_loc())

def blit_game_object(screen, game_object):
    screen.blit(game_object.image, (game_object.xpos, game_object.ypos))   

def end_game():
    print("YOU ARE DEAD")
    pygame.event.post(pygame.event.Event(pygame.QUIT))

#TODO move this somewhere more sensible
def intersection(path, surface):
    intersection = None
    #since our surfaces are horizontal, and our player only collides downward our intersection check is simplified    
    #first we will check if our player path is crossing the surface's height
    print("Checking intersections: ", path )
    print(surface)
    if surface[0][1] >= path[0][1] and surface[0][1] <= path[1][1]:
        #now we will calculate the x location of the player path when it is at the correct height
        surface_height = surface[0][1]
        v_dist = surface_height - path[0][1]
        path_v_dist = path[1][1] - path[0][1] 
        path_x_dist = path[1][0] - path[0][0]
        intersect_x = path[0][0] + path_x_dist * (v_dist/path_v_dist)
        if intersect_x > min(surface[0][0], surface[1][0]) and intersect_x < max(surface[0][0], surface[1][0]):
            #then we have an intersection
            print("INTERSECT")
            intersection = (intersect_x, surface_height)       
    return(intersection)

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
    game_platforms = [gamerect.GameRect("block",gamesettings.START_POS[0] -10, gamesettings.START_POS[1] + 60, gamesettings.BLOCK_WIDTH, gamesettings.BLOCK_HEIGHT)]
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
            draw_game_object(screen, r)
            
        clear_game_object(screen, mydude)
        mydude.playable_update(game_platforms)
        blit_game_object(screen, mydude)
        pygame.display.flip()
        
        
        if not mydude.alive:
            end_game()
 
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mydude.jump()
                elif event.key == pygame.K_LEFT:
                    mydude.move_left()
                elif event.key == pygame.K_RIGHT:
                    mydude.move_right()
                elif event.key == pygame.K_q:
                    end_game()
     
 
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()