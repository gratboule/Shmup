from data.__init__ import *


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Coin, self).__init__()
        self.anim1 = pygame.image.load("C:/dev/pygame/Shmup/assets/sprites/coins/coin1.png")
        self.anim2 = pygame.image.load("C:/dev/pygame/Shmup/assets/sprites/coins/coin2.png")
        self.anim3 = pygame.image.load("C:/dev/pygame/Shmup/assets/sprites/coins/coin3.png")
        self.anim = [self.anim1, self.anim2, self.anim3]
        self.index = 0

        self.posX = pos[0]
        self.posY = pos[1]
        self.rect = self.anim[self.index].get_rect(center=(self.posX, self.posY))
        self.pos = [self.posX, self.posY]
        self.dirX = 0
        self.dirY = 1

    def animation(self):
        self.index += 0.2
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
