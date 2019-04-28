import pygame
import dude
import gameobject
import gamerect
import gamesettings
from hoppercore import *

class HopperGame(object):

    # define a main function
    def __init__(self):   
        # initialize the pygame module
        pygame.init()
        self.human_player = False
        self.results = []
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
        scroll_speed_boost = 0
        # main loop
        while running:
            # event handling, gets all event from the event queue
            if self.human_player:
                self.clock.tick(gamesettings.FPS)
            else:
                self.clock.tick(gamesettings.AI_FPS)
            replace_blocks = 0
            for r in self.game_platforms:              
                clear_game_object(self.screen, r)
                r.ypos = r.ypos + scroll_speed_boost
                r.update()
                if r.out_of_bounds:
                    self.game_platforms.remove(r)
                    replace_blocks = replace_blocks + 1
                    continue
                draw_game_object(self.screen, r)
            
            if replace_blocks > 0:
                top_block = self.game_platforms[len(self.game_platforms) -1]
                new_block = make_block(top_block.xpos, top_block.ypos, top_block.points + 1, add_random=True)
                self.game_platforms.append(new_block)
                replace_blocks = 0

            highest_dude = gamesettings.SCREEN_DIM[1]
            for mydude in self.live_dudes:
                clear_game_object(self.screen, mydude)
                mydude.ypos = mydude.ypos + scroll_speed_boost
                mydude.playable_update(self.game_platforms)
                blit_game_object(self.screen, mydude)

                if mydude.ypos < highest_dude:
                    highest_dude = mydude.ypos

                if not mydude.alive:
                    self.live_dudes.remove(mydude)
                    self.dead_dudes.append(mydude)

            #if there is a dude in the top 3rd of the screen
            if highest_dude < gamesettings.SCREEN_DIM[1] / 3:
                scroll_speed_boost = gamesettings.SCROLL_SPEED_BOOST
            else:
                scroll_speed_boost = 0

            if len(self.live_dudes) == 0:
                self.results = end_game(self.dead_dudes)
            pygame.display.flip()
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
if __name__ == "__main__":
    game = HopperGame()
    game.human_player = True
    game.create_players()
    game.play()   