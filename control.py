import pygame
import neat

class KeyboardControl(object):

    def get_input(self, sensors = None):
        self.genome = "PLAYER"
        controls = [False, False, False]
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_LEFT]:
            controls[0] = True
        if keys[pygame.K_RIGHT]:
            controls[1] = True
        if keys[pygame.K_SPACE]:
            controls[2] = True

        return(controls)

class AgentControl(object):
    def __init__(self, genome, config):
        self.genome = genome
        self.neural_network = neat.nn.FeedForwardNetwork.create(genome, config)

    def get_input(self, sensors = None):
        controls = [False, False, False]
        output = self.neural_network.activate(sensors)
        if output[0] > 0.4:
            controls[0] = True
        if output[1] > 0.4:
            controls[1] = True
        if output[2] > 0.4:
            controls[2] = True

        return(controls)  
