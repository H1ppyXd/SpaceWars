import pygame


class Enemy:
    def __init__(self):
        pass

pygame.init()
size = wigth, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SpaceWars')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
