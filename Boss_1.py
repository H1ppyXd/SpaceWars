import pygame
from load_methods import load_image
from Bullets import *
from sprite_groups import *
from random import randrange, choice


class Boss_1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(evil_sprites)
        self.hp = 1000
        self.image = load_image('boss_1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.atcs = ['20_shots', 'circle_bullet', 'bullet_wall', 'up_down']
        self.special = ['bullet_freeze', 'bullet_tree']
        self.now_atc = ''
        self.cooldown = 250
        self.cooldown_timer = 250
        self.wall_cooldown = -1

    def twenty_shots(self):
        x = self.rect.centerx
        prom = choice([150, 200, 250])
        y = self.rect.centery - prom
        for el in range(2):
            Bullet('crystal1.png', (x, y),
                   pygame.Vector2(-1, 0).normalize(), 5, enemy_bullets, size=(40, 40))
            Bullet('crystal1.png', (x, y),
                   pygame.Vector2(-2, -1).normalize(), 5, enemy_bullets, size=(30, 30))
            Bullet('crystal1.png', (x, y),
                   pygame.Vector2(-2, 1).normalize(), 5, enemy_bullets, size=(30, 30))
            Bullet('crystal1.png', (x, y),
                   pygame.Vector2(-2, 2).normalize(), 5, enemy_bullets, size=(30, 30))
            Bullet('crystal1.png', (x, y),
                   pygame.Vector2(-2, -2).normalize(), 5, enemy_bullets, size=(30, 30))
            Bullet('crystal1.png', (x, y),
                   pygame.Vector2(-2, 3).normalize(), 5, enemy_bullets, size=(30, 30))
            Bullet('crystal1.png', (x, y),
                   pygame.Vector2(-2, -3).normalize(), 5, enemy_bullets, size=(30, 30))

            Bullet('crystal1.png', (x, y),
                   pygame.Vector2(-2, -0.5).normalize(), 5, enemy_bullets, size=(30, 30))
            Bullet('crystal1.png', (x, y),
                   pygame.Vector2(-2, 0.5).normalize(), 5, enemy_bullets, size=(30, 30))
            y = self.rect.centery + prom

    def circle_bullet(self):
        x = self.rect.centerx
        prom = choice([150, 200, 250])
        y = self.rect.centery - prom
        for el in range(2):
            Circle_bullet('crystal1.png', (x, y),
                       pygame.Vector2(-1, 0).normalize(), 5, enemy_bullets, size=(50, 50 ))
            y = self.rect.centery + prom

    def bullet_wall(self):
        window = choice(range(20, 680, 10))
        for el in range(10, 800, 10):
            if el not in range(window, window + 110):
                Bullet('crystal1.png', (950, el),
                        pygame.Vector2(-1, 0).normalize(), 5, enemy_bullets, size=(30, 30))

    def up_down(self):
        pass

    def update(self, screen):
        if self.cooldown_timer == self.cooldown:
            while True:
                atc = choice(self.atcs)
                if atc != self.now_atc:
                    self.now_atc = atc
                    break
            if self.now_atc == '20_shots':
                self.twenty_shots()
                self.cooldown_timer = 0
            if self.now_atc == 'circle_bullet':
                self.circle_bullet()
                self.cooldown_timer = 0
            if self.now_atc == 'bullet_wall':
                self.cooldown_timer = 0
                self.wall_cooldown = 0
        else:
            self.cooldown_timer += 1

        if self.wall_cooldown != -1:
            if self.wall_cooldown in [100, 200, 300, 400, 500]:
                if self.now_atc == 'bullet_wall':
                    self.bullet_wall()
                    self.cooldown_timer = 0
                    self.wall_cooldown += 1
            elif self.wall_cooldown > 500:
                self.wall_cooldown = -1
            else:
                self.wall_cooldown += 1

        for bullet in hero_bullets:                         # Проверка попадания пули героя
            if pygame.sprite.collide_mask(self, bullet):
                self.hp -= 1
                bullet.kill()
