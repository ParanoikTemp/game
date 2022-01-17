import pygame
import sys
import map_generator
import string
import time

pygame.init()
screen = pygame.display.set_mode((64 * 30, 64 * 16))
layers = [[]]
barrier = []
layer = 0
block = '.'
clock = pygame.time.Clock()
bar_vis = True
map3 = map_generator.map_generator(screen, layers)
sdvigx = sdvigy = 0
player_pos = [32, 32]
tiles_names = {'0': 'Черный блок', 'a': 'Натертость на дороге верхний левый угол',
               'b': "Натертость на дороге верх лево", 'c': "Натертость на дорого верх право",
               'd': "Натертость на дороге верхний правый угол", 'e': "Натертость на дороге центр левый бок",
               'f': "Натерстость на дороге центр слева", 'g': "Натертость на дороге центр справа",
               'h': "Натертость на дороге ццентр правый бок", 'i': "Натертость на дороге нижний левый угол",
               'j': "Натертость на дороге снизу слева", 'k': "Натертость на дороге снизу справа",
               'l': "Натертость на дороге снизу правый угол", 'm': "Стена влево",
               'n': "Стена центральная", 'o': "Стена вправо",
               'p': "Плоскость на стене влево", 'r': "Плоскость на стене центр", 's': "Плоскость на стене вправо",
               't': "Светлый блок", 'q': "Средне-светлый блок",
               'u': "Темный блок", 'v': "Череп", '.': 'Пустота'}


def stop_game():
    sys.exit()


create_map_flag = True
create_barrier = False
create_player = False


def create_map():
    global layer, layers, block, map3, sdvigx, sdvigy, tiles_names, bar_vis, player_pos
    tiles = {'0': 0, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 113, 'f': 114, 'g': 115, 'h': 116, 'i': 129,
             'j': 130, 'k': 131, 'l': 132, 'm': 17, 'n': 18, 'o': 19, 'p': 1, 'r': 2, 's': 3, 't': 117, 'q': 101,
             'u': 51, 'v': 50}
    # a - l натертость на дороге
    # mno стены спереди
    # prs верх стен
    # tuq - плоскости
    keyboard = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed(3)
    x, y = pygame.mouse.get_pos()
    if keyboard[pygame.K_TAB]:
        layers.append([])
        print('Слой добавлен!')
        time.sleep(0.5)
        pygame.display.set_caption(f'Выбран блок: {tiles_names[block]} ({block}). Слоев: {len(layers)}.'
                                   f' Выбран слой: {layer + 1}')
    if keyboard[pygame.K_2]:
        layer += 1
        print(layer)
        time.sleep(0.5)
        pygame.display.set_caption(f'Выбран блок: {tiles_names[block]} ({block}). Слоев: {len(layers)}.'
                                   f' Выбран слой: {layer + 1}')
    if keyboard[pygame.K_1]:
        layer -= 1
        print(layer)
        time.sleep(0.5)
        pygame.display.set_caption(f'Выбран блок: {tiles_names[block]} ({block}). Слоев: {len(layers)}.'
                                   f' Выбран слой: {layer + 1}')
    if keyboard[pygame.K_ESCAPE]:
        bar_vis = not bar_vis
        time.sleep(0.5)
    if keyboard[pygame.K_RIGHT]:
        sdvigx -= 10
    if keyboard[pygame.K_LEFT]:
        sdvigx += 10
    if keyboard[pygame.K_UP]:
        sdvigy += 10
    if keyboard[pygame.K_DOWN]:
        sdvigy -= 10
    if mouse[0] and 0 < x < 64 * 30 and 0 < y < 64 * 16:
        bx, by = (x - sdvigx) // 64, (y - sdvigy) // 64
        print(bx, by)
        if create_barrier:
            while len(barrier) < by + 1:
                barrier.append('.' * 31)
            barrier[by] = barrier[by].ljust(bx + 1, '.')
            blocks = list(barrier[by])
            blocks[bx] = 'z'
            barrier[by] = ''.join(blocks)
            pygame.display.set_caption(f'Выбран блок: {"Барьер"}.')
        elif create_player:
            player_pos = [bx * 64 + 32, by * 64 + 32]
        else:
            while len(layers[layer]) < by + 1:
                layers[layer].append('.' * 31)
            layers[layer][by] = layers[layer][by].ljust(bx + 1, '.')
            blocks = list(layers[layer][by])
            blocks[bx] = block
            layers[layer][by] = ''.join(blocks)
            pygame.display.set_caption(f'Выбран блок: {tiles_names[block]} ({block}). Слоев: {len(layers)}.'
                                       f' Выбран слой: {layer + 1}')
    if mouse[2] and 0 < x < 64 * 30 and 0 < y < 64 * 16:
        bx, by = (x - sdvigx) // 64, (y - sdvigy) // 64
        if not create_barrier:
            while len(layers[layer]) < by + 1:
                layers[layer].append('.' * 31)
            layers[layer][by] = layers[layer][by].ljust(bx + 1, '.')
            blocks = list(layers[layer][by])
            blocks[bx] = '.'
            layers[layer][by] = ''.join(blocks)
        else:
            while len(barrier) < by + 1:
                barrier.append('.' * 31)
            barrier[by] = barrier[by].ljust(bx + 1, '.')
            blocks = list(barrier[by])
            blocks[bx] = '.'
            barrier[by] = ''.join(blocks)
    map3 = map_generator.map_generator(screen, layers, barrier, create_barrier)


flag = True

while flag:
    clock.tick(60)
    screen.fill('black')
    for i in range(0, 100):
        pygame.draw.line(screen, (0, 255, 0), (0 + sdvigx, i * 64 + sdvigy), (64 * 100 + sdvigx, i * 64 + sdvigy), 1)
        pygame.draw.line(screen, (0, 255, 0), (i * 64 + sdvigx, 0 + sdvigy), (i * 64 + sdvigx, 64 * 100 + sdvigy), 1)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if create_map_flag and event.unicode in string.ascii_lowercase and event.unicode:
                if str(event.unicode) == 'z':
                    pygame.display.set_caption('Выбран блок: Барьер.')
                    create_barrier = not create_barrier
                elif str(event.unicode) == 'x':
                    pygame.display.set_caption('Выбран игрок')
                    create_player = not create_player
                elif str(event.unicode) in tiles_names.keys():
                    block = str(event.unicode)
                    print('!', block)
                else:
                    if tiles_names.get(block):
                        create_player = create_barrier = False
                        pygame.display.set_caption(f'Выбран блок: {tiles_names[block]} ({block}). Слоев: {len(layers)}.'
                                                   f' Выбран слой: {layer + 1}')
        if event.type == pygame.QUIT:
            flag = False
    if create_map_flag:
        create_map()
        map3.draw(sdvigx, sdvigy)
    pygame.draw.circle(screen, 'red', (player_pos[0] + sdvigx, player_pos[1] + sdvigy), 32)
    pygame.display.flip()

pygame.quit()
print('layers =', layers)
print('barrier =', barrier)
print(f'sdvigx, sdvigy = {sdvigx}, {sdvigy}')
print(f'player_pos = ({player_pos[0]}, {player_pos[1]})')
if f_name := input('Сохранить карту: '):
    with open('maps/' + f_name + '.py', 'w') as f:
        f.write('layers = ' + str(layers) + '\n')
        f.write('barrier = ' + str(barrier) + '\n')
        f.write(f'sdvigx, sdvigy = {sdvigx}, {sdvigy}' + '\n')
        f.write(f'player_pos = ({player_pos[0]}, {player_pos[1]})')
stop_game()
