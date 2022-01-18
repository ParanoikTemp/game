import pygame
import fire_dude
import sys
import map_generator
from maps import fight_map
from player import Player
from StaticObject import Chest, Potion
from weapon import Sword
import pygame_widgets
from pygame_widgets.button import Button

pygame.init()

screen = pygame.display.set_mode((64 * 30, 64 * 16))
width, height = 64 * 30, 64 * 16

clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 60)
enemies = pygame.sprite.Group()
objects = pygame.sprite.Group()

# жеваный крот
sdvigx, sdvigy = fight_map.sdvigx, fight_map.sdvigy
level1 = map_generator.map_generator(screen, fight_map.layers, fight_map.barrier)

cadr = 0

chest = Chest(objects, 1400, 500)
player = Player(objects, fight_map.player_pos[0] + sdvigx, fight_map.player_pos[1] + sdvigy, 7)
sword = Sword(objects, player.rect.x, player.rect.y)

button = Button(screen, 700, 300, 650, 150, text="Начать игру", fontSize=150, inactiveColour=(200, 50, 0),
                hoverColour=(150, 0, 0), radius=20, onClick=lambda: set_scene(2))
button_instruction = Button(screen, 775, 600, 500, 150, text="Инструкция", fontSize=100, inactiveColour=(200, 50, 0),
                            hoverColour=(150, 0, 0), radius=20, onClick=lambda: set_scene(1))
button_menu = Button(screen, 775, 800, 500, 150, text="Меню", fontSize=100, inactiveColour=(200, 50, 0),
                     hoverColour=(150, 0, 0), radius=20, onClick=lambda: set_scene(0))

scene = 0
button_menu.hide()
spawned = False


def spawn_mosters():
    global enemies
    dude = fire_dude.FireDude(enemies, 2000, 500)
    dude2 = fire_dude.FireDude(enemies, 3100, 600)


def set_scene(x):
    global scene
    scene = x
    button.hide()
    button_instruction.hide()
    button_menu.hide()


def stop_game():
    pygame.quit()
    sys.exit()


def start_game_scene():
    button_instruction.show()
    button.show()
    screen.fill('white')
    events = pygame.event.get()
    pygame_widgets.update(events)
    [stop_game() for event in pygame.event.get() if event.type == pygame.QUIT]


def instruction():
    button_menu.show()
    screen.fill('white')
    events = pygame.event.get()
    pygame_widgets.update(events)
    with open('instruction.txt', 'r', encoding="utf8") as f:
        read_txt = f.readlines()
    for i, j in enumerate(read_txt):
        text = font.render(j[:-1], True, 'black')
        screen.blit(text, (160, 100 + i * 300))
    [stop_game() for event in pygame.event.get() if event.type == pygame.QUIT]


def death(screen):
    screen.fill((0, 0, 0))
    button_menu.show()
    font = pygame.font.Font(None, 50)
    text = font.render("Вы проиграли", True, (255, 255, 255))
    score = font.render(f'Убито врагов: {sword.kills}', True, (255, 255, 255))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    score_x, score_y = text_x, text_y + 60
    screen.blit(text, (text_x, text_y))
    screen.blit(score, (score_x, score_y))
    pygame.display.update()


while True:
    clock.tick(60)
    if scene == 0:
        start_game_scene()
    elif scene == 1:
        instruction()
    elif scene == 10:
        spawned = False
        death(screen)
    elif scene == 2:
        if not spawned:
            spawn_mosters()
            spawned = True
        screen.fill('black')
        keyboard = pygame.key.get_pressed()
        barriers = level1.draw(sdvigx, sdvigy)
        sx, sy, cords = player.move(barriers, cadr, enemies)
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
            enemy.update(cords, barriers, sx, sy, enemies, objects)
        for obj in objects:
            obj.update(objects, sx, sy, player)
        enemies.draw(screen)
        objects.draw(screen)
        if player.health == 0:
            scene = 10
    else:
        screen.fill('black')
        keyboard = pygame.key.get_pressed()
        barriers = level1.draw(sdvigx, sdvigy)
        sx, sy, cords = player.move(barriers, cadr, enemies)
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
            enemy.update(cords, barriers, sx, sy, enemies, objects)
        for obj in objects:
            obj.update(objects, sx, sy, player)
        enemies.draw(screen)
        objects.draw(screen)
    pygame.display.flip()
    cadr += 1
    cadr %= 60
    [stop_game() for event in pygame.event.get() if event.type == pygame.QUIT]
