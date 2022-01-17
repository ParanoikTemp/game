import pygame
import pygame_widgets
import fire_dude
import sys
import map_generator
from maps import fight_map
from player import Player
pygame.init()
screen = pygame.display.set_mode((64 * 30, 64 * 16))
clock = pygame.time.Clock()
sprites = pygame.sprite.Group()
sdvigx, sdvigy = fight_map.sdvigx, fight_map.sdvigy
player = Player(sprites, fight_map.player_pos[0] + sdvigx, fight_map.player_pos[1] + sdvigy, 7)
cadr = 0
enemies = pygame.sprite.Group()
dude = fire_dude.FireDude(enemies, 1000, 500)
# жеваный крот

level1 = map_generator.map_generator(screen, fight_map.layers, fight_map.barrier)


def stop_game():
    pygame.quit()
    sys.exit()


while True:
    clock.tick(60)
    screen.fill('black')
    keyboard = pygame.key.get_pressed()
    barriers = level1.draw(sdvigx, sdvigy)
    enemies.draw(screen)
    sprites.draw(screen)
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
    pygame.display.flip()
    cadr += 1
    cadr %= 60
    [stop_game() for event in pygame.event.get() if event.type == pygame.QUIT]
