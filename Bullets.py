import pygame
from load_methods import load_image
from sprite_groups import *
from random import randrange


class Bullet(pygame.sprite.Sprite):     # Класс пули

    # Переменные: название спрайта, центр пули (начальная точка), направление движения, скорость пули,
    # группы спрайтов, размер пули.

    def __init__(self, name, center, naprevl, speed, group, size=(0, 0)):

        super().__init__(group)         # Добавление пули в группу

        self.naprevl = naprevl
        self.speed = speed

        self.image = load_image(name)
        self.size = size
        self.center = center
        if size != (0, 0):
            self.image = pygame.transform.scale(self.image, size)                               # Создание спрайта
        self.rect = self.image.get_rect(center=center)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = pygame.Vector2(self.rect.center)

    def update(self, screen):

        self.pos += self.naprevl * self.speed       # Движение пули
        self.rect.center = self.pos

        if not screen.get_rect().contains(self.rect):       # Проверка выхода за экран
            self.kill()


class Giant_bullet(Bullet):
    def __init__(self, name, center, naprevl, speed, group, size=(0, 0)):
        super().__init__(name, center, naprevl, speed, group, size)
        self.timer = 0

    def update(self, screen):
        super().update(screen)
        if self.timer == 30:
            self.timer = 0
            Small_bullet('enemy_bullet.png', self.rect.center,
                   pygame.Vector2(-2, -1).normalize(), 1, enemy_bullets, size=(25, 25))
            Small_bullet('enemy_bullet.png', self.rect.center,
                   pygame.Vector2(-2, 1).normalize(), 1, enemy_bullets, size=(25, 25))
        else:
            self.timer += 1


class Super_bullet(Bullet):
    def __init__(self, name, center, naprevl, speed, group, size=(0, 0)):
        super().__init__(name, center, naprevl, speed, group, size)
        self.timer = 0

    def update(self, screen):
        super().update(screen)
        if self.timer == 70:
            self.timer = 0
            s = self.rect.centerx - 50
            S_Giant_bullet('enemy_bullet.png', self.rect.center,
                         pygame.Vector2(-1, -1).normalize(), 1, enemy_bullets, size=(25, 25))
            S_Giant_bullet('enemy_bullet.png', self.rect.center,
                         pygame.Vector2(-1, 1).normalize(), 1, enemy_bullets, size=(25, 25))

        else:
            self.timer += 1

class S_Giant_bullet(Bullet):
    def __init__(self, name, center, naprevl, speed, group, size=(0, 0)):
        super().__init__(name, center, naprevl, speed, group, size)
        self.timer = 0

    def update(self, screen):
        super().update(screen)
        if self.timer == 70:
            self.timer = 0
            Small_bullet('enemy_bullet.png', self.rect.center,
                   pygame.Vector2(1, -0.5).normalize(), 1, enemy_bullets, size=(20, 20), timer_to=240)
            Small_bullet('enemy_bullet.png', self.rect.center,
                   pygame.Vector2(1, 0.5).normalize(), 1, enemy_bullets, size=(20, 20), timer_to=240)
            Small_bullet('enemy_bullet.png', self.rect.center,
                   pygame.Vector2(0, -1).normalize(), 1, enemy_bullets, size=(20, 20), timer_to=150)
            Small_bullet('enemy_bullet.png', self.rect.center,
                   pygame.Vector2(0, -1).normalize(), 1, enemy_bullets, size=(20, 20), timer_to=150)
        else:
            self.timer += 1

class Small_bullet(Bullet):
    def __init__(self, name, center, naprevl, speed, group, size=(0, 0), timer_to=125):
        super().__init__(name, center, naprevl, speed, group, size)
        self.timer = 0
        self.timer_to = timer_to

    def update(self, screen):
        super().update(screen)
        if self.timer == self.timer_to:
            self.kill()
        else:
            self.timer += 1


