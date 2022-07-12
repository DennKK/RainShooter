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
        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_RIGHT]:
            self.x += 5

    def draw(self):
        pygame.draw.rect(screen, (0, 0, 128), [self.x, HEIGHT - 120, self.x_size, self.y_size])

        if self.x >= WIDTH - self.x_size:
            self.x = WIDTH - self.x_size - 5
        if self.x <= 0:
            self.x = 5


player = Player()
clock = pygame.time.Clock()


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(60)
        screen.fill([120, 10, 70])
        player.draw()
        player.handle_keys()
        pygame.display.update()
        pygame.display.flip()


if __name__ == '__main__':
    main()
