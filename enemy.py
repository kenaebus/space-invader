import pygame
import main
import bullet

# Defining Enemy Object
class Enemy(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load("imgs/enemySprite.png")
        self.image = pygame.transform.scale(self.image,(80,80))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)

    def EnemyDie(self):
        # TODO: MAKE ENEMY DIE WHEN TOUCHING BULLET
        print("Enemy Died")
        
    
    def draw(self):
        # TODO: CREATE ENEMY
        print("Created Enemy")
