import pygame
class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y, npc_rects):
        pygame.sprite.Sprite.__init__(self)
        # self.image = tools.get_image()
        # self.rec
class Wangfeng(NPC):
    def __init__(self, x, y):
        npc_rects = (250, 46, 39, 42)
        super().__init__(x, y, npc_rects)


wangfeng = Wangfeng(10, 20)
print(wangfeng)