from xml.dom.minidom import parseString
import pygame

# Defining Player Object
class Player(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, picture_path, pos):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(self.image,(90,90))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        # self.shoot = pygame.mixer.Sound("") # FIXME: IMPLEMENT SOUND
        
        # Player Movement
        self.moveX = 0
        self.moveY = 0
        self.frame = 0
    
    def control(self,x,y):
        self.moveX += x
        self.moveY += y

    def update(self):
        
        self.rect.x = self.rect.x + self.moveX
        self.rect.y = self.rect.y + self.moveY
