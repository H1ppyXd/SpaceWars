import pygame
from load_methods import load_image
from sprite_groups import *

class Bullet(pygame.sprite.Sprite):     # Класс пули

    # Переменные: название спрайта, центр пули (начальная точка), направление движения, скорость пули,
    # группы спрайтов, размер пули.

    def __init__(self, name, center, naprevl, speed, group, size=(0, 0)):

        super().__init__(group)         # Добавление пули в группу

        self.naprevl = naprevl
        self.speed = speed

        self.image = load_image(name)
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
            Small_bullet('crystal1.png', self.rect.center,
                   pygame.Vector2(-2, -1).normalize(), 1, enemy_bullets, size=(30, 30))
            Small_bullet('crystal1.png', self.rect.center,
                   pygame.Vector2(-2, 1).normalize(), 1, enemy_bullets, size=(30, 30))
        else:
            self.timer += 1

class Small_bullet(Bullet):
    def __init__(self, name, center, naprevl, speed, group, size=(0, 0)):
        super().__init__(name, center, naprevl, speed, group, size)
        self.timer = 0

    def update(self, screen):
        super().update(screen)
        if self.timer == 125:
            self.kill()
        else:
            self.timer += 1

class Bullet_wall(Bullet):
    def update(self, screen):
        super().update(screen)
        if self.rect.x < 800:
            self.kill()


class Circle_bullet(Bullet):
    def update(self, screen):
        super().update(screen)
        if self.rect.centerx == 400:
            Bullet('crystal1.png', self.rect.center,
                   pygame.Vector2(-1, 0).normalize(), 5, enemy_bullets, size=(30, 30))
            Bullet('crystal1.png', self.rect.center,
                   pygame.Vector2(1, 0).normalize(), 5, enemy_bullets, size=(30, 30))
            Bullet('crystal1.png', self.rect.center,
                   pygame.Vector2(0, 1).normalize(), 5, enemy_bullets, size=(30, 30))
            Bullet('crystal1.png', self.rect.center,
                   pygame.Vector2(0, -1).normalize(), 5, enemy_bullets, size=(30, 30))
            Bullet('crystal1.png', self.rect.center,
                   pygame.Vector2(-1, -1).normalize(), 5, enemy_bullets, size=(30, 30))
            Bullet('crystal1.png', self.rect.center,
                   pygame.Vector2(1, 1).normalize(), 5, enemy_bullets, size=(30, 30))
            Bullet('crystal1.png', self.rect.center,
                   pygame.Vector2(-1, 1).normalize(), 5, enemy_bullets, size=(30, 30))
            Bullet('crystal1.png', self.rect.center,
                   pygame.Vector2(1, -1).normalize(), 5, enemy_bullets, size=(30, 30))
            self.kill()