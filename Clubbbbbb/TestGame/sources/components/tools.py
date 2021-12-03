import pygame
from gameStates import level
from components import warrior
from components import beast
from pygame.sprite import collide_mask
import data.config as cfg
def detectQuit(event):
    if event.type == (pygame.QUIT):
            print("Bye!")
            exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            print("Bye!")
            exit()
    
def setup():
    pygame.init()
    pygame.display.set_caption("Warriors' Adventure")

def flash(screen,keys,sprites):
    fclock = pygame.time.Clock()
    for group in sprites:
        group.update(screen,keys,sprites)
    pygame.display.flip()
    fclock.tick(cfg.FPS)

def collidedDetect(group1, group2, ):
    collideDict = pygame.sprite.groupcollide(group1,group2,False,True,collided=collide_mask)
    if collideDict != {}:
        for i in range(0,len(collideDict)):
            group1.sprites()[0].score.addPoints(10)
    return collideDict

def setupWarriorGroup():
    group = pygame.sprite.GroupSingle()
    warrior0 = warrior.Warrior(332,"./images/huashi.png",3)
    group.add(warrior0)
    return group
def setupBackground():
    group = pygame.sprite.Group()
    group.add(level.Level("./images/Level1_long.png"))
    return group
def setupBeastGroup():
    group = pygame.sprite.Group()
    for i in range(0,5):
        yrd = beast.Beast(332,"./images/Warriort.png",8)
        yrd.rect.center = (1920-100,yrd.windowsInfo.current_h-332-70)
        yrd.changeCompass()
        group.add(yrd)
    return group

if __name__ == "__main__":
    print("hello world!")