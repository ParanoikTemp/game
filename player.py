import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, group, x, y, velocity=5):
        super().__init__(group)
        self.images = [pygame.image.load('data/player1.png'), pygame.image.load('data/player2.png'),
                       pygame.image.load('data/player3.png')]
        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, (50, 64))
        self.rect = self.image.get_rect()
        self.rect.width = 50
        self.rect.x = x
        self.rect.y = y
        self.velocity = velocity
        self.rot = 'right'
        self.type = 'player'
        self.health = 5
        self.cadr = 0
        self.immortal = False

    def move(self, barrier, cadr, group):
        keyboard = pygame.key.get_pressed()
        sdvigx, sdvigy = 0, 0
        animate = False
        if not self.immortal:
            for spr in pygame.sprite.spritecollide(self, group, False):
                if spr.type == 'firebullet':
                    self.immortal = True
                    self.cadr = 0
                    self.health -= 1
                    print(self.health)
                    spr.kill()
                    break
        else:
            self.cadr += 1
            if self.cadr == 60:
                self.cadr = 0
                self.immortal = False

        if keyboard[pygame.K_w]:
            animate = True
            if self.rect.y < 64 * 3:
                sdvigy += self.velocity
                self.rect.y -= self.velocity
                if pygame.sprite.spritecollideany(self, barrier, None):
                    sdvigy -= self.velocity
                self.rect.y += self.velocity
            else:
                self.rect.y -= self.velocity
                if pygame.sprite.spritecollideany(self, barrier, None):
                    self.rect.y += self.velocity
        if keyboard[pygame.K_s]:
            animate = True
            if self.rect.y > 64 * 13:
                sdvigy -= self.velocity
                self.rect.y += self.velocity
                if pygame.sprite.spritecollideany(self, barrier, None):
                    sdvigy += self.velocity
                self.rect.y -= self.velocity
            else:
                self.rect.y += self.velocity
                if pygame.sprite.spritecollideany(self, barrier, None):
                    self.rect.y -= self.velocity
        if keyboard[pygame.K_d]:
            animate = True
            if self.rect.x > 64 * 20:
                sdvigx -= self.velocity
                self.rect.x += self.velocity
                if pygame.sprite.spritecollideany(self, barrier, None):
                    sdvigx += self.velocity
                self.rect.x -= self.velocity
            else:
                self.rect.x += self.velocity
                if pygame.sprite.spritecollideany(self, barrier, None):
                    self.rect.x -= self.velocity
            if self.rot == 'left':
                self.image = pygame.transform.flip(self.image, True, False)
                self.rot = 'right'
        if keyboard[pygame.K_a]:
            animate = True
            if self.rect.x < 64 * 10:
                sdvigx += self.velocity
                self.rect.x -= self.velocity
                if pygame.sprite.spritecollideany(self, barrier, None):
                    sdvigx -= self.velocity
                self.rect.x += self.velocity
            else:
                self.rect.x -= self.velocity
                if pygame.sprite.spritecollideany(self, barrier, None):
                    self.rect.x += self.velocity
            if self.rot == 'right':
                self.image = pygame.transform.flip(self.image, True, False)
                self.rot = 'left'
        if animate:
            self.image = self.images[((cadr // 10) % 2) + 1]
            self.image = pygame.transform.scale(self.image, (50, 64))
            if self.rot == 'left':
                self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.image = self.images[0]
            if self.rot == 'left':
                self.image = pygame.transform.flip(self.image, True, False)
            self.image = pygame.transform.scale(self.image, (50, 64))
        return sdvigx, sdvigy, (self.rect.x, self.rect.y)

    def sdvig(self, sdvigx, sdvigy):
        self.rect.x += sdvigx
        self.rect.y += sdvigy

    def get_cords(self):
        return self.rect.x, self.rect.y

    def add_speed(self, vel):
        self.velocity *= vel
        self.velocity = int(self.velocity)
