import pygame
import dude
# define a main function
def main():   
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    BLACK=(0,0,0)
    # create a surface on screen
    screen = pygame.display.set_mode((600,800))
    mydude = dude.Dude() 
    # define a variable to control the main loop
    running = True
    
    
    # main loop
    while running:
        # event handling, gets all event from the event queue
        
        pygame.draw.rect(screen, BLACK, mydude.image.get_rect(left=mydude.xpos, top=mydude.ypos))
        mydude.update()
        screen.blit(mydude.image, (mydude.xpos,mydude.ypos))
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