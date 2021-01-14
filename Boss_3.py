import pygame
from load_methods import load_image
from Bullets import *
from sprite_groups import *
from random import randrange, choice
import globals
from Circle import Circle


class Boss_3(pygame.sprite.Sprite):
    def __init__(self, hero):
        super().__init__(boss_sprite)
        self.hp = 350
        self.atcs = ['square', 'wall', 'weel']
        self.now_atc = 'weel'
        self.invicsibility = False
        self.hero = hero
        self.image = load_image('Boss_3.png')
        self.rect = self.image.get_rect()
        self.rect.x = 850
        self.rect.y = 310

        self.color = 'green'

        self.circle_cooldown = 1000
        self.cooldown_timer = 0
        self.cooldown = 300

        self.square = -1
        self.wall = -1
        self.weel = -1
        self.icicle = -1
        self.fan = -1
        self.fall = -1
        self.marionette = -1
        self.marionette_t = 0
        self.world = -1
        self.mirror = -1
        self.arrows = -1

    def update(self, screen):

        if self.cooldown_timer == self.cooldown:
            while True:
                atc = choice(self.atcs)
                if atc != self.now_atc:
                    self.now_atc = atc
                    break
                elif atc == 'world':
                    self.now_atc = atc
                    break
            if self.now_atc == 'square':
                self.cooldown_timer = 0
                self.square = 0
            elif self.now_atc == 'wall':
                self.cooldown_timer = 0
                self.wall = 0
            elif self.now_atc == 'weel':
                self.cooldown_timer = 0
                self.weel = 0
            elif self.now_atc == 'icicle':
                self.cooldown_timer = 0
                self.icicle = 0
            elif self.now_atc == 'fan':
                self.cooldown_timer = 0
                self.fan = 0
            elif self.now_atc == 'fall':
                self.cooldown_timer = 0
                self.fall = 0
            elif self.now_atc == 'marionette':
                self.cooldown_timer = 0
                self.marionette = 0
            elif self.now_atc == 'mirror':
                self.cooldown_timer = 0
                self.mirror = 0
            elif self.now_atc == 'arrows':
                self.cooldown_timer = 0
                self.arrows = 0
            elif self.now_atc == 'world':
                self.cooldown_timer = 0
                self.world = 0

        elif self.square != -1:
            if self.square == 0:
                for _ in range(25, 100, 25):
                    Bullet('enemy_bullet.png', (_, 25),
                   pygame.Vector2(0, 1).normalize(), 5, enemy_bullets, size=(25, 25))
                for _ in range(200, 800, 25):
                    Bullet('enemy_bullet.png', (_, 25),
                   pygame.Vector2(0, 1).normalize(), 5, enemy_bullets, size=(25, 25))
                self.square += 1
            elif self.square == 150:
                for _ in range(25, 650, 25):
                    Bullet('enemy_bullet.png', (25, _),
                   pygame.Vector2(1, 0).normalize(), 5, enemy_bullets, size=(25, 25))
                for _ in range(750, 800, 25):
                    Bullet('enemy_bullet.png', (25, _),
                   pygame.Vector2(1, 0).normalize(), 5, enemy_bullets, size=(25, 25))
                self.square += 1
            elif self.square == 300:
                for _ in range(25, 650, 25):
                    Bullet('enemy_bullet.png', (_, 775),
                   pygame.Vector2(0, -1).normalize(), 5, enemy_bullets, size=(25, 25))
                for _ in range(750, 800, 25):
                    Bullet('enemy_bullet.png', (_, 775),
                   pygame.Vector2(0, -1).normalize(), 5, enemy_bullets, size=(25, 25))
                self.square += 1
            elif self.square == 450:
                for _ in range(25, 100, 25):
                    Bullet('enemy_bullet.png', (775, _),
                   pygame.Vector2(-1, 0).normalize(), 5, enemy_bullets, size=(25, 25))
                for _ in range(200, 800, 25):
                    Bullet('enemy_bullet.png', (775, _),
                   pygame.Vector2(-1, 0).normalize(), 5, enemy_bullets, size=(25, 25))
                self.square += 1
            elif self.square == 600:
                self.square = -1
            else:
                self.square += 1

        elif self.wall != -1:
            if self.wall in range(0, 1500, 5) and self.wall % 75 < 25:
                Bullet('enemy_bullet.png', (25, 266),
                   pygame.Vector2(1, 0).normalize(), 5, enemy_bullets, size=(25, 25))
                Bullet('enemy_bullet.png', (975, 533),
                       pygame.Vector2(-1, 0).normalize(), 5, enemy_bullets, size=(25, 25))
                self.wall += 1
            elif self.wall == 1700:
                self.wall = -1
            else:
                self.wall += 1

            for el in range(0, 1500, 300):
                if self.wall == el + 1:
                    x = [1, 2, 3]
                    self.trt_0 = choice(x)
                    x.remove(self.trt_0)
                    self.trt_1 = choice(x)

                if self.wall in range(el + 2, el + 107):
                    if self.trt_0 == 1 or self.trt_1 == 1:
                        pygame.draw.line(screen, 'green', (400, 25), (400, 125), width=10)
                        pygame.draw.circle(screen, 'green', (400, 175), 10)
                    if self.trt_0 == 2 or self.trt_1 == 2:
                        pygame.draw.line(screen, 'green', (400, 325), (400, 425), width=10)
                        pygame.draw.circle(screen, 'green', (400, 475), 10)
                    if self.trt_0 == 3 or self.trt_1 == 3:
                        pygame.draw.line(screen, 'green', (400, 625), (400, 725), width=10)
                        pygame.draw.circle(screen, 'green', (400, 775), 10)

                if self.wall in range(el + 107, el + 243, 5):
                    if self.trt_0 == 1 or self.trt_1 == 1:
                        Bullet('enemy_bullet.png', (25, randrange(25, 200)),
                               pygame.Vector2(1, 0).normalize(), 10, enemy_bullets, size=(25, 25))
                        Bullet('enemy_bullet.png', (975, randrange(25, 200)),
                               pygame.Vector2(-1, 0).normalize(), 10, enemy_bullets, size=(25, 25))
                    if self.trt_0 == 2 or self.trt_1 == 2:
                        Bullet('enemy_bullet.png', (25, randrange(250, 520)),
                               pygame.Vector2(1, 0).normalize(), 10, enemy_bullets, size=(25, 25))
                        Bullet('enemy_bullet.png', (975, randrange(250, 520)),
                               pygame.Vector2(-1, 0).normalize(), 10, enemy_bullets, size=(25, 25))
                    if self.trt_0 == 3 or self.trt_1 == 3:
                        Bullet('enemy_bullet.png', (25, randrange(560, 775)),
                               pygame.Vector2(1, 0).normalize(), 10, enemy_bullets, size=(25, 25))
                        Bullet('enemy_bullet.png', (975, randrange(560, 775)),
                               pygame.Vector2(-1, 0).normalize(), 10, enemy_bullets, size=(25, 25))

        elif self.weel != -1:
            if self.weel in range(0, 100):
                pygame.draw.circle(screen, (255, 0, 0, 100), (500, 400), 75)
                self.weel += 1
            elif self.weel == 100:
                self.circle.kill()
                self.circle_cooldown = -1
                self.rect.center = (500, 400)
                self.weel += 1
                self.angle = 0
            elif self.weel in range(200, 2000, 10):
                Bullet('enemy_bullet.png', (500, 400),
                       pygame.Vector2(-1, 0).rotate(self.angle).normalize(), 4, enemy_bullets, size=(25, 25))
                Bullet('enemy_bullet.png', (500, 400),
                       pygame.Vector2(1, 0).rotate(self.angle).normalize(), 4, enemy_bullets, size=(25, 25))
                Bullet('enemy_bullet.png', (500, 400),
                       pygame.Vector2(0, -1).rotate(self.angle).normalize(), 4, enemy_bullets, size=(25, 25))
                Bullet('enemy_bullet.png', (500, 400),
                       pygame.Vector2(0, 1).rotate(self.angle).normalize(), 4, enemy_bullets, size=(25, 25))
                self.angle -= 10
                self.weel += 1
            elif self.weel in range(2000, 2100):
                pygame.draw.circle(screen, (255, 0, 0, 100), (850, 310), 75)
                self.weel += 1
            elif self.weel == 2100:
                self.weel = -1
                self.circle.kill()
                self.circle_cooldown = 1000
                self.rect.center = (850, 310)
            else:
                self.weel += 1

        elif self.icicle != -1:
            if self.icicle in range(0, 201, 40):
                for _ in range(25, 1000, 125):
                    Freeze_bullets('enemy_bullet.png', (975, _),
                       pygame.Vector2(-1, 0).normalize(), 4, boss_bullets, size=(25, 25))
            elif self.icicle == 220:
                boss_bullets.update(screen, 1)
            elif self.icicle in range(250, 551, 4):
                Bullet('enemy_bullet.png', self.rect.center,
                               pygame.Vector2(randrange(-7, -1), randrange(-5, 6)).normalize(),
                               randrange(3, 6), enemy_bullets, size=(25, 10))
            elif self.icicle == 750:
                for blt in boss_bullets:
                    blt.speed = 1
                boss_bullets.update(screen, 2)
            elif self.icicle == 1000:
                boss_bullets.empty()
                self.icicle = -2
            self.icicle += 1

        elif self.fan != -1:
            if self.fan in range(0, 1001, 100):
                x = randrange(1, 5)
                if x == 1:
                    for _ in range(25, 800, 25):
                        Bullet('enemy_bullet.png', (975, _),
                           pygame.Vector2(self.hero.rect.centerx - 975, self.hero.rect.centery - _).normalize(),
                               5, enemy_bullets, size=(25, 25))
                if x == 2:
                    for _ in range(25, 800, 25):
                        Bullet('enemy_bullet.png', (25, _),
                           pygame.Vector2(self.hero.rect.centerx - 25, self.hero.rect.centery - _).normalize(),
                               5, enemy_bullets, size=(25, 25))
                if x == 3:
                    for _ in range(25, 800, 25):
                        Bullet('enemy_bullet.png', (_, 25),
                           pygame.Vector2(self.hero.rect.centerx - _, self.hero.rect.centery - 25).normalize(),
                               5, enemy_bullets, size=(25, 25))
                if x == 4:
                    for _ in range(25, 800, 25):
                        Bullet('enemy_bullet.png', (_, 775),
                           pygame.Vector2(self.hero.rect.centerx - _, self.hero.rect.centery - 775).normalize(),
                               5, enemy_bullets, size=(25, 25))
            elif self.fan == 1100:
                self.fan = -2
            self.fan += 1

        elif self.fall != -1:
            if self.fall == 0:
                self.napravl = 2
            if self.fall in range(0, 401, 80):
                for _ in [[-1, 'r'], [1, 'l']]:
                    Rottating_bullet('enemy_bullet.png', self.rect.center,
                                     pygame.Vector2(self.napravl, _[0] * 10).normalize(),
                                     5, enemy_bullets, _[1], 90, size=(25, 25))

            elif self.fall in range(20, 421, 80):
                for _ in [[-1, 'r'], [1, 'l']]:
                    Rottating_bullet('enemy_bullet.png', self.rect.center,
                                     pygame.Vector2(self.napravl, _[0] * 10).normalize(),
                                     5, enemy_bullets, _[1], 65, size=(25, 25))

            elif self.fall in range(40, 441, 80):
                for _ in [[-1, 'r'], [1, 'l']]:
                    Rottating_bullet('enemy_bullet.png', self.rect.center,
                                     pygame.Vector2(self.napravl, _[0] * 10).normalize(),
                                     5, enemy_bullets, _[1], 40, size=(25, 25))
            elif self.fall in range(60, 461, 80):
                for _ in [[-1, 'r'], [1, 'l']]:
                    Rottating_bullet('enemy_bullet.png', self.rect.center,
                                     pygame.Vector2(self.napravl, _[0] * 10).normalize(),
                                     5, enemy_bullets, _[1], 15, size=(25, 25))
                self.napravl -= 2
            elif self.fall == 600:
                self.fall = -2
            self.fall += 1

        elif self.marionette != -1:
            if self.marionette == 0:
                self.x, self.y = self.hero.rect.centerx - self.rect.centerx, self.hero.rect.centery - self.rect.centery
            if self.marionette in range(0, 121, 30):
                x = 100
                for el in range(3):
                    b = Bullet('enemy_bullet.png', self.rect.center,
                               pygame.Vector2(self.x, self.y + x).normalize(), 4, enemy_bullets, size=(31, 10))
                    b.rotate(pygame.Vector2(-1, 0))
                    x -= 100
            elif self.marionette == 150:
                globals.time_stop = True
                for bullet in enemy_bullets:
                    for el in range(3):
                        b = Bullet('time_stop_bullet.png', bullet.rect.center,
                                   pygame.Vector2(randrange(-50, 51), randrange(-50, 51)).normalize(),
                                   4, enemy_bullets, size=(26, 7))
                        b.rotate(bullet.naprevl)
                enemy_bullets.draw(screen)
            elif self.marionette == 230:
                globals.time_stop = False
            if len(enemy_bullets) <= 10 and self.marionette > 200:
                self.marionette_t += 1
                if self.marionette_t == 3:
                    self.marionette_t = 0
                    self.marionette = -2
                else:
                    self.marionette = -1
            self.marionette += 1

        elif self.arrows != -1:
            if self.arrows == 0:
                for vect in [(-2, 1), (-2, -1), (-1, -1), (-1, 1), (-1, 2), (-1, -2), (-4, 1), (-4, -1)]:
                    b = Mirror_bullet('ricochet_bullet.png', self.rect.center, pygame.Vector2(vect).normalize(),
                                      8, enemy_bullets, cols=10, size=(51, 16))
                    b.rotate(pygame.Vector2(-1, 0))
            elif self.arrows in range(100, 601, 200):
                for el in range(3):
                    while True:
                        globals.time_stop = True
                        c = self.hero.rect.center - pygame.Vector2(randrange(-10, 11),
                                                                         randrange(-10, 11)).normalize() * 250
                        b = Bullet('time_stop_bullet.png', c, pygame.Vector2(self.hero.rect.centerx - c[0],
                                                                         self.hero.rect.centery - c[1]).normalize(),
                                      4, enemy_bullets, size=(41, 13))
                        if screen.get_rect().contains(b.rect):
                            b.rotate(pygame.Vector2(-1, 0))
                            break
            elif self.arrows in range(170, 671, 200):
                globals.time_stop = False
            elif self.arrows >= 800:
                self.arrows = -2
                enemy_bullets.empty()
            self.arrows += 1

        elif self.mirror != -1:
            if self.mirror in range(0, 101, 2):
                self.angle = 0
                self.rect.centerx -= 2
                self.circle.rect.centerx -= 2
            if self.mirror in range(121, 172, 10):
                for x in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    for s in [3, 2]:
                        b = Mirror_bullet('ricochet_bullet.png', self.rect.center,
                                   pygame.Vector2(x).normalize().rotate(self.angle), s, enemy_bullets, size=(41, 13))
                        b.rotate(pygame.Vector2(-1, 0))
                    self.angle += 3
            elif self.mirror in range(1600, 1701, 2):
                self.rect.centerx += 2
                self.circle.rect.centerx += 2
            elif self.mirror >= 500 and self.mirror <= 1550 and len(enemy_bullets) <= 10:
                enemy_bullets.empty()
                self.mirror = 1550
            elif self.mirror == 1701:
                self.mirror = -2
            self.mirror += 1

        elif self.world != -1:
            if self.world in range(0, 50, 5):
                self.rect.centery += 5
                self.circle.rect.centery += 5
            if self.world in range(50, 161, 20):
                for vect in [(-1, 0), (-1, -1), (-1, 1), (0, 1), (0, -1),
                             (-1, 2), (-1, -2), (-2, 1), (-2, -1)]:
                    b = Bullet('enemy_bullet.png', (self.rect.centerx, self.rect.centery - 15),
                               pygame.Vector2(vect).normalize(), 4, enemy_bullets, size=(61, 25))
                    b.rotate(pygame.Vector2(-1, 0))
            elif self.world == 180:
                globals.time_stop = True
            elif self.world == 190:
                for el in [(1, 0), (1, 1), (1, -1), (2, 1), (2, -1)]:
                    for _ in range(-1, 2):
                        b = Bullet('time_stop_bullet.png', self.hero.rect.center + pygame.Vector2(el).normalize() * 400,
                                   pygame.Vector2((-el[0], -el[1] + _)).normalize(), 3, enemy_bullets, size=(41, 13))
                        for el1 in range(2):
                            q = Bullet('emerald_bullet.png', b.rect.center,
                                       pygame.Vector2(randrange(-50, 51), randrange(-50, 51)).normalize(),
                                       3, enemy_bullets, size=(26, 7))
                            q.rotate(b.naprevl)
                        b.rotate(pygame.Vector2(-1, 0))
            elif self.world == 200:
                for el in [(3, 1), (3, -1), (3, -2), (3, 2), (4, 1), (4, -1)]:
                    for _ in range(-1, 2):
                        b = Bullet('time_stop_bullet.png', self.hero.rect.center + pygame.Vector2(el).normalize() * 500,
                                   pygame.Vector2((-el[0], -el[1] + _)).normalize(), 3, enemy_bullets, size=(41, 13))
                        for el1 in range(2):
                            q = Bullet('time_stop_bullet.png', b.rect.center,
                                       pygame.Vector2(randrange(-50, 51), randrange(-50, 51)).normalize(),
                                       3, enemy_bullets, size=(26, 7))
                            q.rotate(b.naprevl)
                        b.rotate(pygame.Vector2(-1, 0))
            elif self.world == 210:
                for el in [(1, 2), (1, -2), (2, 3), (2, -3)]:
                    for _ in range(-1, 2):
                        b = Bullet('time_stop_bullet.png', self.hero.rect.center + pygame.Vector2(el).normalize() * 500,
                                   pygame.Vector2((-el[0], -el[1] + _)).normalize(), 3, enemy_bullets, size=(41, 13))
                        for el1 in range(2):
                            q = Bullet('time_stop_bullet.png', b.rect.center,
                                       pygame.Vector2(randrange(-50, 51), randrange(-50, 51)).normalize(),
                                       3, enemy_bullets, size=(26, 7))
                            q.rotate(b.naprevl)
                        b.rotate(pygame.Vector2(-1, 0))
            elif self.world == 220:
                globals.time_stop = False
            if len(enemy_bullets) == 0 and self.world > 300:
                self.world = 49
            self.world += 1

        else:
            self.cooldown_timer += 1


        if self.circle_cooldown != -1:
            if self.circle_cooldown == 1000:
                self.circle = Circle(self.color)
                self.circle.rect.center = self.rect.center
                self.circle_cooldown = 0
            elif len(circles) == 0:
                self.circle_cooldown += 1

        if globals.movement == 0:
            if len(circles) != 0:
                if self.color == 'green':
                    globals.speed = 3
                if self.color == 'red':
                    vector = pygame.Vector2(self.rect.centerx - self.hero.rect.centerx,
                                   self.rect.centery - self.hero.rect.centery).normalize()
                    pos = pygame.Vector2(self.hero.rect.center)
                    pos += vector * 2
                    self.hero.rect.center = pos
                elif self.color == 'blue':
                    globals.uprav = False
                elif self.color == 'yellow':
                    if self.world == 300:
                        self.circle.kill()
                        self.color = 'black'
            else:
                globals.uprav = True
                globals.speed = 5

        if not self.invicsibility:
            for bullet in hero_bullets:
                if not self.invicsibility:
                    if pygame.sprite.collide_mask(self, bullet):
                        bullet.kill()
                        self.hp -= 1
            if self.hp == 250:
                self.color = 'red'
                self.atcs = ['icicle', 'fan', 'fall']
            elif self.hp == 150:
                self.color = 'blue'
                self.atcs = ['marionette', 'mirror', 'arrows']
            elif self.hp == 15 and self.atcs != ['world']:
                self.color = 'yellow'
                self.circle_cooldown = 999
                self.atcs = ['world']
            if self.hp <= 0:
                self.kill()
