import pygame
from load_methods import load_image
from Bullets import Bullet


pygame.init()
screen = pygame.display.set_mode((500, 500))    # Создание экрана

bullets = pygame.sprite.Group()                 # Группы для спрайтов пуль и врагов/героя
enemy_sprites = pygame.sprite.Group()
hero_bullets = pygame.sprite.Group()

clock = pygame.time.Clock()


class Enemy(pygame.sprite.Sprite):                              # Тестовый класс врага

    # Передаваемые значения: название спрайта, группы спрайтов, скорость движения, размер спрайта.
    def __init__(self, name, flag_moving_left, *group, speed=3, size=(0, 0), hp=3):

        super().__init__(group)                     # Добавление спрайта в группы
        self.flag_moving_left = flag_moving_left    # Флаг движения вперед
        self.go_down_flag = True                    # Флаг движения вверх/вниз
        self.hp = hp                                # Количество Hp
        self.angle = 90                             # Угол стрельбы
        self.speed = speed                          # Скорость движения
        self.direction = pygame.Vector2(1, 0)       # Направление стрельбы

        self.image = load_image(name)                                   # Создание спрайта
        self.image = pygame.transform.rotate(self.image, self.angle)
        if size != (0, 0):
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = 500

        self.pos = pygame.Vector2(self.rect.center)

        self.cooldown = 0               # Таймер перезарядки

    def front_shot(self):                                               # Создание пули
        self.groups()[0].add(Bullet('crystal.png', self.rect.center,
                                    pygame.Vector2(0, -1).rotate(-self.angle).normalize(),
                                    5, bullets, size=(30, 30)))

    def update(self, events):

        if self.cooldown == 30:         # Выстрел/перезарядка
            self.cooldown = 0
            self.front_shot()
        else:
            self.cooldown += 1

        if not self.flag_moving_left:                          # Движение
            if self.go_down_flag:
                self.rect.y += self.speed
            else:
                self.rect.y -= self.speed

            if not screen.get_rect().contains(self.rect):       # Проверка выхода за пределы экрана
                if self.go_down_flag:
                    self.go_down_flag = False
                else:                                       # Изменение направления движения
                    self.go_down_flag =True

        else:
            self.rect.x -= self.speed

        for bullet in hero_bullets:                         # Проверка попадания пули героя
            if pygame.sprite.collide_mask(self, bullet):
                self.hp -= 1
                bullet.kill()
        if self.hp == 0:
            self.kill()



def main():

    Enemy('ship.png', True, enemy_sprites, size=(50, 50), speed=5)
    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    for enemy in enemy_sprites:
                        enemy.flag_moving_left = True
                elif e.key == pygame.K_UP:
                    for enemy in enemy_sprites:
                        enemy.flag_moving_left = False
                        enemy.go_down_flag = False
                else:
                    for enemy in enemy_sprites:
                        enemy.flag_moving_left = False
                        enemy.go_down_flag = True

        enemy_sprites.update(events)
        screen.fill((30, 30, 30))
        enemy_sprites.draw(screen)
        pygame.display.update()
        clock.tick(20)

if __name__ == '__main__':
    main()