class Bullet_wall(Bullet):
    def update(self, screen):
        super().update(screen)
        if self.rect.x < 800:
            self.kill()


class Circle_bullet(Bullet):
    def __init__(self, name, center, naprevl, speed, group, size=(0, 0), x=400):
        super().__init__(name, center, naprevl, speed, group, size)
        self.x = x

    def update(self, screen):
        super().update(screen)
        if self.rect.centerx == self.x:
            Bullet('enemy_bullet.png', self.rect.center,
                   pygame.Vector2(-1, 0).normalize(), 5, enemy_bullets, size=(25, 25))
            Bullet('enemy_bullet.png', self.rect.center,
                   pygame.Vector2(1, 0).normalize(), 5, enemy_bullets, size=(25, 25))
            Bullet('enemy_bullet.png', self.rect.center,
                   pygame.Vector2(0, 1).normalize(), 5, enemy_bullets, size=(25, 25))
            Bullet('enemy_bullet.png', self.rect.center,
                   pygame.Vector2(0, -1).normalize(), 5, enemy_bullets, size=(25, 25))
            Bullet('enemy_bullet.png', self.rect.center,
                   pygame.Vector2(-1, -1).normalize(), 5, enemy_bullets, size=(25, 25))
            Bullet('enemy_bullet.png', self.rect.center,
                   pygame.Vector2(1, 1).normalize(), 5, enemy_bullets, size=(25, 25))
            Bullet('enemy_bullet.png', self.rect.center,
                   pygame.Vector2(-1, 1).normalize(), 5, enemy_bullets, size=(25, 25))
            Bullet('enemy_bullet.png', self.rect.center,
                   pygame.Vector2(1, -1).normalize(), 5, enemy_bullets, size=(25, 25))
            self.kill()


class Freeze_bullets(Bullet):
    def __init__(self, name, center, naprevl, speed, group, size=(0, 0)):
        super().__init__(name, center, naprevl, speed, group, size)
        self.freeze = False

    def update(self, screen, x):

        if x == 0:
            if not self.freeze:
                super().update(screen)

        elif x == 1:
            vx, vy = randrange(-10, 11), randrange(-10, 11)
            if vx == vy == 0:
                vx = -1
            self.naprevl = pygame.Vector2(vx, vy).normalize()
            self.speed = randrange(3, 7)
            self.freeze = True

            self.image = load_image('frozen_bullet.png')
            if self.size != (0, 0):
                self.image = pygame.transform.scale(self.image, self.size)  # Создание спрайта
            self.mask = pygame.mask.from_surface(self.image)

        elif x == 2:

            self.image = load_image('enemy_bullet.png')
            if self.size != (0, 0):
                self.image = pygame.transform.scale(self.image, self.size)  # Создание спрайта
            self.mask = pygame.mask.from_surface(self.image)

            self.freeze = False

# Новые классы пуль

class Guided_bullet(Bullet):
    def update(self, screen, hero):
        self.naprevl = pygame.Vector2(-self.rect.centerx + hero.rect.centerx,
                                      -self.rect.centery + hero.rect.centery).normalize()
        super().update(screen)


class Stop_Bullet(Bullet):
    def __init__(self, name, center, naprevl, speed, group, size=(0, 0), time=49, flag=True):
        super().__init__(name, center, naprevl, speed, group, size)
        self.stop_timer = 0
        self.time = time
        self.flag = flag

    def update(self, screen, hero):
        if self.stop_timer == self.time:
            if self.flag:
                self.naprevl = pygame.Vector2(hero.rect.centerx - self.rect.centerx,
                                              hero.rect.centery - self.rect.centery).normalize()
            self.stop_timer += 1
        elif self.stop_timer == self.time + 1:
            super().update(screen)
        else:
            self.stop_timer += 1

class Wall_bullet(Stop_Bullet):
    def update(self, screen):
        if self.stop_timer == self.time:
            self.kill()
        else:
            self.stop_timer += 1