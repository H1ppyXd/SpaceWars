import pygame
from load_methods import load_image


class Bullet(pygame.sprite.Sprite):     # Класс пули

    # Переменные: название спрайта, центр пули (начальная точка), направление движения, скорость пули,
    # группы спрайтов, размер пули.

    def __init__(self, name, center, naprevl, speed, *group, size=(0, 0)):

        super().__init__(group)         # Добавление пули в группы

        self.naprevl = naprevl
        self.speed = speed

        self.image = load_image(name)                               # Создание спрайта
        self.rect = self.image.get_rect(center=center)
        if size != (0, 0):
            self.image = pygame.transform.scale(self.image, size)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = pygame.Vector2(self.rect.center)

    def update(self, screen):

        self.pos += self.naprevl * self.speed       # Движение пули
        self.rect.center = self.pos

        if not screen.get_rect().contains(self.rect):       # Проверка выхода за экран
            self.kill()
