from typing import Dict
import pygame
from components import doudou
from components import pacman
from pygame.sprite import collide_mask
import data.config as cfg

def setup():
    pygame.init()
    pygame.display.set_caption("Warriors' Adventure")
def detectQuit(event):
    if event.type == (pygame.QUIT):
            print("Bye!")
            exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            print("Bye!")
            exit()
def flash(keys, screen,sprites, FPS):
    fclock = pygame.time.Clock()
    for group in sprites:
        group.update(keys, screen)
    pygame.display.flip()
    fclock.tick(FPS)

def collidedDetect(group1, group2) -> Dict:
    collideDict = pygame.sprite.groupcollide(group1,group2,False,True,collided=collide_mask)
    if collideDict != {}:
        group1.sprites()[0].score.addPoints(10)
    return collideDict

def draw_grid():
    cell_size = ((cfg.HEIGHT-cfg.MARGIN*2))

def setupPacman() -> pygame.sprite.GroupSingle:
    group = pygame.sprite.GroupSingle()
    group.add(pacman.Pacman())
    return group

if __name__ == "__main__":
    print("hello world!")