import pygame
import pygame_widgets
from pygame_widgets.button import Button

def draw(screen, kills=0):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Вы проиграли", True, (255, 255, 255))
    score = font.render(f'Убито врагов: {kills}', True, (255, 255, 255))
    button_menu = Button(screen, 630, 700, 650, 150, text='Меню', fontSize=150, inactiveColour=(255, 255, 255),
                         hoverColour=(255, 255, 255), radius=20, onClick=lambda: menu)
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    score_x, score_y = text_x, text_y + 60
    screen.blit(text, (text_x, text_y))
    screen.blit(score, (score_x, score_y))
    pygame.display.update()
    run = True

    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()

        # Now
        pygame_widgets.update(events)

        # Instead of
        button_menu.listen(events)
        button_menu.draw()

        pygame.display.update()

def menu():
    pass

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

