import pygame_gui
import pygame
import hero as h
import math
import random

import globals
from Enemy import *
from sprite_groups import *
from random import sample, choice
from Bullets import Bullet, Bullet_wall
from Boss_1 import Boss_1

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.randint(-3, -1)
        self.dy = random.randint(-1, 1)

    def moving(self):
        self.x += self.dx
        self.y += self.dy

    def dot_pos(self):
        return self.x, self.y


data = [Dot(random.randint(0, 1200), random.randint(0, 800)) for i in range(50)]


def game_over():
    pass


def background():
    for i in data:
        if i.x < 0:
            i.x = 1200
        if i.y < 0:
            i.y = 800
        elif i.y > 800:
            i.y = 0
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), (i.x, i.y, 3, 3))
        i.moving()


def check_player_pos(x, y):
    if Hero.rect.x > wigth:
        x = -1
        Hero.dx = 0
    if Hero.rect.x < 0:
        x = 1
        Hero.dx = 0
    if Hero.rect.y > height - 45:
        y = -1
        Hero.dy = 0
    if Hero.rect.y < 0:
        y = 1
        Hero.dy = 0
    return x, y


def main_menu():
    manager = pygame_gui.UIManager(size)

    f1 = pygame.font.Font(None, 72)
    text1 = f1.render('SpaceWars', True,
                      (255, 255, 255))

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

    leaderboard = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((wigth // 2 - 100, height // 2 + 45), (200, 50)),
        text='leaderboard',
        manager=manager
    )

    exit_btn = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((wigth // 2 - 100, height // 2 + 105), (200, 50)),
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
        background()
        manager.update(time_delta)
        manager.draw_ui(screen)
        screen.blit(text1, (wigth // 2 - 130, 100))
        pygame.display.flip()


def option():
    manager = pygame_gui.UIManager(size)
    if globals.movement == 0:
        st_op = 'Arcade movement'
    elif globals.movement == 1:
        st_op = 'Realistic movement'
    elif globals.movement == 2:
        st_op = 'Simulation movement'
    difficulty = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
        options_list=['Arcade movement', 'Realistic movement', 'Simulation movement'],
        starting_option=st_op,
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
                        globals.nem_movement(0)
                    elif event.text == 'Realistic movement':
                        globals.nem_movement(1)
                    else:
                        globals.nem_movement(2)
            manager.process_events(event)
        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.flip()


def game():
    t = 300
    global_timer = 0
    t_flag = True
    x, y = 0, 0
    wall_flag = True
    running = True
    while running:
        movement = globals.movement
        now_boss_flag = globals.now_boss_flag
        clock.tick(75)
        keys = pygame.key.get_pressed()
        if movement == 0:
            x = (keys[pygame.K_d] * 5 - keys[pygame.K_a] * 5)
            y = (keys[pygame.K_s] * 5 - keys[pygame.K_w] * 5)
            x, y = check_player_pos(x, y)
            Hero.update(x, y, screen)

        if movement == 1:
            if keys[pygame.K_d] == 0 and keys[pygame.K_a] == 0:
                if x > 0.1:
                    x -= 0.1
                else:
                    x += 0.1

            if keys[pygame.K_w] == 0 and keys[pygame.K_s] == 0:
                if y > 0.1:
                    y -= 0.1
                else:
                    y += 0.1

            x += (keys[pygame.K_d] - keys[pygame.K_a]) * .5
            y += (keys[pygame.K_s] - keys[pygame.K_w]) * .5
            x, y = check_player_pos(x, y)
            Hero.update(x, y, screen)

        if movement == 2:
            sin_a = math.sin(Hero.angle)
            cos_a = math.cos(Hero.angle)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                Hero.dx += 0.1 * cos_a
                Hero.dy += 0.1 * sin_a
            if keys[pygame.K_LEFT]:
                Hero.angle -= 0.03
                Hero.pov += 1
            if keys[pygame.K_RIGHT]:
                Hero.angle += 0.03
                Hero.pov -= 1
            Hero.rect.x += Hero.dx
            Hero.rect.y += Hero.dy
            pygame.display.flip()
            x, y = check_player_pos(x, y)
            Hero.update(x, y, screen)

        if keys[pygame.K_SPACE] != 0:
            if globals.movement == 2:
                Hero.shot_by_line()
            else:
                Hero.shot()

        if not now_boss_flag:
            if global_timer == 10000:
                globals.now_boss_flag = True
                evil_sprites.empty()
                snipers.empty()
                enemy_bullets.empty()
                Boss_1()
                global_timer = 0
            elif (t == 300 and len(evil_sprites) + len(snipers) < 5) or len(evil_sprites) + len(snipers) == 0:
                c = choice([0, 1, 2, 3])
                if c == 0:
                    Sniper('ship.png', True, snipers, shooting_type=choice(['sniper_shot', 'cline_shot']))
                else:
                    Enemy('ship.png', True, evil_sprites,
                          shooting_type=choice(['front_shot', 'triple_shot', 'five_shotes', 'giant_shot']))
                t = 0
            elif t == 300:
                t = 0
            else:
                t += 1
                global_timer += 1


        screen.fill(pygame.Color('black'))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(-1)
            if keys[pygame.K_ESCAPE] == 1:
                option()

        if movement == 2:
            pygame.draw.line(screen, pygame.Color(255, 0, 0), (Hero.rect.centerx, Hero.rect.centery - 5),
                             (Hero.rect.centerx + 800 * math.cos(Hero.angle),
                              Hero.rect.centery + 800 * math.sin(Hero.angle) - 5))

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
        boss_sprite.update(screen)
        boss_bullets.update(screen, 0)

        #  Чтобы убрать фон в игре закомментируй это
        background()
        boss_bullets.draw(screen)
        snipers.draw(screen)
        enemy_bullets.draw(screen)
        hero_bullets.draw(screen)
        evil_sprites.draw(screen)
        boss_sprite.draw(screen)
        good_sprites.draw(screen)



        pygame.display.flip()


pygame.init()
movement = globals.movement
size = wigth, height = 1000, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SpaceWars')
Hero = h.Hero(good_sprites)

good_sprites.add(Hero)
clock = pygame.time.Clock()
main_menu()