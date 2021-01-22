import pygame
import load_methods
from Bullets import Bullet
import math
from sprite_groups import *
import globals
from Circle import Circle


class Hero(pygame.sprite.Sprite):
    image = load_methods.load_image('Hero.png')

    def __init__(self, sprite_group, hp=5):
        super().__init__(sprite_group)
        Hero.image = pygame.transform.scale(Hero.image, (100, 100))
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 0
        self.pov = 0
        self.circle = 0
        self.rect.x = 100
        self.rect.y = 250
        self.dx = 0
        self.dy = 0
        self.hp = hp
        self.cooldown = globals.hero_cooldown
        self.cooldown_timer = 50
        self.inv = False
        self.inv_timer = -1

    def shot(self):
        if self.cooldown_timer == self.cooldown:
            Bullet('hero_bullet.png', self.rect.center,
                 pygame.Vector2(1, 0).normalize(), 5, hero_bullets, size=(25, 25))
            self.cooldown_timer = 0

    def shot_by_line(self):
        if self.cooldown_timer == self.cooldown:
            Bullet('hero_bullet.png', self.rect.center,
                   pygame.Vector2((self.rect.centerx + 800 * math.cos(self.angle)) - self.rect.centerx,
                                  (self.rect.centery + 800 * math.sin(self.angle))- self.rect.centery).normalize(),
                   7, hero_bullets, size=(25, 25))
            self.cooldown_timer = 0

    def update(self, x, y, screen):
        self.cooldown = globals.hero_cooldown
        if self.cooldown_timer < self.cooldown:
            self.cooldown_timer += 1
        elif self.cooldown_timer > self.cooldown:
            self.cooldown_timer = self.cooldown
        self.rect.x += x
        self.rect.y += y

        for bullet in wall_bullets:
            if pygame.sprite.collide_mask(self, bullet) and not self.inv:
                self.hp -= 1
                globals.enemys_killed -= 21
                globals.enemy_kill()
                self.inv = True
                self.rect.center = (400, 400)
                self.inv_timer = 40
        for bullet in bullet_wall:
            if pygame.sprite.collide_mask(self, bullet) and not self.inv:
                self.hp -= 1
                globals.enemys_killed -= 21
                globals.enemy_kill()
                self.inv = True
                self.rect.x = 700
                self.inv_timer = 40

        for bullet in boss_sprite:
            if pygame.sprite.collide_mask(self, bullet) and not self.inv:
                self.hp -= 1
                globals.enemys_killed -= 21
                globals.enemy_kill()
                self.inv = True
                self.inv_timer = 0
        for group in [enemy_bullets, snipers, evil_sprites, boss_bullets, guided_bullet, stop_bullets]:
            for bullet in group:
                if pygame.sprite.collide_mask(self, bullet) and not self.inv:
                    self.hp -= 1
                    globals.enemys_killed -= 21
                    globals.enemy_kill()
                    self.inv = True
                    self.inv_timer = 0
                    bullet.kill()

        if self.hp <= 0:
            globals.is_still_alive = 0
            guided_bullet.empty()

        if self.inv_timer == 0:
            self.circle = Circle('skyblue', rad=50)
        elif self.inv_timer == 100:
            if self.circle != 0:
                self.circle.kill()
            self.circle = 0
            self.inv = False
            self.inv_timer = -1
        if self.inv_timer != -1:
            self.inv_timer += 1

        if self.circle != 0:
            self.circle.rect.center = self.rect.center
            self.circle.rect.centerx -= 5
            self.circle.rect.centery -= 5

    def rotate(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        screen.blit(rotated_image, rotated_image.get_rect())
        pygame.display.flip()

    def get_pos(self):
        return self.rect.x, self.rect.y