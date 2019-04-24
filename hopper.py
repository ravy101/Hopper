import pygame
import dude

#GAME CONSTANTS
SCREEN_DIM = (600,800)
BLACK=(0,0,0)
FPS = 60

def clear_game_object(screen, game_object):
    pygame.draw.rect(screen, BLACK, game_object.image.get_rect().move(game_object.xpos, game_object.ypos))

def blit_game_object(screen, game_object):
    screen.blit(game_object.image, (game_object.xpos, game_object.ypos))   

# define a main function
def main():   
    # initialize the pygame module
    pygame.init()
    clock = pygame.time.Clock()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # create a surface on screen
    screen = pygame.display.set_mode(SCREEN_DIM)
    mydude = dude.Dude() 
    # define a variable to control the main loop
    running = True
    
    
    # main loop
    while running:
        # event handling, gets all event from the event queue
        clock.tick(FPS)
        clear_game_object(screen, mydude)
        mydude.update()
        blit_game_object(screen, mydude)
        pygame.display.flip()
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
     
 
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()