import pygame
import dude
import gameobject
import gamerect
import gamesettings
import numpy.random as rand
from hoppercore import *

class HopperGame(object):

    # define a main function
    def __init__(self):   
        # initialize the pygame module
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("ITS HOPPER!")

        # create a surface on screen
        self.screen = pygame.display.set_mode(gamesettings.SCREEN_DIM)
        self.game_platforms = generate_start_blocks()
        
    

    def create_players(self, genomes = None, config = None):
        self.live_dudes = []
        self.dead_dudes = []
        if genomes is not None and config is not None:
            for g in genomes:
                self.live_dudes.append(dude.Dude("Mr Duderstein", gamesettings.START_POS[0], gamesettings.START_POS[1], g, config))
        else:      
            self.live_dudes.append(dude.Dude("Mr Duderstein Player", gamesettings.START_POS[0], gamesettings.START_POS[1]))

        
    def play(self):
        running = True
        # main loop
        while running:
            # event handling, gets all event from the event queue
            self.clock.tick(gamesettings.FPS)
            replace_blocks = 0
            for r in self.game_platforms:
                clear_game_object(self.screen, r)
                r.update()
                if r.out_of_bounds:
                    self.game_platforms.remove(r)
                    replace_blocks = replace_blocks + 1
                    continue
                draw_game_object(self.screen, r)
            
            if replace_blocks > 0:
                new_block = make_block(self.game_platforms[len(self.game_platforms) -1].xpos, self.game_platforms[len(self.game_platforms) -1].ypos, add_random=True)
                self.game_platforms.append(new_block)
                replace_blocks = 0
            
            for mydude in self.live_dudes:
                clear_game_object(self.screen, mydude)
                mydude.playable_update(self.game_platforms)
                blit_game_object(self.screen, mydude)
                if not mydude.alive:
                    self.live_dudes.remove(mydude)
                    self.dead_dudes.append(mydude)


            if len(self.live_dudes) == 0:
                self.results = end_game(self.dead_dudes)
            pygame.display.flip()
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
    