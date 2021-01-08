import pygame
from load_methods import load_image
from Bullets import *
from sprite_groups import *
import globals
from random import randrange, choice


class Base_Enemy(pygame.sprite.Sprite):

    def __init__(self, name, flag_moving_left, group, speed=1, size=(0, 0), hp=3,
                 shooting_type='front_shot', cooldown=210):

        super().__init__(group)                     # Добавление спрайта в группы
        self.flag_moving_left = flag_moving_left    # Флаг движения вперед
        self.go_down_flag = choice([True, False])   # Флаг движения вверх/вниз
        self.hp = hp                                # Количество Hp
        self.speed = speed                          # Скорость движения
        self.shooting_type = shooting_type
        self.direction = pygame.Vector2(1, 0)       # Направление стрельбы
        self.image = load_image(name)                                   # Создание спрайта
        self.image = pygame.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect()
        if size != (0, 0):
            self.image = pygame.transform.scale(self.image, size)
        self.rect.x = 1000
        self.rect.y = randrange(0, 600)
        self.stop_pos = randrange(600, 900, 5)

        self.pos = pygame.Vector2(self.rect.center)
        self.cooldown = cooldown
        self.cooldown_timer = 0

    def update(self, screen):
        if not self.flag_moving_left:                          # Движение
            if self.go_down_flag:
                self.rect.y += self.speed
            else:
                self.rect.y -= self.speed
        else:
            self.rect.x -= self.speed
            if self.rect.x <= self.stop_pos:
                self.flag_moving_left = False

        if not screen.get_rect().contains(self.rect):       # Проверка выхода за пределы экрана
            if self.go_down_flag:
                self.go_down_flag = False
            else:                                       # Изменение направления движения
                self.go_down_flag = True

        for bullet in hero_bullets:                         # Проверка попадания пули героя
            if pygame.sprite.collide_mask(self, bullet):
                self.hp -= 1
                bullet.kill()
        if self.hp <= 0:
            self.kill()
            globals.enemy_kill()


class Enemy(Base_Enemy):
    def front_shot(self):                                        # Создание пули
        Bullet('enemy_bullet.png', self.rect.center,
               pygame.Vector2(-1, 0).normalize(), 5, enemy_bullets, size=(25, 25))

    def triple_shot(self):
        self.front_shot()
        Bullet('enemy_bullet.png', self.rect.center,
               pygame.Vector2(-2, -1).normalize(), 5, enemy_bullets, size=(25, 25))
        Bullet('enemy_bullet.png', self.rect.center,
               pygame.Vector2(-2, 1).normalize(), 5, enemy_bullets, size=(25, 25))

    def five_shotes(self):
        self.triple_shot()
        Bullet('enemy_bullet.png', self.rect.center,
               pygame.Vector2(-2, 2).normalize(), 5, enemy_bullets, size=(25, 25))
        Bullet('enemy_bullet.png', self.rect.center,
               pygame.Vector2(-2, -2).normalize(), 5, enemy_bullets, size=(25, 25))

    def giant_shot(self):
        Giant_bullet('enemy_bullet.png', self.rect.center,
               pygame.Vector2(-1, 0).normalize(), 3, enemy_bullets, size=(70, 70))

    def update(self, screen):
        super().update(screen)        # Выстрел/перезарядка
        if self.cooldown_timer == self.cooldown:
            self.cooldown_timer = 0
            if self.shooting_type == 'front_shot':
                self.front_shot()
            if self.shooting_type == 'triple_shot':
                self.triple_shot()
            if self.shooting_type == 'five_shotes':
                self.five_shotes()
            if self.shooting_type == 'giant_shot':
                self.giant_shot()
        else:
            self.cooldown_timer += 1


class Sniper(Base_Enemy):
    def shot(self, Hero):
        Bullet('enemy_bullet.png', self.rect.center,
                pygame.Vector2(Hero.centerx - self.rect.centerx,
                                Hero.centery - self.rect.centery).normalize(), 7, enemy_bullets, size=(15, 15))

    def sniper_shot(self, Hero):
        Bullet('enemy_bullet.png', self.rect.center,
                pygame.Vector2(Hero.centerx - self.rect.centerx,
                                Hero.centery - self.rect.centery).normalize(), 7, enemy_bullets, size=(15, 15))

    def cline_shot(self, Hero):
        self.sniper_shot(Hero)
        Bullet('enemy_bullet.png', (self.rect.centerx + 10, self.rect.centery + 10),
                pygame.Vector2(Hero.centerx - self.rect.centerx + 10,
                                Hero.centery - self.rect.centery + 10).normalize(), 7, enemy_bullets, size=(15, 15))
        Bullet('enemy_bullet.png', (self.rect.centerx + 10, self.rect.centery - 10),
                pygame.Vector2(Hero.centerx - self.rect.centerx - 10,
                                Hero.centery - self.rect.centery - 10).normalize(), 7, enemy_bullets, size=(15, 15))
        Bullet('enemy_bullet.png', (self.rect.centerx + 20, self.rect.centery + 20),
                pygame.Vector2(Hero.centerx - self.rect.centerx + 20,
                                Hero.centery - self.rect.centery + 20).normalize(), 7, enemy_bullets, size=(15, 15))
        Bullet('enemy_bullet.png', (self.rect.centerx + 20, self.rect.centery - 20),
                pygame.Vector2(Hero.centerx - self.rect.centerx - 20,
                                Hero.centery - self.rect.centery - 20).normalize(), 7, enemy_bullets, size=(15, 15))

    def update(self, screen, hero):
        super().update(screen)
        self.cooldown_timer += 1
        if self.shooting_type == 'shot':
            if self.cooldown_timer == self.cooldown:
                self.sniper_shot(hero.rect)
                self.cooldown_timer = -1
        elif self.shooting_type == 'sniper_shot':
            if self.cooldown_timer == self.cooldown:
                self.sniper_shot(hero.rect)
            elif self.cooldown_timer == self.cooldown + 3 or self.cooldown_timer == self.cooldown + 6 or\
                    self.cooldown_timer == self.cooldown + 9:
                self.sniper_shot(hero.rect)
            elif self.cooldown_timer == self.cooldown + 12:
                self.sniper_shot(hero.rect)
                self.cooldown_timer = -1
        elif self.shooting_type == 'cline_shot':
            if self.cooldown_timer == self.cooldown:
                self.cline_shot(hero.rect)
                self.cooldown_timer = -1


