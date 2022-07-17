import random

import pygame
pygame.init()

size = WIDTH, HEIGHT = 650, 650
player_size_x = 100
player_size_y = 100
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Rain Shooter')

playerIMG = pygame.image.load('images/playerIMG.png')
playerIMG = pygame.transform.scale(playerIMG, (player_size_x, player_size_y))
enemyIMG = pygame.image.load('images/enemy.png')
enemyIMG = pygame.transform.scale(enemyIMG, (80, 80))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerIMG
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2 
        self.rect.top = HEIGHT - 120
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.speedx = -5
        if keys[pygame.K_d]:
            self.speedx = 5

        if self.rect.x >= WIDTH - player_size_x:
            self.rect.x = WIDTH - player_size_x - 5
        if self.rect.x <= 0:
            self.rect.x = 5

        self.rect.x += self.speedx

    def create_bullet(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemyIMG
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(2, 6)
        self.speedx = random.randrange(-2, 2)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT + 10 or self.rect.left < -50 or self.rect.right > WIDTH + 50:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 6)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 15))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.bottom = y + 20
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy

        if self.rect.y <= -10:
            self.kill()


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()

all_sprites.add(player)

clock = pygame.time.Clock()

for i in range(500):
    m = Mob()
    mobs.add(m)


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.create_bullet()


        clock.tick(60)
        screen.fill([100, 105, 0])

        all_sprites.update()
        mobs.update()

        all_sprites.draw(screen)
        mobs.draw(screen)

        hit_player = pygame.sprite.spritecollide(player, mobs, True)
        if hit_player:
            print(hit_player)
        hit_enemy = pygame.sprite.groupcollide(bullets, mobs, True, True)
        if hit_enemy:
            print(hit_enemy)

        pygame.display.flip()


if __name__ == '__main__':
    main()
