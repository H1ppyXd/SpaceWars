import pygame
from load_methods import load_image
from sprite_groups import *
from Bullets import Bullet

class Circle(pygame.sprite.Sprite):
    def __init__(self, color, rad=75):
        super().__init__(circles)
        self.hp = 10
        self.rad = rad
        self.color = color
        self.image = load_image('circle_surf.png')
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, self.color, self.rect.center, self.rad, width=3)

    def update(self):
        if self.color == 'skyblue':
            for group in [enemy_bullets, stop_bullets, boss_bullets, guided_bullet, wall_bullets, bullet_wall]:
                for bullet in group:
                    if pygame.sprite.collide_mask(self, bullet):
                        bullet.kill()
        else:
            for bullet in hero_bullets:
                if pygame.sprite.collide_mask(self, bullet):
                    if self.color == 'yellow':
                        napr = -1 * bullet.naprevl
                        center = bullet.rect.center
                        s = bullet.speed
                        bullet.kill()
                        Bullet('enemy_bullet.png', center, napr, s, enemy_bullets, size=(25, 25))
                    elif self.color != 'black':
                        bullet.kill()
                        self.hp -= 1
        if self.hp <= 0:
            self.kill()