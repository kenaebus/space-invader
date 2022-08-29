# Import pygame
import pygame
from pygame.locals import *
# Import player class
import player
from player import *

pygame.init()

# Set up screen
screen = pygame.display.set_mode((500,800))
pygame.mouse.set_visible(False)

# Player Sprites
player = Player("player.png", ((250,700)))
player_group = pygame.sprite.RenderPlain()
player_group.add(player)


# Run game till player asks to quit
running = True
while running:

    # Look at every event in queue
    for event in pygame.event.get():
        # Player hits
        if event.type == pygame.QUIT:
            running = False
        
        # Fill the background with blue
        screen.fill((56,59,96))
        player_group.draw(screen)

        pygame.display.update()


# Quit game
pygame.quit()

