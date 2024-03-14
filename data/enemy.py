from data.__init__ import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Enemy, self).__init__()
        self.anim1 = pygame.image.load("assets/sprites/enemies/green_enemy1.png")
        self.anim2 = pygame.image.load("assets/sprites/enemies/green_enemy2.png")
        self.surf = self.anim1
        self.rect = self.surf.get_rect()

        self.anim = [self.anim1, self.anim2]
        self.index = 0
        self.posX = pos[0]
        self.posY = pos[1]
        self.rect = self.anim[self.index].get_rect(center=(self.posX, self.posY))
        self.pos = (self.posX, self.posY)
        self.dirX = 0
        self.dirY = 0.1

    def animation(self):
        self.index += 0.4
        if self.index >= len(self.anim):
            self.index = 0
        self.surf = self.anim[int(self.index)]

    def update(self):
        self.animation()
        self.posY += self.dirY
        self.posX += self.dirX
        self.rect.center = [self.posX, self.posY]
        if self.rect.bottom < 0:
            self.kill()
        screen.blit(self.surf, self.rect)
