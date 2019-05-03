import pygame
import dude
import gameobject
import gamerect
import gamesettings
from hoppercore import *

class HopperGame(object):


    def __init__(self):   
        # initialize pygame
        pygame.init()
        self.human_player = False
        self.results = []
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("ITS HOPPER!")

        # create a playing surface and start blocks
        self.screen = pygame.display.set_mode(gamesettings.SCREEN_DIM)
        self.game_platforms = generate_start_blocks()
        
    

    def create_players(self, genomes = None, config = None):
        self.live_dudes = []
        self.dead_dudes = []
        # Create AI players if we are passed genomes, otherwise alow manual play
        if genomes is not None and config is not None:
            for g in genomes:
                self.live_dudes.append(dude.Dude("Duder AI", gamesettings.START_POS[0], gamesettings.START_POS[1], g, config))
        else:      
            self.live_dudes.append(dude.Dude("Duder Player", gamesettings.START_POS[0], gamesettings.START_POS[1]))

        
    def play(self):
        running = True
        scroll_speed_boost = 0
        # ************************* MAIN LOOP *******************************
        while running:
            # AI will play at a higher speed to improve learning time
            if self.human_player:
                self.clock.tick(gamesettings.FPS)
            else:
                self.clock.tick(gamesettings.AI_FPS)
            replace_blocks = 0

            # Update and redraw the blocks, check for out of bounds
            for r in self.game_platforms:              
                clear_game_object(self.screen, r)
                r.ypos = r.ypos + scroll_speed_boost
                r.update()
                if r.out_of_bounds:
                    self.game_platforms.remove(r)
                    replace_blocks = replace_blocks + 1
                    continue
                draw_game_object(self.screen, r)
            
            # A block has moved out of bounds so replace it with a new block at the top
            if replace_blocks > 0:
                top_block = self.game_platforms[len(self.game_platforms) -1]
                new_block = make_block(top_block)
                
                # NEW STAGE, INCREASE THE SPEED OF BLOCKS
                if new_block.points == gamesettings.STAGE_ONE or new_block.points == gamesettings.STAGE_TWO:
                    for b in self.game_platforms:
                        b.yvel = b.yvel + gamesettings.SCROLL_INCREMENT

                self.game_platforms.append(new_block)
                replace_blocks = 0

            # Update the players
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

            # If there is a dude in the top 3rd of the screen, then speed up the scrolling
            if highest_dude < gamesettings.SCREEN_DIM[1] / 4:
                scroll_speed_boost = gamesettings.SCROLL_SPEED_BOOST
            else:
                scroll_speed_boost = 0

            # End the game if there are no surviving players
            if len(self.live_dudes) == 0:
                self.results = end_game(self.dead_dudes)
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        #*********************************************************************


if __name__ == "__main__":
    game = HopperGame()
    game.human_player = True
    game.create_players()
    game.play()   