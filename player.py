from xml.dom.minidom import parseString
import pygame
# Defining Player Object
class Player(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, picture_path, pos):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        # self.shoot = pygame.mixer.Sound("") # FIXME: IMPLEMENT SOUND
    
    def update(self):
        pass


