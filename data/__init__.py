import pygame
from pygame.locals import *
import random

pygame.init()

SCREEN_WIDTH = 88
SCREEN_HEIGHT = 128
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED, pygame.FULLSCREEN)
clock = pygame.time.Clock()
k = pygame.key.get_pressed()
bar = pygame.image.load("assets/sprites/bar/bar.png")
title = pygame.image.load("assets/sprites/bar/title.png")

# Groups
all_sprites = pygame.sprite.Group()
player_sprites = pygame.sprite.Group()
bullets_sprites = pygame.sprite.Group()
bonus_sprites = pygame.sprite.Group()
senemy_sprites = pygame.sprite.Group()

ADD_BONUS = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_BONUS, 10000)

ADD_COIN = pygame.USEREVENT + 3
pygame.time.set_timer(ADD_COIN, 1000)

ADD_ENEMY = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_ENEMY, 2000)
