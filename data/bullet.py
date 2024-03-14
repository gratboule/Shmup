from data.__init__ import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        self.surf = pygame.image.load("assets/sprites/bullets/bullet1.png").convert_alpha()
        self.rect = self.surf.get_rect()
        self.rect.center = [x, y]
        self.speed = 1

    def update(self):
        self.rect.y -= 6
        screen.blit(self.surf, self.rect)
        if self.rect.bottom < 0:
            self.kill()
