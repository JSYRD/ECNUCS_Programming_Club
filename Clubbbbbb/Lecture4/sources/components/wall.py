import pygame
class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Surface((100,100))
        self.rect.fill((255,255,255))
        self.rect.x = 500
        self.rect.bottom = 900
