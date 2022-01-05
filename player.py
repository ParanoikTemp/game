import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, group, x, y, velocity=5):
        super().__init__(group)
        self.image = pygame.image.load('data/image_part_256.png')
        self.image = pygame.transform.scale(self.image, (50, 64))
        self.rect = self.image.get_rect()
        self.rect.width = 50
        self.rect.x = x
        self.rect.y = y
        self.velocity = velocity
        self.rot = 'right'

    def move(self, barrier):
        keyboard = pygame.key.get_pressed()
        if keyboard[pygame.K_w]:
            self.rect.y -= self.velocity
            if pygame.sprite.spritecollide(self, barrier, True):
                self.rect.y += self.velocity
        if keyboard[pygame.K_s]:
            self.rect.y += self.velocity
            if pygame.sprite.spritecollide(self, barrier, True):
                self.rect.y -= self.velocity
        if keyboard[pygame.K_d]:
            self.rect.x += self.velocity
            if pygame.sprite.spritecollide(self, barrier, True):
                self.rect.x -= self.velocity
            if self.rot == 'left':
                self.image = pygame.transform.flip(self.image, True, False)
                self.rot = 'right'
        if keyboard[pygame.K_a]:
            self.rect.x -= self.velocity
            if pygame.sprite.spritecollide(self, barrier, True):
                self.rect.x += self.velocity
            if self.rot == 'right':
                self.image = pygame.transform.flip(self.image, True, False)
                self.rot = 'left'

    def sdvig(self, sdvigx, sdvigy):
        self.rect.x += sdvigx
        self.rect.y += sdvigy
