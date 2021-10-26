import pygame
import data.config as cfg


class calculator():
    def add(self,a,b):
        return a+b
def mult(a, b):
    return a*b
def change(a):
    a=10
def main():
    print("Hello World, this is tools.")


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
    pygame.display.set_caption("Hello World!")

def flash(sprites,screen):
    fclock = pygame.time.Clock()
    sprites.update()
    sprites.draw(screen)
    pygame.display.flip()
    fclock.tick(cfg.FPS)

if __name__ == "__main__":
    print("hello world!")