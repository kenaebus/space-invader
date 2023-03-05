# Import pygame
import pygame
from pygame.locals import *
# Import player class
import playerManager
# Import Level
import level
# Import Sys
import sys

pygame.init()
pygame.font.init()

class Game:
    def __init__(self):

        # Set up icon & caption
        playerIMG = pygame.image.load("imgs/playerSprite.png")
        pygame.display.set_caption("Space-Invader by Makena Bustos")
        pygame.display.set_icon(playerIMG)

        # Set up screen

        # Find player's screen info
        infoObject = pygame.display.Info()
        self.SCREEN_WIDTH = infoObject.current_w
        self.SCREEN_LENGTH = infoObject.current_h

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_LENGTH))
        self.clock = pygame.time.Clock()
        self.mouse = pygame.mouse.set_visible(False)
        self.level = level.GameLevel()

    def run(self):
        backgroundIMG = pygame.image.load("imgs/spacebackground.jpg")
        backgroundIMG = pygame.transform.scale(backgroundIMG,(self.SCREEN_WIDTH,self.SCREEN_LENGTH))
        
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
            self.level.run()
        
            pygame.display.update()  

if __name__ == "__main__":

    game = Game()
    game.run()

