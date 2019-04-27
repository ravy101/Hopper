import pygame

class KeyboardControl(object):

    def get_input(self):
        controls = [False, False, False]
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_LEFT]:
            controls[0] = True
        if keys[pygame.K_RIGHT]:
            controls[1] = True
        if keys[pygame.K_SPACE]:
            controls[2] = True

        return(controls)
