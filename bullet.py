import pygame

# Definint Bullet Object
class Bullet(pygame.sprite.Sprite):
    # Constructor
    def __init__(self,group):
        super().__init__(group)
        # self.image = pygame.image.load() FIXME: Add img
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()


    def move(self):
        print("FIXME: Add move()")
        
    def update(self):
        self.move()