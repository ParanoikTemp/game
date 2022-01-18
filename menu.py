import pygame
import pygame_widgets
from pygame_widgets.button import Button

pygame.font.init()

font = pygame.font.SysFont('arial', 60)

pygame.init()
win = pygame.display.set_mode((64 * 30, 64 * 16))
button = Button(win, 700, 300, 650, 150, text="Начать игру", fontSize=150, inactiveColour=(200, 50, 0),
                hoverColour=(150, 0, 0), radius=20, onClick=lambda: keks())

button_instruction = Button(win, 775, 600, 500, 150, text="Инструкция", fontSize=100, inactiveColour=(200, 50, 0),
                            hoverColour=(150, 0, 0), radius=20, onClick=lambda: keks())

run = True
what = 0


def keks():
    global what
    what = 1


def instruction():
    global button_instruction, button
    button_instruction.hide()
    button.hide()
    with open('instruction.txt', 'r', encoding="utf8") as f:
        read_txt = f.readlines()
    for i, j in enumerate(read_txt):
        text = font.render(j[:-1], True, 'black')
        win.blit(text, (160, 100 + i * 300))


while run:
    win.fill((255, 255, 255))
    events = pygame.event.get()
    if what == 1:
        instruction()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    # Now
    pygame_widgets.update(events)

    # Instead of
    button.listen(events)
    button.draw()
    pygame.display.flip()
