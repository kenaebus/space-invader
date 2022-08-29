# Import pygame
import pygame
from pygame.locals import *
# Import player class
import player
from player import *
# Import Level
import level
from level import Level
# Import Sys
import sys

class Game:
    def __init__(self):
        # Set up icon & caption
        playerIMG = pygame.image.load("imgs/player.png")
        pygame.display.set_caption("Space-Invader")
        pygame.display.set_icon(playerIMG)
        # Set up screen
        self.screen = pygame.display.set_mode((500,800))
        self.clock = pygame.time.Clock()
        self.mouse = pygame.mouse.set_visible(False)
        self.level = Level()

    def run(self):
        backgroundIMG = pygame.image.load("imgs/spacebackground.jpg")
        backgroundIMG = pygame.transform.scale(backgroundIMG,(800,800))
        
        fps = 60
        while True:
             # Look at every event in queue
            for event in pygame.event.get():
                # Player hits windows close button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.clock.tick(fps)
            self.screen.blit(backgroundIMG,[0,0])
            # Set up level
            self.level.run()
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()

