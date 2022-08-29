import pygame

from player import Player
from enemy import Enemy

class Level:
    def __init__(self):

        # Display Surface
        self.display_surface = pygame.display.get_surface()
    
        # Group sprite
        self.sprites = pygame.sprite.Group()

        self.setup()

    # Set up player
    def setup(self):
        self.player = Player(self.sprites)
        self.enemy = Enemy(self.sprites)

    def run(self):
        # Display Sprites
        self.sprites.draw(self.display_surface)
        self.sprites.update()

    