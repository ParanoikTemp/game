import pygame
pygame.init()


def rast(x, y, x1, y1):
    kek = ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5
    if kek < 5:
        kek = 10
    return kek


class FireDude(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = pygame.image.load('data/firedude.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (48, 48))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.velocity = 4
        self.cadr = 0
        self.type = 'firedude'

    def update(self, pc, barrier, sx, sy, enemies):
        self.cadr += 1
        if sx or sy:
            self.rect.x += sx
            self.rect.y += sy
        px, py = pc
        if abs(rast(self.rect.x, self.rect.y, px, py)) < 600:
            if abs(rast(self.rect.x, self.rect.y, px, py)) < 200:
                k = rast(self.rect.x, self.rect.y, px, py) / self.velocity
                a = (self.rect.x - px) / k
                self.rect.x += a
                if pygame.sprite.spritecollideany(self, barrier, None):
                    self.rect.x -= a * 2
                b = (self.rect.y - py) / k
                self.rect.y += b
                if pygame.sprite.spritecollideany(self, barrier, None):
                    self.rect.y -= b * 2
            elif abs(rast(self.rect.x, self.rect.y, px, py)) > 300:
                k = rast(self.rect.x, self.rect.y, px, py) / self.velocity
                a = (self.rect.x - px) / k
                self.rect.x -= a
                if pygame.sprite.spritecollideany(self, barrier, None):
                    self.rect.x += a * 2
                b = (self.rect.y - py) / k
                self.rect.y -= b
                if pygame.sprite.spritecollideany(self, barrier, None):
                    self.rect.y += b * 2
            self.attack(enemies)

    def attack(self, enemies):
        if self.cadr == 239:
            FireBullet(enemies, self.rect.x, self.rect.y)
        self.cadr %= 240

    def get_cords(self):
        return self.rect.x, self.rect.y


class FireBullet(pygame.sprite.Sprite):
    def __init__(self, group, dx, dy):
        super().__init__(group)
        self.image = pygame.image.load('data/firebullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (48, 48))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = dx, dy
        self.velocity = 8
        self.cadr = 0
        self.k = 1
        self.a, self.b = 1, 1
        self.type = 'firebullet'

    def update(self, pc, barrier, sx, sy, enemies):
        self.cadr += 1
        if sx or sy:
            self.rect.x += sx
            self.rect.y += sy
        px, py = pc
        if self.cadr == 1:
            self.k = rast(self.rect.x, self.rect.y, px, py) / self.velocity
            self.a = (self.rect.x - px) / self.k
            self.b = (self.rect.y - py) / self.k
        self.rect.x -= self.a
        self.rect.y -= self.b
        if pygame.sprite.spritecollideany(self, barrier, None):
            self.kill()
        self.cadr %= 60
