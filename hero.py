import pygame
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Hero(pygame.sprite.Sprite):
    image = load_image('Spaceshit.png')

    def __init__(self, sprite_group):
        super().__init__(sprite_group)
        Hero.image = pygame.transform.scale(Hero.image, (100, 50))
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 100
        self.rect.y = 250

    def update(self, x, y):
        self.rect = self.rect.move(x, y)