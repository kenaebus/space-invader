import pygame

# Definint Bullet Object
class Bullet(pygame.sprite.Sprite):
    # Constructor
    def __init__(self,group,posX,posY):
        super().__init__(group)
        self.image = pygame.Surface((50,10))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = (posX,posY))

    # Create Bullet
    def createBullet(self):
        # TODO: DRAW BULLET
        print("Create bullet")

    # Move bullet in y-direction, 5 pixels
    def update(self):
        self.rect.y += 5