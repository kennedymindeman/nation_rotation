import sys
import json
import pygame


class Display:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.tile_width = 60
        self.tile_height = 60

    def draw_tile(self, x, y, color):
        upper_left_x = x * self.tile_width
        upper_left_y = y * self.tile_height

        rect = (upper_left_x, upper_left_y, self.tile_width, self.tile_height)
        pygame.draw.rect(self.screen, color, rect)

    def draw_map(self, map_data):
        for y, row in enumerate(map_data['tiles']):
            for x, tile in enumerate(row):
                if tile['land']:
                    self.draw_tile(x, y, pygame.Color('green'))
                else:
                    self.draw_tile(x, y, pygame.Color('blue'))


def main():
    display = Display(800, 600)
    map_data = read_json_map_file('maps/dummy_map.json')
    display.draw_map(map_data)
    while True:
        update()


def read_json_map_file(file_path):
    with open(file_path) as json_map_file:
        return json.load(json_map_file)


def update():
    pygame.display.flip()
    event_loop()


def event_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    main()
