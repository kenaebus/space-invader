import pygame

# Defining Enemy Object
class Enemy(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load("imgs/enemy.png")
        self.image = pygame.transform.scale(self.image,(80,80))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)