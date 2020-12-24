import pygame

# Сделать Класс Героя
class Hero:
    def __init__(self, name):
        self.name = name


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
