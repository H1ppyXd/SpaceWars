import pygame
from load_methods import load_image
from Bullets import *
from sprite_groups import *
from random import randrange, choice
import globals


class Boss_2(pygame.sprite.Sprite):
    def __init__(self, hero):
        super().__init__(boss_sprite)
        self.hp = 753
        self.go_down_flag = True
        self.speed = 1
        self.hero = hero
        self.image = load_image('boss_2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 300
        self.atcs = ['bullet_rain', 'circle', 'shot', 'blaster']
        self.now_atc = ''
        self.invicsibility = False
        self.cooldown = 300
        self.cooldown_timer = 100
        self.stop_up = False
        self.circle = -1
        self.blaster = -1
        self.stop = -1
        self.last_atc_timer = -1
        self.doors_timer = -1
        self.doors = 0
        self.rain = -1
        self.timers = [self.blaster, self.stop, self.rain, self.circle]

    def bullet_rain(self):
        Bullet('enemy_bullet.png', (randrange(20, 800), 20),
               pygame.Vector2(0, 1).normalize(), 3, enemy_bullets, size=(20, 20))

    def blast(self):
        while True:
            x_1, x_2, y_1, y_2 = 0, 0, 0, 0
            if self.hero.rect.centerx - 100 > 80:
                x_1 = self.hero.rect.centerx - 100
            if self.hero.rect.centerx + 100 < 720:
                x_2 = self.hero.rect.centerx + 100
            if self.hero.rect.centery - 100 > 80:
                y_1 = self.hero.rect.centery - 100
            if self.hero.rect.centery + 100 < 720:
                y_2 = self.hero.rect.centery + 100
            if x_1 == 0:
                x = randrange(x_2, 760)
            elif x_2 == 0:
                x = randrange(40, x_1)
            elif x_1 == x_2 == 0:
                x = 400
            else:
                x = choice([randrange(40, x_1), randrange(x_2, 760)])
            if y_1 == 0:
                y = randrange(y_2, 760)
            elif y_1 == y_2 == 0:
                y = 400
            elif y_2 == 0:
                y = randrange(40, y_1)
            else:
                y = choice([randrange(40, y_1), randrange(y_2, 760)])
            break
        Stop_Bullet('enemy_bullet.png', (x, y),
               pygame.Vector2(0, 1).normalize(), 13, stop_bullets, size=(40, 40), time=29)
        self.cooldown_timer = -300

    def update(self, screen):
        if len(guided_bullet) == 0 and self.now_atc != 'circle' and self.cooldown_timer == 1:
            Guided_bullet('guided_bullet.png', self.rect.center,
                   pygame.Vector2(-1, 0).normalize(), 1, guided_bullet, size=(20, 20))

        if self.cooldown_timer > self.cooldown:
            self.cooldown_timer = 0

        if self.cooldown_timer == self.cooldown and len(enemy_bullets) == 0 \
                and len(stop_bullets) == 0 and self.doors_timer == -1:
            while True:
                atc = choice(self.atcs)
                if atc != self.now_atc:
                    self.now_atc = atc
                    break
            if self.now_atc == 'bullet_rain':
                self.cooldown_timer = 0
                self.rain = 0
            elif self.now_atc == 'shot':
                self.stop = 0
                self.cooldown_timer = 0
            elif self.now_atc == 'blaster':
                self.blaster = 0
                self.cooldown_timer = 0
            elif self.now_atc == 'circle':
                self.circle = 0
                self.cooldown_timer = 0
        elif all([el == -1 for el in self.timers]):
            self.cooldown_timer += 1

        if self.rain in range(0, 350, 10):
            self.bullet_rain()
            self.rain += 1
        elif self.rain == 351:
            self.rain = -1
            self.cooldown_timer = 0
        elif self.rain != -1:
            self.rain += 1

        if self.blaster in range(0, 1000, 100):
            self.blast()
            self.blaster += 1
            self.cooldown_timer = 0
        elif self.blaster == 1001:
            self.blaster = -1
            self.cooldown_timer = 0
        elif self.blaster != -1:
            self.blaster += 1

        if self.circle == 60:
            x = 70
            for _ in range(3):
                for el in [pygame.Vector2(0, -1).normalize(), pygame.Vector2(1, -4.5).normalize(),
                           pygame.Vector2(2, -4.5).normalize(), pygame.Vector2(2, -3).normalize(),
                           pygame.Vector2(1, -1).normalize(), pygame.Vector2(3, -2).normalize(),
                           pygame.Vector2(4.5, -2).normalize(), pygame.Vector2(4.5, -1).normalize(),

                           pygame.Vector2(1, 0).normalize(), pygame.Vector2(4.5, 1).normalize(),
                           pygame.Vector2(4.5, 2).normalize(), pygame.Vector2(3, 2).normalize(),
                           pygame.Vector2(1, 1).normalize(), pygame.Vector2(2, 3).normalize(),
                           pygame.Vector2(2, 4.5).normalize(), pygame.Vector2(1, 4.5).normalize(),

                           pygame.Vector2(0, 1).normalize(), pygame.Vector2(-1, 4.5).normalize(),
                           pygame.Vector2(-2, 4.5).normalize(), pygame.Vector2(-2, 3).normalize(),
                           pygame.Vector2(-1, 1).normalize(), pygame.Vector2(-3, 2).normalize(),
                           pygame.Vector2(-4.5, 2).normalize(), pygame.Vector2(-4.5, 1).normalize(),

                           pygame.Vector2(-1, 0).normalize(), pygame.Vector2(-4.5, -1).normalize(),
                           pygame.Vector2(-4.5, -2).normalize(), pygame.Vector2(-3, -2).normalize(),
                           pygame.Vector2(-1, -1).normalize(), pygame.Vector2(-2, -3).normalize(),
                           pygame.Vector2(-2, -4.5).normalize(), pygame.Vector2(-1, -4.5).normalize()]:
                    Wall_bullet('enemy_bullet.png', (400, 400) + el * 270,
                        -el, 15, wall_bullets, size=(35, 35), time=x)
                    Stop_Bullet('enemy_bullet.png', (400, 400) + el * 270,
                        -el, 15, stop_bullets, size=(35, 35), time=x, flag=False)
                    x += 8
            self.circle = -1
            self.cooldown_timer = 0
        elif self.circle == 0:
            globals.teleportation = 0
            globals.tp_flag = True
            self.circle += 1
            guided_bullet.empty()
            self.hero.rect.center = (400, 400)
        elif self.circle in range(1, 60):
            self.circle += 1

        if self.stop in range(25, 775, 25):
            if not self.stop_up:
                Stop_Bullet('enemy_bullet.png', (650, self.stop),
                   pygame.Vector2(-1, 0).normalize(), 7, stop_bullets, size=(25, 25))
                self.stop += 1
            else:
                Stop_Bullet('enemy_bullet.png', (650, 800 - self.stop),
                   pygame.Vector2(-1, 0).normalize(), 7, stop_bullets, size=(25, 25))
                self.stop += 1
        elif self.stop == 751:
            if not self.stop_up:
                self.stop = 1
                self.stop_up = True
            else:
                self.stop = -1
                self.stop_up = False
                self.cooldown_timer = 0
        elif self.stop != -1:
            self.stop += 1

        if (self.hp == 201 or self.hp == 352 or self.hp == 503) and self.cooldown_timer == 290\
                and len(enemy_bullets) == 0 and len(stop_bullets) == 0 and self.invicsibility:
            self.doors_timer = 0

        if self.doors_timer != -1:
            if self.doors_timer == 0:
                for el in range(25, 350, 25):
                    Bullet('enemy_bullet.png', (el, 25), pygame.Vector2(0, 1).normalize(),
                           4, enemy_bullets, size=(25, 25))
                for el in range(450, 800, 25):
                    Bullet('enemy_bullet.png', (el, 25), pygame.Vector2(0, 1).normalize(),
                           4, enemy_bullets, size=(25, 25))
                self.doors_timer += 1
                self.cooldown_timer = 0
            if self.doors_timer in (200, 300, 400, 500, 600):
                x = choice([4, 5])
                if self.doors in (150, 300):
                    door = randrange(150, 401, 25)
                elif self.doors in (400, 551):
                    door = randrange(300, 551, 25)
                else:
                    door = randrange(250, 451, 25)
                self.doors = door
                for el in range(25, 350, 25):
                    Bullet('enemy_bullet.png', (el, 25), pygame.Vector2(0, 1).normalize(),
                           4, enemy_bullets, size=(25, 25))
                for el in range(450, 800, 25):
                    Bullet('enemy_bullet.png', (el, 25), pygame.Vector2(0, 1).normalize(),
                           4, enemy_bullets, size=(25, 25))
                for el in range(25, door, 25):
                    Bullet('enemy_bullet.png', (25, el), pygame.Vector2(1, 0).normalize(),
                           x, enemy_bullets, size=(25, 25))
                for el in range(door + 100, 800, 25):
                    Bullet('enemy_bullet.png', (25, el), pygame.Vector2(1, 0).normalize(),
                           x, enemy_bullets, size=(25, 25))
                for el in range(25, door, 25):
                    Bullet('enemy_bullet.png', (750, el), pygame.Vector2(-1, 0).normalize(),
                           x, enemy_bullets, size=(25, 25))
                for el in range(door + 100, 800, 25):
                    Bullet('enemy_bullet.png', (750, el), pygame.Vector2(-1, 0).normalize(),
                           x, enemy_bullets, size=(25, 25))
                self.cooldown_timer = 0
                self.doors_timer += 1
            elif self.doors_timer == 700:
                self.doors_timer = -1
                self.invicsibility = False
                self.hp -= 1
                self.cooldown_timer = 0
                self.doors = 0
            else:
                guided_bullet.empty()
                self.doors_timer += 1
                self.cooldown_timer = 0

        if self.go_down_flag:
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed
        if self.hp == 1 and self.invicsibility and self.last_atc_timer == -1 and self.cooldown_timer == 299:
            self.last_atc_timer = 0
        if self.last_atc_timer != -1:
            guided_bullet.empty()
            if self.last_atc_timer == 0:
                self.last_atc_timer += 1
                for el in range(25, 350, 25):
                    Bullet('enemy_bullet.png', (el, 25), pygame.Vector2(0, 1).normalize(),
                           4, enemy_bullets, size=(25, 25))
                for el in range(450, 800, 25):
                    Bullet('enemy_bullet.png', (el, 25), pygame.Vector2(0, 1).normalize(),
                           4, enemy_bullets, size=(25, 25))
            if self.last_atc_timer == 20:
                for el in range(0, 1000, 7):
                    if el in range(0, 300):
                        x = 525
                        y = 500
                    elif el in range(300, 600):
                        for el1 in range(300, 600, 100):
                            if el < el1:
                                mn = (el - el1) // 100
                        x += 5 * mn
                        y += 5 * mn
                    elif el in range(600, 1000):
                        for el1 in range(600, 1000, 100):
                            if el < el1:
                                mn = (el - el1) // 100
                        x -= 5 * mn
                        y -= 5 * mn
                    Stop_Bullet('enemy_bullet.png', (800, x - 200), pygame.Vector2(-1, 0).normalize(),
                           4, stop_bullets, size=(25, 25), time=el, flag=False)
                    Stop_Bullet('enemy_bullet.png', (800, x), pygame.Vector2(-1, 0).normalize(),
                           4, stop_bullets, size=(25, 25), time=el, flag=False)
                    Stop_Bullet('enemy_bullet.png', (y, 25), pygame.Vector2(0, 1).normalize(),
                           4, stop_bullets, size=(25, 25), time=el, flag=False)
                    Stop_Bullet('enemy_bullet.png', (y - 200, 25), pygame.Vector2(-0, 1).normalize(),
                           4, stop_bullets, size=(25, 25), time=el, flag=False)
                self.last_atc_timer += 1
            elif self.last_atc_timer == 1300:
                self.invicsibility = False
                self.hp -= 1
            else:
                self.last_atc_timer += 1
                self.cooldown_timer = -300

        if not screen.get_rect().contains(self.rect):       # Проверка выхода за пределы экрана
            if self.go_down_flag:
                self.go_down_flag = False
            else:                                       # Изменение направления движения
                self.go_down_flag = True

        if not self.invicsibility:
            for bullet in hero_bullets:
                if not self.invicsibility:
                    if pygame.sprite.collide_mask(self, bullet):
                        bullet.kill()
                        self.hp -= 1
                        if (self.hp == 1 or self.hp == 201 or self.hp == 352 or self.hp == 503)\
                                and not self.invicsibility:
                            self.invicsibility = True
                            self.circle = -1
                            self.blaster = -1
                            self.stop = -1
                            self.rain = -1
                            enemy_bullets.empty()
                            stop_bullets.empty()
                            wall_bullets.empty()
                            self.cooldown_timer = 0
            if self.hp <= 0:
                self.hero.hp += 1
                globals.enem_to += 50
                self.kill()
                guided_bullet.empty()
                globals.now_boss_flag = False
                globals.snipers.append('cline_shot')
                globals.snipers.remove(globals.snipers[0])
                globals.enemys.append('giant_shot')
                globals.enemys.remove(globals.enemys[0])
                globals.flag += 1
