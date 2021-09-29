from data.player import Player
from data.enemy import Enemy
from data.bonus import Bonus
from data.coin import Coin
from data.__init__ import *

# Main variables
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/1.25)
player_sprites.add(player)
all_sprites.add(player)


class GameState():
    def __init__(self):
        self.state = "intro"

    def intro(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit(0)
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.state = "main_game"
                        game_state.state_manager()
            screen.fill((0, 0, 0))
            screen.blit(bar, (0, 0))
            screen.blit(title, (SCREEN_WIDTH/2-23, SCREEN_HEIGHT/2-12))
            pygame.display.flip()
            clock.tick(60)

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit(0)
                if event.type == ADD_ENEMY:
                    enemy = Enemy([random.randint(0, SCREEN_WIDTH), 0])
                    all_sprites.add(enemy)
                    senemy_sprites.add(enemy)
                if event.type == ADD_ENEMY:
                    coin = Coin([random.randint(0, SCREEN_WIDTH), 0])
                    all_sprites.add(coin)
                    senemy_sprites.add(coin)

                if event.type == ADD_BONUS:
                    bonus = Bonus([random.randint(0, SCREEN_WIDTH), 0])
                    bonus_sprites.add(bonus)
                    all_sprites.add(bonus)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.state = "intro"
                        game_state.state_manager()

            screen.fill((0, 0, 0))
            all_sprites.update()
            screen.blit(bar, (0, 0))
            pygame.display.flip()
            clock.tick(60)

    def state_manager(self):
        if self.state == "intro":
            self.intro()
        if self.state == "main_game":
            self.main()


game_state = GameState()

while True:
    game_state.state_manager()
