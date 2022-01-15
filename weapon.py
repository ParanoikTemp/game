import pygame


class Weapon(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)

        #
        self.images = [pygame.image.load('data/sword0.png'), pygame.image.load('data/sword1.png')]
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        # координаты отрисовки меча, такиеже как у персонажа
        self.rect.x = x
        self.rect.y = y

        self.type = "weapon"

        self.caunt = 0

    def sword(self, x, y, direction):

        if direction == 'right':
            self.image = self.images[0]
            # координаты отрисовки меча
            self.rect.x = x + 14
            self.rect.y = y + 32

            # отрисовка оружия
            self.image = pygame.transform.scale(self.image, (52, 20))

            mouse = pygame.mouse.get_pressed(3)

            #
            if mouse[0]:
                self.rect.x = x + 14
                self.rect.y = y

                # отрисовка оружияaa
                self.image = pygame.transform.rotate(self.image, 70)

        if direction == 'left':
            self.image = self.images[1]

            # координаты отрисовки меча
            self.rect.x = x - 14
            self.rect.y = y + 32

            # отрисовка оружия
            self.image = pygame.transform.scale(self.image, (52, 20))

            mouse = pygame.mouse.get_pressed(3)

            #
            if mouse[0]:
                self.rect.x = x
                self.rect.y = y

                # отрисовка оружия
                self.image = pygame.transform.rotate(self.image, -70)
