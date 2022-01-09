import pygame
import pygame_widgets
import sys
import map_generator
from maps import start_map
from player import Player
pygame.init()
screen = pygame.display.set_mode((64 * 30, 64 * 16))
clock = pygame.time.Clock()
sprites = pygame.sprite.Group()
sdvigx, sdvigy = start_map.sdvigx, start_map.sdvigy
player = Player(sprites, start_map.player_pos[0] + sdvigx, start_map.player_pos[1] + sdvigy, 7)
cadr = 0

level1 = map_generator.map_generator(screen, start_map.layers, start_map.barrier)


def stop_game():
    pygame.quit()
    sys.exit()


while True:
    clock.tick(60)
    screen.fill('black')
    keyboard = pygame.key.get_pressed()
    barriers = level1.draw(sdvigx, sdvigy)
    sprites.draw(screen)
    sx, sy = player.move(barriers, cadr)
    sdvigx += sx
    sdvigy += sy
    if keyboard[pygame.K_RIGHT]:
        sdvigx -= 10
        player.sdvig(-10, 0)
    if keyboard[pygame.K_LEFT]:
        sdvigx += 10
        player.sdvig(10, 0)
    if keyboard[pygame.K_UP]:
        sdvigy += 10
        player.sdvig(0, 10)
    if keyboard[pygame.K_DOWN]:
        sdvigy -= 10
        player.sdvig(0, -10)
    pygame.display.flip()
    cadr += 1
    cadr %= 60
    [stop_game() for event in pygame.event.get() if event.type == pygame.QUIT]
