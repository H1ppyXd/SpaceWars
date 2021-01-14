import pygame
from load_methods import load_image
from Bullets import *
from sprite_groups import *
from random import randrange, choice
import globals

class Boss_1(pygame.sprite.Sprite):
    def __init__(self, hero):
        self.hero = hero
        super().__init__(boss_sprite)
        self.hp = 500
        self.image = load_image('boss_1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.atcs = ['20_shots', 'circle_bullet', 'bullet_wall', 'up_down']
        self.now_atc = ''
        self.cooldown = 250

        self.cooldown_timer = 0
        self.wall_cooldown = -1
        self.invicsibility = False
        self.deaf_timer = -1
        self.freeze_timer = -1

    def twenty_shots(self):
        x = self.rect.centerx
        prom = choice([150, 200, 250])
        y = self.rect.centery - prom
        for el in range(2):
            Bullet('enemy_bullet.png', (x, y),
                   pygame.Vector2(-1, 0).normalize(), 5, enemy_bullets, size=(20, 20))
            Bullet('enemy_bullet.png', (x, y),
                   pygame.Vector2(-2, -1).normalize(), 5, enemy_bullets, size=(20, 20))
            Bullet('enemy_bullet.png', (x, y),
                   pygame.Vector2(-2, 1).normalize(), 5, enemy_bullets, size=(20, 20))
            Bullet('enemy_bullet.png', (x, y),
                   pygame.Vector2(-2, 2).normalize(), 5, enemy_bullets, size=(20, 20))
            Bullet('enemy_bullet.png', (x, y),
                   pygame.Vector2(-2, -2).normalize(), 5, enemy_bullets, size=(20, 20))
            Bullet('enemy_bullet.png', (x, y),
                   pygame.Vector2(-2, 3).normalize(), 5, enemy_bullets, size=(20, 20))
            Bullet('enemy_bullet.png', (x, y),
                   pygame.Vector2(-2, -3).normalize(), 5, enemy_bullets, size=(20, 20))
            Bullet('enemy_bullet.png', (x, y),
                   pygame.Vector2(-2, -0.5).normalize(), 5, enemy_bullets, size=(20, 20))
            Bullet('enemy_bullet.png', (x, y),
                   pygame.Vector2(-2, 0.5).normalize(), 5, enemy_bullets, size=(20, 20))
            y = self.rect.centery + prom

    def circle_bullet(self):
        x = self.rect.centerx
        prom = choice([150, 200, 250])
        y = self.rect.centery - prom
        for el in range(2):
            Circle_bullet('enemy_bullet.png', (x, y),
                       pygame.Vector2(-1, 0).normalize(), 5, enemy_bullets, size=(30, 30))
            y = self.rect.centery + prom

    def bullet_wall(self):
        window = choice(range(20, 680, 10))
        for el in range(10, 800, 10):
            if el not in range(window, window + 110):
                Bullet('enemy_bullet.png', (950, el),
                        pygame.Vector2(-1, 0).normalize(), 5, enemy_bullets, size=(20, 20))

    def up_down(self):
        for el in range(0, 400, 10):
            Bullet('enemy_bullet.png', (el, 10), pygame.Vector2(0, 1).normalize(),
                   5, enemy_bullets, size=(20, 20))
        for el in range(400, 800, 10):
            Bullet('enemy_bullet.png', (el, 790), pygame.Vector2(0, -1).normalize(),
                   5, enemy_bullets, size=(20, 20))

    def update(self, screen):
        if self.deaf_timer != -1:
            self.deaf_timer += 1
        if self.cooldown_timer == self.cooldown and not self.invicsibility:
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
            if self.now_atc == 'bullet_wall' or self.now_atc == 'up_down':
                self.cooldown_timer = 0
                self.wall_cooldown = 0
        else:
            self.cooldown_timer += 1

        if self.wall_cooldown != -1:
            if self.wall_cooldown in [0, 200, 300, 400, 100]:
                if self.now_atc == 'bullet_wall':
                    self.bullet_wall()
                elif self.now_atc == 'up_down':
                    self.up_down()
                self.cooldown_timer = 0
                self.wall_cooldown += 1
            elif self.wall_cooldown > 400:
                self.wall_cooldown = -1
            else:
                self.wall_cooldown += 1

        for bullet in hero_bullets:                         # Проверка попадания пули героя
            if pygame.sprite.collide_mask(self, bullet) and not self.invicsibility and \
                    self.hp != 0 and self.hp != 50 and self.hp != 100 and self.hp != 150:
                self.hp -= 1
                bullet.kill()

        if self.hp == 0 and not self.invicsibility and self.cooldown_timer == 249:
            self.invicsibility = True
            self.wall_cooldown = -1
            Super_bullet('enemy_bullet.png', self.rect.center,
                        pygame.Vector2(-1, 0).normalize(), 1, enemy_bullets, size=(70, 70))
            Bullet('enemy_bullet.png', (self.rect.centerx + 100, self.rect.centery - 370),
                        pygame.Vector2(-1, 0).normalize(), 1, enemy_bullets, size=(20, 20))
            Bullet('enemy_bullet.png', (self.rect.centerx + 100, self.rect.centery + 370),
                        pygame.Vector2(-1, 0).normalize(), 1, enemy_bullets, size=(20, 20))
            self.deaf_timer = 0

        if (self.hp == 50 or self.hp == 100 or self.hp == 150) \
                and not self.invicsibility and self.cooldown_timer == 249:
            self.invicsibility = True
            self.freeze_timer = 0

        if self.freeze_timer < 50 and self.freeze_timer != -1:
            Freeze_bullets('enemy_bullet.png', self.rect.center,
                        pygame.Vector2(randrange(-7, -1), randrange(-5, 6)).normalize(),
                           randrange(3, 5), boss_bullets, size=(20, 20))
        elif self.freeze_timer == 200:
            boss_bullets.update(screen, 1)
        elif self.freeze_timer == 300:
            boss_bullets.update(screen, 2)
        elif self.freeze_timer == 400:
            self.invicsibility = False
            self.hp -= 1
            self.freeze_timer = -1
            self.cooldown_timer = 0

        if self.freeze_timer != -1:
            self.freeze_timer += 1


        if self.deaf_timer == 1300:
            globals.now_boss_flag = False

        # Добавление новых врагов
            globals.snipers.append('sniper_shot')
            globals.snipers.remove(globals.snipers[0])
            globals.enemys.append('five_shotes')
            globals.enemys.remove(globals.enemys[0])
            globals.enem_to += 50
            self.hero.hp += 1
            self.kill()
            globals.flag += 1
