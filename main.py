import pygame
import hero as h


pygame.init()
size = wigth, height = 1000, 800
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SpaceWars')

evil_sprites = pygame.sprite.Group()
good_sprites = pygame.sprite.Group()

Hero = h.Hero(good_sprites)
good_sprites.add(Hero)

clock = pygame.time.Clock()

speed = 5
x, y = 0, 0

running = True
while running:
    clock.tick(75)
    keys = pygame.key.get_pressed()

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

    Hero.update(x, y)

    good_sprites.draw(screen)
    pygame.display.flip()
