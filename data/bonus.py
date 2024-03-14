from data.__init__ import *


class Bonus(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Bonus, self).__init__()
        self.anim1 = pygame.image.load("assets/sprites/bonus/bonus1.png")
        self.anim2 = pygame.image.load("assets/sprites/bonus/bonus2.png")
        self.anim3 = pygame.image.load("assets/sprites/bonus/bonus3.png")
        self.anim = [self.anim1, self.anim2, self.anim3]
        self.index = 0

        self.posX = pos[0]
        self.posY = pos[1]
        self.rect = self.anim[self.index].get_rect(center=(self.posX, self.posY))
        self.pos = [self.posX, self.posY]
        self.dirX = 0
        self.dirY = 0.3

    def animation(self):
        self.index += 0.6
        if self.index >= len(self.anim):
            self.index = 0
        self.surf = self.anim[int(self.index)]

    def update(self):
        self.animation()

        self.posX += self.dirX
        self.posY += self.dirY
        self.rect.center = (self.posX, self.posY)

        if self.rect.top >= SCREEN_HEIGHT:
            self.kill()
        screen.blit(self.surf, self.rect)
