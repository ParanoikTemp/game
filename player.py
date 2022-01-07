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

    def move(self, barrier, cadr):
        keyboard = pygame.key.get_pressed()
        sdvigx, sdvigy = 0, 0
        animate = False
        if keyboard[pygame.K_w]:
            if self.rect.y < 64 * 3:
                sdvigy += self.velocity
                self.rect.y -= self.velocity
                if pygame.sprite.spritecollide(self, barrier, True):
                    sdvigy -= self.velocity
                self.rect.y += self.velocity
            else:
                self.rect.y -= self.velocity
                if pygame.sprite.spritecollide(self, barrier, True):
                    self.rect.y += self.velocity
            animate = True
        if keyboard[pygame.K_s]:
            if self.rect.y > 64 * 13:
                sdvigy -= self.velocity
                self.rect.y += self.velocity
                if pygame.sprite.spritecollide(self, barrier, True):
                    sdvigy += self.velocity
                self.rect.y -= self.velocity
            else:
                self.rect.y += self.velocity
                if pygame.sprite.spritecollide(self, barrier, True):
                    self.rect.y -= self.velocity
            animate = True
        if keyboard[pygame.K_d]:
            if self.rect.x > 64 * 20:
                sdvigx -= self.velocity
                self.rect.x += self.velocity
                if pygame.sprite.spritecollide(self, barrier, True):
                    sdvigx += self.velocity
                self.rect.x -= self.velocity
            else:
                self.rect.x += self.velocity
                if pygame.sprite.spritecollide(self, barrier, True):
                    self.rect.x -= self.velocity
                if self.rot == 'left':
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.rot = 'right'
            animate = True
        if keyboard[pygame.K_a]:
            if self.rect.x < 64 * 10:
                sdvigx += self.velocity
                self.rect.x -= self.velocity
                if pygame.sprite.spritecollide(self, barrier, True):
                    sdvigx -= self.velocity
                self.rect.x += self.velocity
            else:
                self.rect.x -= self.velocity
                if pygame.sprite.spritecollide(self, barrier, True):
                    self.rect.x += self.velocity
                if self.rot == 'right':
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.rot = 'left'
            animate = True
        if animate:
            self.image = self.images[((cadr // 10) % 2) + 1]
            self.image = pygame.transform.scale(self.image, (50, 64))
            if self.rot == 'left':
                self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.image = self.images[0]
            self.image = pygame.transform.scale(self.image, (50, 64))
        return sdvigx, sdvigy

    def sdvig(self, sdvigx, sdvigy):
        self.rect.x += sdvigx
        self.rect.y += sdvigy
