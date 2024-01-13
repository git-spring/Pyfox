# 键盘控制坦克移动
# 长按移动,松开停止

import pygame
import sys

from practise_game.base_practise.tank_game.base_item import BaseItem

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BG_COLOR = pygame.Color(0, 0, 0)


class Tank(BaseItem):
    def __init__(self, tank_pos):
        pygame.sprite.Sprite.__init__(self)
        self.images = {'W':pygame.image.load('tank/tankW.png'),
                      'S':pygame.image.load('tank/tankS.png'),
                      'A':pygame.image.load('tank/tankA.png'),
                      'D':pygame.image.load('tank/tankD.png')}
        self.direction = 'W'  # 坦克方向
        self.tank = self.images[self.direction]  # 根据方向获取图片
        self.rect = self.tank.get_rect()  # 图形区域
        self.rect.x = tank_pos[0]
        self.rect.y = tank_pos[1]
        self.speed = 10  # 坦克速度
        self.alive = True  # 坦克是否存活
        self.prev_x = self.rect.x  # 之前位置的X坐标
        self.prev_y = self.rect.y  # 之前位置的Y坐标

    def tank_move(self):
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        if self.direction == 'W':
            if self.rect.y > 0:
                self.rect.y -= self.speed
        elif self.direction == 'S':
            if self.rect.y + self.rect.height < SCREEN_HEIGHT:
                self.rect.y += self.speed
        elif self.direction == 'A':
            if self.rect.x > 0:
                self.rect.x -= self.speed
        elif self.direction == 'D':
            if self.rect.x + self.rect.width < SCREEN_WIDTH:
                self.rect.x += self.speed


class MainGame:

    def start_game(self):
        pygame.init()  # 初始化
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 设置窗口大小
        pygame.display.set_caption('Tank')  # 设置窗口名称
        # screen.fill((255,255,255))
        tank = Tank((150, 350))
        # pygame.sprite.Sprite.add(tank)
        pygame.display.flip()  # 第一次更新窗口

        while True:  # 死循环确保窗口一直显示
            for event in pygame.event.get():  # 遍历所有事件
                if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    tank.direction = str.upper(chr(event.key))
                    tank.tank = tank.images[tank.direction]
                    tank.tank_move()
                    # screen.blit(tank.tank, (tank.prev_x, tank.prev_y))

                    pygame.draw.rect(screen, (0,0,0),
                                     (tank.prev_x, tank.prev_y, tank.rect.width, tank.rect.height))  # 将坦克的上一个区域填充成背景色
            screen.blit(tank.tank, tank.rect)

            pygame.display.update()  #


if '__main__' == __name__:
    MainGame().start_game()
