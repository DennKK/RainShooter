import pygame
pygame.init()

size = WIDTH, HEIGHT = 650, 650
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Rain Shooter')


class Player(object):
    def __init__(self):
        self.x_size = 50
        self.y_size = 100
        self.x = WIDTH // 2 - self.x_size // 2

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= 5
        if keys[pygame.K_d]:
            self.x += 5

    def draw(self):
        pygame.draw.rect(screen, (0, 0, 128), [self.x, HEIGHT - 120, self.x_size, self.y_size])

    def update(self):
        if self.x >= WIDTH - self.x_size:
            self.x = WIDTH - self.x_size - 5
        if self.x <= 0:
            self.x = 5

    def create_bullet(self):
        return Bullet(self.x, HEIGHT - 120, self.x_size)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, x_size):
        super().__init__()
        self.image = pygame.Surface((10, 25))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(pos_x + x_size // 2, pos_y))

    def update(self):
        self.rect.y -= 10

        if self.rect.y <= -10:
            self.kill()


player = Player()
clock = pygame.time.Clock()

bullet_group = pygame.sprite.Group()


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
        screen.fill([120, 10, 70])
        bullet_group.draw(screen)
        player.draw()
        player.handle_keys()
        bullet_group.update()
        player.update()
        pygame.display.flip()


if __name__ == '__main__':
    main()
