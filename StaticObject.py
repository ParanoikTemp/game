import pygame


class Chest(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)

        self.images = [pygame.image.load('data/image_chest_close.png'), pygame.image.load('data/image_chest_open.png')]
        self.image = pygame.transform.scale(self.images[0], (48, 48))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = 'potion'

    def update(self, sprites, sx, sy, *x):
        self.rect.x += sx
        self.rect.y += sy
        keyboard = pygame.key.get_pressed()
        if keyboard[pygame.K_e]:
            spr = pygame.sprite.spritecollide(self, sprites, False)
            for i in spr:
                if i.type == 'player':
                    self.image = pygame.transform.scale(self.images[1], (48, 48))

    def sdvig(self, sdvigx, sdvigy):
        self.rect.x += sdvigx
        self.rect.y += sdvigy


class Potion(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)

        self.image = pygame.transform.scale(pygame.image.load('data/image_potion_speed.png').convert_alpha(), (48, 48))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = 'potion'

    def update(self, sprites, sx, sy, player, *k):
        keyboard = pygame.key.get_pressed()
        self.rect.x += sx
        self.rect.y += sy
        if keyboard[pygame.K_e]:
            spr = pygame.sprite.spritecollide(self, sprites, False)
            for i in spr:
                if i.type == 'player':
                    self.image = pygame.transform.scale(self.image, (48, 48))
                    player.add_speed(1.5)
                    self.kill()

