# -*- coding = utf-8 -*-
import pygame
from pygame.locals import *
import time
def main():
    #1、创建窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)
    #2、创建一个背景图片
    background = pygame.image.load("./images/background.png")
    #3、创建一个飞机
    aircraft = pygame.image.load("./images/hero1.png")
    x = 200
    y = 700
    while True:
        screen.blit(background, (0, 0))
        screen.blit(aircraft, (x, y))
        pygame.display.update()

        #获取用户点击事件
        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                    if x > 0:
                        x -= 5
                    else:
                        x = x
                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                    if x > 480:
                        x = x
                    else:
                        x += 5
                elif event.key == K_w or event.key == K_UP:
                    print("up")
                    if y < 0:
                        y = y
                    else:
                        y -= 5
                elif event.key == K_s or event.key == K_DOWN:
                    print("down")
                    if y > 780:
                        y = y
                    else:
                        y += 5
                elif event.key == K_SPACE:
                    print("space")





        time.sleep(0.01)

if __name__ == "__main__":
    main()