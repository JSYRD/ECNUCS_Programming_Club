import pygame
from components import tools
from data import config
class Level(pygame.sprite.Sprite):
    def __init__(self,path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path).convert()
        self.rect = self.image.get_rect()
        self.groundHeight = 332
    def updateWindow(self, warrior):
        if ((warrior.speed > 0) and (warrior.rect.right > self.rect.x + config.WIDTH / 3)):
            self.rect.x += warrior.speed
    def update(self,screen,keys, sprites):
        self.updateWindow(sprites[1].sprites()[0])
        screen.blit(self.image,(0,0),self.rect)
