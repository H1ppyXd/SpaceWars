import pygame
import load_methods


class Hero(pygame.sprite.Sprite):
    image = load_methods.load_image('Spaceshit.png')

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