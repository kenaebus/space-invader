# Import pygame
import pygame
from pygame.locals import *
# Import player class
import player
from player import *

clock = pygame.time.Clock()

pygame.init()

# Set up screen
screen = pygame.display.set_mode((500,800))
fps = 60
pygame.mouse.set_visible(False)

# Player Sprites
player = Player("player.png", ((250,700)))
player_group = pygame.sprite.RenderPlain()
player_group.add(player)
steps = 20 # Pixels to Move

# Run game till player asks to quit
running = True
while running:

    # Look at every event in queue
    for event in pygame.event.get():
        # Player hits windows close button
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps,0)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)
        

        # Fill the background with blue
        screen.fill((56,59,96))
        player_group.draw(screen)
        
        player.update()
        pygame.display.update()
        clock.tick(fps)


# Quit game
pygame.quit()

