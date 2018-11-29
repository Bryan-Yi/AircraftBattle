# -*- coding = utf-8 -*-


import pygame
from pygame.locals import *
import time


class HeroPlane(object):
    def __init__(self, screen_temp):
        self.x = 200
        self.y = 700
        self.screen = screen_temp
        self.image = pygame.image.load("./images/hero1.png")
        # 存储发射出去的子弹
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move_left(self):
        if self.x > -30:
            self.x -= 5
        else:
            self.x = self.x

    def move_right(self):
        if self.x > 450:
            self.x = self.x
        else:
            self.x += 5

    def move_up(self):
        if self.y < 0:
            self.y = self.y
        else:
            self.y -= 5

    def move_down(self):
        if self.y > 780:
            self.y = self.y
        else:
            self.y += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))


class EnemyPlane(object):
    def __init__(self, screen_temp):
        self.x = 0
        self.y = 0
        self.screen = screen_temp
        self.image = pygame.image.load("./images/enemy0.png")
        # 存储发射出去的子弹
        self.bullet_list = []
        self.direction = "right"

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)


    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5
        if self.x > 430:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))


def key_control(hero_temp):
    # 获取用户点击事件
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print("left")
                hero_temp.move_left()

            elif event.key == K_d or event.key == K_RIGHT:
                print("right")
                hero_temp.move_right()

            elif event.key == K_w or event.key == K_UP:
                print("up")
                hero_temp.move_up()

            elif event.key == K_s or event.key == K_DOWN:
                print("down")
                hero_temp.move_down()

            elif event.key == K_SPACE:
                print("space")
                hero_temp.fire()


class Bullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen_temp
        self.image = pygame.image.load("./images/bullet.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


def main():
    # 1、创建窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)
    # 2、创建一个背景图片
    background = pygame.image.load("./images/background.png")
    # 3、创建一个飞机
    hero = HeroPlane(screen)
    # 4、创建敌机
    enemy = EnemyPlane(screen)

    while True:
        screen.blit(background, (0, 0))
        hero.display()
        enemy.display()
        enemy.move()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)


if __name__ == "__main__":
    main()
