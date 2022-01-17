import pygame
import pygame_widgets
import fire_dude
import sys
import map_generator
from maps import fight_map
from player import Player
from StaticObject import Chest, Potion

pygame.init()
screen = pygame.display.set_mode((64 * 30, 64 * 16))
clock = pygame.time.Clock()
sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
objects = pygame.sprite.Group()

# жеваный крот
sdvigx, sdvigy = fight_map.sdvigx, fight_map.sdvigy
level1 = map_generator.map_generator(screen, fight_map.layers, fight_map.barrier)

cadr = 0

chest = Chest(objects, 500, 500)
potion = Potion(objects, 500, 540)
player = Player(sprites, fight_map.player_pos[0] + sdvigx, fight_map.player_pos[1] + sdvigy, 7)
dude = fire_dude.FireDude(enemies, 1000, 500)


def stop_game():
    pygame.quit()
    sys.exit()


while True:
    clock.tick(60)
    screen.fill('black')
    keyboard = pygame.key.get_pressed()
    barriers = level1.draw(sdvigx, sdvigy)
    sx, sy, cords = player.move(barriers, cadr)
    sdvigx += sx
    sdvigy += sy
    # pygame.draw.line(screen, (255, 0, 0), player.get_cords(), dude.get_cords(), 3)
    # pygame.draw.circle(screen, (0, 255, 0), player.get_cords(), 200, 3)
    # pygame.draw.circle(screen, (0, 255, 0), player.get_cords(), 300, 3)
    if keyboard[pygame.K_RIGHT]:
        sdvigx -= 10
        sx -= 10
        player.sdvig(-10, 0)
    if keyboard[pygame.K_LEFT]:
        sdvigx += 10
        sx += 10
        player.sdvig(10, 0)
    if keyboard[pygame.K_UP]:
        sdvigy += 10
        sy += 10
        player.sdvig(0, 10)
    if keyboard[pygame.K_DOWN]:
        sdvigy -= 10
        sy -= 10
        player.sdvig(0, -10)
    for enemy in enemies:
        enemy.update(cords, barriers, sx, sy, enemies)
    for obj in objects:
        obj.update(sprites, sx, sy, player)
    enemies.draw(screen)
    objects.draw(screen)
    sprites.draw(screen)
    pygame.display.flip()
    cadr += 1
    cadr %= 60
    [stop_game() for event in pygame.event.get() if event.type == pygame.QUIT]
