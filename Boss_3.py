import pygame
from load_methods import load_image
from Bullets import *
from sprite_groups import *
from random import randrange, choice
import globals


class Boss_3(pygame.sprite.Sprite):
    def __init__(self, hero):
        super().__init__(boss_sprite)
        self.hp = 1000
        self.atcs = []
        self.invicsibility = False
        self.hero = hero
        self.image = load_image('Boss_3.png')
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 300
        self.color = 'green'
        self.circle = Circle(self.color)
        self.circle.rect.center = self.rect.center

        self.bullet_shield = 500
        self.tp = 0

        self.zone = Zona(self.rect.center)

    def update(self, screen):
        if self.tp == 2000:
            c = (randrange(500, 851), randrange(100, 701))
            self.rect.center = c
            self.zone.rect.center = c
            self.circle.rect.center = c
            self.tp = 0
        else:
            self.tp += 1

        if globals.movement == 0:
            if self.color == 'red':
                vector = pygame.Vector2(self.rect.centerx - self.hero.rect.centerx,
                               self.rect.centery - self.hero.rect.centery).normalize()
                pos = pygame.Vector2(self.hero.rect.center)
                pos += vector * 2
                self.hero.rect.center = pos
            elif self.color == 'green':
                globals.speed = 3
            elif self.color == 'blue':
                globals.speed = 5
                globals.uprav = False
            else:
                globals.uprav = True

        if not self.invicsibility:
            for bullet in hero_bullets:
                if not self.invicsibility:
                    if pygame.sprite.collide_mask(self, bullet):
                        bullet.kill()
                        self.hp -= 1
            if self.hp <= 0:
                self.kill()


class Zona(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__(zone)

        self.image = load_image('zona.png')
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.center = center


class Circle(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__(circles)
        self.hp = 10
        self.color = color
        self.image = load_image('circle_surf.png')
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, self.color, self.rect.center, 75, width=3)

    def update(self):
        for bullet in hero_bullets:
            if pygame.sprite.collide_mask(self, bullet):
                bullet.kill()
                self.hp -= 1
        if self.hp <= 0:
            self.kill()