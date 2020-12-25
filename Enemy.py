import pygame
from load_methods import load_image
from Bullets import *
from sprite_groups import *
from random import randrange

class Enemy(pygame.sprite.Sprite):                              # Тестовый класс врага

    # Передаваемые значения: название спрайта, группы спрайтов, скорость движения, размер спрайта, жизни, тип стрельбы, кулдаун.
    def __init__(self, name, flag_moving_left, speed=1, size=(0, 0), hp=3, shooting_type='front_shot', cooldown=210):

        super().__init__(evil_sprites)                     # Добавление спрайта в группы
        self.flag_moving_left = flag_moving_left    # Флаг движения вперед
        self.go_down_flag = True                    # Флаг движения вверх/вниз
        self.hp = hp                                # Количество Hp
        self.angle = 90                             # Угол стрельбы
        self.speed = speed                          # Скорость движения
        self.shooting_type = shooting_type[0]
        self.direction = pygame.Vector2(1, 0)       # Направление стрельбы
        self.image = load_image(name)                                   # Создание спрайта
        self.image = pygame.transform.rotate(self.image, self.angle)
        if size != (0, 0):
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = randrange(0, 600)
        self.stop_pos = randrange(600, 900, 5)

        self.pos = pygame.Vector2(self.rect.center)
        self.cooldown = cooldown
        self.cooldown_timer = 0               # Таймер перезарядки

    def front_shot(self):                                        # Создание пули
        Bullet('crystal1.png', self.rect.center,
               pygame.Vector2(0, -1).rotate(-self.angle).normalize(), 5, size=(40, 40))

    def triple_shot(self):
        self.front_shot()
        Bullet('crystal1.png', self.rect.center,
               pygame.Vector2(-1, -2).rotate(-self.angle).normalize(), 5, size=(30, 30))
        Bullet('crystal1.png', self.rect.center,
               pygame.Vector2(1, -2).rotate(-self.angle).normalize(), 5, size=(30, 30))

    def five_shotes(self):
        self.triple_shot()
        Bullet('crystal1.png', self.rect.center,
               pygame.Vector2(-1, -4).rotate(-self.angle).normalize(), 5, size=(30, 30))
        Bullet('crystal1.png', self.rect.center,
               pygame.Vector2(1, -4).rotate(-self.angle).normalize(), 5, size=(30, 30))

    def giant_shot(self):
        Giant_bullet('crystal1.png', self.rect.center, self.angle,
               pygame.Vector2(0, -1).rotate(-self.angle).normalize(), 5, size=(90, 90))

    def update(self, screen):

        if self.cooldown_timer == self.cooldown:         # Выстрел/перезарядка
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

        # for bullet in hero_bullets:                         # Проверка попадания пули героя
        #     if pygame.sprite.collide_mask(self, bullet):
        #         self.hp -= 1
        #         bullet.kill()
        # if self.hp == 0:
        #     self.kill()