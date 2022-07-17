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


class Player(object):
    def __init__(self):
        self.player_rect = playerIMG.get_rect()
        self.x = WIDTH // 2 - player_size_x // 2

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= 5
        if keys[pygame.K_d]:
            self.x += 5

    def draw(self):
        # pygame.draw.rect(screen, (0, 0, 128), [self.x, HEIGHT - 120, self.x_size, self.y_size])
        screen.blit(playerIMG, [self.x, HEIGHT - 120, self.player_rect.x, self.player_rect.y])

    def update(self):
        if self.x >= WIDTH - player_size_x:
            self.x = WIDTH - player_size_x - 5
        if self.x <= 0:
            self.x = 5

    def create_bullet(self):
        return Bullet(self.x, HEIGHT - 120, player_size_x)


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
    def __init__(self, pos_x, pos_y, player_size_x):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(pos_x + player_size_x // 2, pos_y))

    def update(self):
        self.rect.y -= 10

        if self.rect.y <= -10:
            self.kill()


player = Player()
clock = pygame.time.Clock()
mobs = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
for i in range(10):
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
                    bullet_group.add(player.create_bullet())

        clock.tick(60)
        screen.fill([100, 105, 0])
        bullet_group.draw(screen)
        player.draw()
        mobs.draw(screen)
        player.handle_keys()
        bullet_group.update()
        player.update()
        mobs.update()
        pygame.display.flip()


if __name__ == '__main__':
    main()
