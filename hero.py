import pygame
import load_methods
from sprite_groups import hero_bullets
from Bullets import Bullet

class Hero(pygame.sprite.Sprite):
    image = load_methods.load_image('Hero_ship.png')

    def __init__(self, sprite_group, hp=3):
        super().__init__(sprite_group)
        Hero.image = pygame.transform.scale(Hero.image, (75, 50))
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 100
        self.rect.y = 250

    #     self.cooldown = 100
    #     self.cooldown_timer = 100

    # def shot(self):
    #     if self.cooldown_timer == self.cooldown:
    #         Bullet('crystal1.png', self.rect.center,
    #                pygame.Vector2(1, 0).normalize(), 5, hero_bullets, size=(40, 40))
    #         self.cooldown_timer = 0

    def update(self, x, y, group):
        # if self.cooldown_timer != self.cooldown:
        #     self.cooldown_timer += 1
        self.rect = self.rect.move(x, y)
        for bullet in group:
            if pygame.sprite.collide_mask(self, bullet):
                self.kill()