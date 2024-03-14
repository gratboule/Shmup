from data.__init__ import *
from data.bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.anim1 = pygame.image.load("assets/sprites/player/player1.png")
        self.anim2 = pygame.image.load("assets/sprites/player/player2.png")
        self.anim3 = pygame.image.load("assets/sprites/player/player3.png")

        self.left1 = pygame.image.load("assets/sprites/player/player_left1.png")
        self.left2 = pygame.image.load("assets/sprites/player/player_left2.png")
        self.left3 = pygame.image.load("assets/sprites/player/player_left3.png")

        self.right1 = pygame.image.load("assets/sprites/player/player_right1.png")
        self.right2 = pygame.image.load("assets/sprites/player/player_right2.png")
        self.right3 = pygame.image.load("assets/sprites/player/player_right3.png")


        self.anim = [self.anim1, self.anim2, self.anim3]
        self.anim_index = 0
        self.rect = self.anim1.get_rect()
        self.rect.center = [x, y]
        self.speed = 1
        self.last_shot = pygame.time.get_ticks()

    def move(self):
        k = pygame.key.get_pressed()
        if k[K_RIGHT]:
            self.rect.x += self.speed
            self.anim = [self.right1, self.right2, self.right3]
        if k[K_LEFT]:
            self.rect.x -= self.speed
            self.anim = [self.left1, self.left2, self.left3]
        if k[K_UP]:
            self.rect.y -= self.speed
            self.anim = [self.anim1, self.anim2, self.anim3]
        if k[K_DOWN]:
            self.rect.y += self.speed
            self.anim = [self.anim1, self.anim2, self.anim3]

    def screen_border(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def animation(self):
        self.anim_index += 0.3
        if self.anim_index >= len(self.anim):
            self.anim_index = 0
        self.surf = self.anim[int(self.anim_index)]

    def shoot(self):
        delta_shoot = 300
        time_now = pygame.time.get_ticks()
        k = pygame.key.get_pressed()
        if k[K_SPACE] and time_now - self.last_shot > delta_shoot:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bullets_sprites.add(bullet)
            all_sprites.add(bullet)
            self.last_shot = time_now


    def update(self):
        self.animation()
        self.move()
        self.shoot()
        self.screen_border()
        screen.blit(self.surf, self.rect)





