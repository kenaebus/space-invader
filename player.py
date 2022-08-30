from winreg import DisableReflectionKey
from xml.dom.minidom import parseString
import pygame
from bullet import Bullet

# Defining Player Object
class Player(pygame.sprite.Sprite):
    # Constructor
    def __init__(self,group):
        super().__init__(group)
        self.image = pygame.image.load("imgs/player.png")
        self.image = pygame.transform.scale(self.image,(80,80))
        self.rect = self.image.get_rect(center = (250,750) )
        self.pos = pygame.math.Vector2(self.rect.center) 
        self.direction = pygame.math.Vector2()
        

        # self.shoot = pygame.mixer.Sound("") # FIXME: IMPLEMENT SOUND
    
    def input(self):
        speed = 10 # Pixels
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[ord("a")]:
            self.direction.x = -speed
        elif keys[pygame.K_RIGHT] or keys[ord("d")]:
            self.direction.x = speed
        elif keys[pygame.K_SPACE]:
             self.create_bullet()
        else:
            self.direction.x = 0

    def move(self):
        self.pos += self.direction
        self.rect.center = self.pos

    def create_bullet(self):
        """""
        BULLET FUNCTION DOES NOT WORK!! FIXME

        return Bullet(self.rect.center[0],self.rect.center[1])
        """
    def update(self):
        self.input()
        self.move()

