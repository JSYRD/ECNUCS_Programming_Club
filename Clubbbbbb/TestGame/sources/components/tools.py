import pygame
import data.config as cfg
import os
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

def flash(sprites,screen):
    fclock = pygame.time.Clock()
    sprites.update()
    sprites.draw(screen)
    pygame.display.flip()
    fclock.tick(cfg.FPS)
def loadGraphics(path, accept=('.jpg','.png','.bmp','.gif')):
    graphics = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path, pic))
            if(img.get_alpha()):
                img = img.convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img
    return graphics

def getImage(sheet, x, y, width, height, colorkey, scale):
    image = pygame.Surface((width, height))
    image.blit(sheet, (0,0), (x, y, width, height))
    image.set_colorkey(colorkey)
    # image = pygame.transform.scale(image, int(width*scale), int(height*scale))
    return image

if __name__ == "__main__":
    print("hello world!")