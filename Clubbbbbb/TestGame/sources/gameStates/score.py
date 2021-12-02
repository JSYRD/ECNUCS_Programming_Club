import pygame
import pygame.freetype
class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.fconsola = pygame.freetype.Font("./fonts/consola.ttf")
        self.score = 0
    def addPoints(self, point):
        self.score += point
    def update(self, screen, keys):
        self.fconsola.render_to(screen,(200, 900),"%d" %self.score,fgcolor=(0,0,0),size=100)