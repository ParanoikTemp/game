import pygame


class Sword(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.images = [pygame.image.load('data/sword0.png'), pygame.image.load('data/sword1.png')]
        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, (40, 20))
        self.rect = self.image.get_rect()
        # координаты отрисовки меча, такиеже как у персонажа
        self.rect.x = x
        self.rect.y = y
        self.type = "sword"
        self.attack = False
        self.cadr = 0
        self.kills = 0

    def update(self, objects, sx, sy, player):
        if player.rot == 'right':
            k = 1
            self.image = self.images[0]
            self.image = pygame.transform.scale(self.image, (40, 20))
        else:
            k = -1
            self.image = self.images[1]
            self.image = pygame.transform.scale(self.image, (40, 20))
        self.rect.x = player.rect.x + 20 * k
        self.rect.y = player.rect.y + 35
        mouse = pygame.mouse.get_pressed(3)
        if not self.attack and mouse[0]:
            self.attack = True
            self.cadr = 0
        elif self.attack:
            self.cadr += 1
            if self.cadr <= 30:
                self.rect.x += self.cadr * k
            elif self.cadr == 60:
                self.cadr = 0
                self.attack = False
            elif self.cadr > 30:
                self.rect.x += (60 - self.cadr) * k


