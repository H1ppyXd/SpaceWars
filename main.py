import pygame
import hero as h
from Enemy import Enemy
from sprite_groups import *
from random import sample
from Bullets import Bullet_wall

pygame.init()
size = wigth, height = 1000, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SpaceWars')


Hero = h.Hero(good_sprites)

good_sprites.add(Hero)

clock = pygame.time.Clock()
t = 300
speed = 5
x, y = 0, 0

running = True
wall_flag = True
while running:
    clock.tick(75)
    keys = pygame.key.get_pressed()
    if (t == 300 and len(evil_sprites) < 5) or len(evil_sprites) == 0:
        Enemy('ship.png', True, shooting_type=sample(['front_shot', 'triple_shot', 'five_shotes', 'giant_shot'], 1))
        t = 0
    else:
        t += 1
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

    screen.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x += (keys[pygame.K_d] - keys[pygame.K_a]) * .5
    y += (keys[pygame.K_s] - keys[pygame.K_w]) * .5

    Hero.update(x, y, enemy_bullets)
    if Hero.rect.x > 800 and wall_flag:
        for el in range(-30, 800, 10):
            Bullet_wall('crystal1.png', (950, el),
                   pygame.Vector2(0, -1).rotate(-90).normalize(), 10, size=(30, 30))
        wall_flag = False
    elif not wall_flag and Hero.rect.x < 800:
        wall_flag = True
    evil_sprites.update(screen)
    enemy_bullets.update(screen)
    evil_sprites.draw(screen)
    enemy_bullets.draw(screen)
    good_sprites.draw(screen)
    pygame.display.flip()
