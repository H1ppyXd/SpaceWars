import pygame_gui
import pygame
import hero as h

from Enemy import *
from sprite_groups import *
from random import sample, choice
from Bullets import Bullet, Bullet_wall


def game_over():
    pass


def check_player_pos(x, y):
    if Hero.rect.x > wigth:
        x = -1
    if Hero.rect.x < 0:
        x = 1
    if Hero.rect.y > height - 45:
        y = -1
    if Hero.rect.y < 0:
        y = 1
    return x, y


def main_menu():
    manager = pygame_gui.UIManager(size)

    start_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((wigth // 2 - 100, height // 2 - 75), (200, 50)),
        text='New Game',
        manager=manager
    )

    options = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((wigth // 2 - 100, height // 2 - 15), (200, 50)),
        text='Options',
        manager=manager
    )

    exit_btn = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((wigth // 2 - 100, height // 2 + 45), (200, 50)),
        text='Exit',
        manager=manager
    )

    while True:
        screen.fill(pygame.Color('black'))
        time_delta = clock.tick(75) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(-1)
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == start_button:
                        game()
                    if event.ui_element == options:
                        option()
                    if event.ui_element == exit_btn:
                        exit(-1)
            manager.process_events(event)
        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.flip()


def option():
    global movement
    manager = pygame_gui.UIManager(size)
    difficulty = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
        options_list=['Arcade movement', 'Realistic movement'],
        starting_option='Arcade movement',
        relative_rect=pygame.Rect((wigth // 2 - 100, height // 2 + 45), (200, 50)),
        manager=manager
    )
    running = True
    while running:
        keys = pygame.key.get_pressed()
        screen.fill(pygame.Color('black'))
        time_delta = clock.tick(75) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(-1)
            if keys[pygame.K_ESCAPE] == 1:
                running = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    if event.text == 'Arcade movement':
                        movement = 0
                    else:
                        movement = 1
                    print(movement)
            manager.process_events(event)
        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.flip()


def game():
    global movement
    t = 300
    x, y = 0, 0
    wall_flag = True
    running = True
    while running:
        clock.tick(75)
        keys = pygame.key.get_pressed()
        if movement == 1:
            if keys[pygame.K_d] == 0 and keys[pygame.K_a] == 0:
                if x > 0:
                    x -= 0.1
                else:
                    x += 0.1

            if keys[pygame.K_w] == 0 and keys[pygame.K_s] == 0:
                if y > 0:
                    y -= 0.1
                else:
                    y += 0.1
            x += (keys[pygame.K_d] - keys[pygame.K_a]) * .5
            y += (keys[pygame.K_s] - keys[pygame.K_w]) * .5
        else:
            x = (keys[pygame.K_d] * 5 - keys[pygame.K_a] * 5)
            y = (keys[pygame.K_s] * 5 - keys[pygame.K_w] * 5)

        x, y = check_player_pos(x, y)

        if keys[pygame.K_SPACE] != 0:
            Hero.shot()

        if (t == 300 and len(evil_sprites) + len(snipers) < 5) or len(evil_sprites) + len(snipers) == 0:
            c = choice([0, 1])
            if c == 0:
                Enemy('ship.png', True, evil_sprites,
                      shooting_type=choice(['front_shot', 'triple_shot', 'five_shotes', 'giant_shot']))
            else:
                Sniper('ship.png', True, snipers, shooting_type=choice(['sniper_shot', 'cline_shot']))
            t = 0

        else:
            t += 1

        screen.fill(pygame.Color('black'))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(-1)
            if keys[pygame.K_ESCAPE] == 1:
                option()

        Hero.update(x, y, enemy_bullets)

        if Hero.rect.x > 750 and wall_flag:
            for el in range(-30, 750, 10):
                Bullet_wall('crystal1.png', (950, el),
                            pygame.Vector2(-1, 0).normalize(), 10, enemy_bullets, size=(30, 30))
            wall_flag = False
        elif not wall_flag and Hero.rect.x < 750:
            wall_flag = True

        snipers.update(screen, Hero)
        evil_sprites.update(screen)
        enemy_bullets.update(screen)
        hero_bullets.update(screen)

        snipers.draw(screen)
        evil_sprites.draw(screen)
        enemy_bullets.draw(screen)
        hero_bullets.draw(screen)

        good_sprites.draw(screen)
        pygame.display.flip()


pygame.init()
movement = 0
size = wigth, height = 1000, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SpaceWars')
Hero = h.Hero(good_sprites)

good_sprites.add(Hero)
clock = pygame.time.Clock()
main_menu()