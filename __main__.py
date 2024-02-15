import sys
import pygame


class Display:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))


def main():
    display = Display(800, 600)
    while True:
        update(display)


def update(display):
    event_loop()


def event_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()
