import pygame
class Doudou(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./doudou.png").convert()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
    def setPlace(self, coordinates):
        self.rect.center = coordinates
    def update(self, screen):
        screen.blit(self.image, self.rect)