import pygame
from components import tools

class Level(pygame.sprite.Sprite):
    def __init__(self,path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path).convert()
        self.rect = self.image.get_rect()
        self.groundHeight = 332
    def update(self,screen,keys):
        screen.blit(self.image,self.rect)
