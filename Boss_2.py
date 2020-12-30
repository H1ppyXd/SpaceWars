import pygame
from load_methods import load_image
from Bullets import *
from sprite_groups import *
from random import randrange, choice
import globals



class Boss_2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(boss_sprite)
        self.hp = 10
        self.image = load_image('boss_2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 275
        self.atcs = ['20_shots', 'circle_bullet', 'bullet_wall', 'up_down']
        self.special = ['bullet_freeze', 'bullet_tree']
        self.now_atc = ''
        self.cooldown = 250
        self.cooldown_timer = 0

    def update(self, screen):
        if self.cooldown_timer == self.cooldown:
            Bullet('enemy_bullet.png', self.rect.center,
                   pygame.Vector2(-1, 0).normalize(), 5, enemy_bullets, size=(20, 20))
            self.cooldown_timer = 0
        else:
            self.cooldown_timer += 1

        for bullet in hero_bullets:
            if pygame.sprite.collide_mask(self, bullet):
                bullet.kill()
                self.hp -= 1
        if self.hp <= 0:
            self.kill()
            globals.now_boss_flag = False
