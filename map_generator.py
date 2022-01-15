import pygame

pygame.init()


class Tile(pygame.sprite.Sprite):
    def __init__(self, group, num, x, y, draw_barriers=False):
        super().__init__(group)
        if num:
            if num == 999:
                if draw_barriers:
                    image = pygame.image.load('data/barrier.png')
                    image = pygame.transform.scale(image, (65, 65))
                    self.image = image
                    self.rect = self.image.get_rect()
                else:
                    self.image = pygame.surface.Surface((0, 0))
                    self.rect = pygame.rect.Rect((0, 0, 64, 64))
            else:
                image = pygame.image.load(f'data/image_part_{str(num).rjust(3, "0")}.png')
                self.image = pygame.transform.scale(image, (64, 64))
                self.rect = self.image.get_rect()
                image = pygame.transform.scale(image, (65, 65))
                self.image = image
        else:
            image = pygame.surface.Surface((64, 64))
            image.fill('black')
        self.rect.x = x
        self.rect.y = y


class map_generator:
    def __init__(self, screen, map, barrier=None):
        self.map = map
        self.screen = screen
        self.barrier = barrier

    def draw(self, sdvigx=0, sdvigy=0, draw_barriers=False):
        tiles_list = pygame.sprite.Group()
        barrier_list = pygame.sprite.Group()
        tiles = {'0': 0, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 113, 'f': 114, 'g': 115, 'h': 116, 'i': 129,
                 'j': 130, 'k': 131, 'l': 132, 'm': 17, 'n': 18, 'o': 19, 'p': 1, 'r': 2, 's': 3, 't': 117, 'q': 101,
                 'u': 51, 'v': 50, 'z': 999}
        # a - l натертость на дороге
        # mno стены спереди
        # prs верх стен
        # tuq - плоскости
        for layer in self.map:
            for y, layer_y in enumerate(layer):
                for x, color in enumerate(layer_y):
                    if color != '.':
                        Tile(tiles_list, tiles[color], x * 64 + sdvigx, y * 64 + sdvigy)
        if self.barrier:
            for y, layer_y in enumerate(self.barrier):
                for x, color in enumerate(layer_y):
                    if color != '.':
                        Tile(barrier_list, tiles[color], x * 64 + sdvigx, y * 64 + sdvigy, draw_barriers)
        tiles_list.draw(self.screen)
        barrier_list.draw(self.screen)
        return barrier_list
