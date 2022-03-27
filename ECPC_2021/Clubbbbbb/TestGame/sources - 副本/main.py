import os
import pygame
from components import tools,warrior
from states import level
import data.config as cfg
from sys import exit

tools.setup()
screen = pygame.display.set_mode(cfg.SIZE)
level1 = level.Level("./images/Level1.png")
warrior = warrior.Warrior(332)

while(True):
    eventList = pygame.event.get()
    # screen.fill((255,255,255))
    keys=pygame.key.get_pressed()
    sprites = pygame.sprite.Group()
    sprites.add(level1)
    for event in eventList:
        tools.detectQuit(event)
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
    warrior.update(keys,screen)
    tools.flash(sprites,screen)