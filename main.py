import pygame


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
