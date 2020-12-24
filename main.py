import pygame

# Сделать Класс Героя

class Hero:
    def __init__(self, name):
        self.name = name


class Enemy:
    def __init__(self):
        pass

pygame.init()
size = wigth, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SpaceWars')

evil_sprites = pygame.sprite.Group()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
